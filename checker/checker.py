import json, os

fileName = "data0.json"
readingSave = "readingSave.txt"
NOT_MARKED = 9

def saveJson(data):
    with open(fileName, 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(data,indent=4,sort_keys=False,ensure_ascii=False))

def saveHistory(index):
    f = open('readingSave.txt', 'w')
    f.write(str(index))
    f.close()

def updateLabel(new, ori):
    if ori == 0: 
        return new
    elif ori == 2: 
        if new == 0: 
            return ori
        else:
            return new
    elif ori == 1: return 1
    

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
                if mashineChecked: # machine checked
                    print('reason by machine:', rec['reason'])
                    print('label by machine:', rec['label'])

                print('your input:', end='')
                label = input()
                if label in ['1', '2', '', '0']: # 1 = accident, 2 = not sure, null = 0 = not accident
                    label = int(label) if label is not '' else 0

                    if mashineChecked:      
                        if label != '': # forced changing machine result
                            rec['label'] = label
                            carLabel = label
                            rec['reason'] = ' ' # reset reason
                        # else skip
                    else: # human judge
                        carLabel = updateLabel(label, carLabel) if rec['label'] is NOT_MARKED else label
                        rec['label'] = label

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
            




