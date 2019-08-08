import json, os

fileName = "C:\\Users\\DELL\\Desktop\\car300\\data\\data_2.json"
readingSave = "C:\\Users\\DELL\\Desktop\\car300\\data\\readingSave.txt"
NOT_MARKED = 9

def saveJson(data):
    with open(fileName, 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(data,indent=4,sort_keys=False,ensure_ascii=False))

def saveHistory(index):
    f = open('C:\\Users\\DELL\\Desktop\\car300\\data\\readingSave.txt', 'w')
    f.write(str(index))
    f.close()

def updateLabel(car):
    status = 0
    for r in car['records']:
        if status == 0 and r['label'] == 2:
            status = 2
        if r['label'] == 1:
            status = 1
    return status
    
    

if __name__ == "__main__":
    carIndex = 0
    with open(readingSave, 'r') as save:
        carIndex = int(save.read())

    with open(fileName, 'r', encoding = 'utf-8') as file:
        data = json.loads(file.read())

        for i in range(len(data)):
            if(i < carIndex):
                continue
            car = data[i]
            carLabel = car['label']
            carvin = car['vin']
            carIndex = i

            nowRec = 0
            while nowRec < len(car['records']):
                os.system("cls")
                rec = car['records'][nowRec]
                mashineChecked = rec['reason'] is not ' '

                if 'type' == rec['reason'][:4]: # filting marked record
                    nowRec += 1
                    continue
                
                print("Now checking car", i+1, "/", len(data), ":", nowRec+1, "/", len(car['records']))
                print('vin:', carvin)
                print('present car label:', carLabel)
                print('type:', rec['type'])
                print('detail:', rec['detail'])
                print('other:', rec['other'])
                print('label:', rec['label'])
                if mashineChecked: # machine checked
                    print('reason by machine:', rec['reason'])
                    

                print('your input:', end='')
                label = input()
                if label in ['1', '2', '', '0']: # 1 = accident, 2 = not sure, null = 0 = not accident
                    if mashineChecked: # 被机器检测过的
                        if label != '': # 不跳过
                            rec['label'] = int(label)
                            carLabel = updateLabel(car)
                            rec['reason'] = ' ' # reset reason
                        # else skip
                    else: # human judge
                        if rec['label'] == NOT_MARKED:
                            rec['label'] = 0
                        rec['label'] = int(label) if label is not '' else 0 
                        carLabel = updateLabel(car)



                elif label == 'r': # turn to prev rec
                    nowRec -= 1
                    while nowRec >= -1 and car['records'][nowRec]['reason'][:4] == 'type':
                        nowRec -= 1
                    if nowRec != -1:
                        nowRec -= 1

                elif label == 'exit': # exit the checker
                    saveHistory(carIndex)
                    exit()

                else: 
                    nowRec -= 1 # recheck this record

                    
                nowRec += 1

            car['label'] = carLabel
            saveJson(data)
            saveHistory(carIndex)
            




