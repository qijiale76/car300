import json, os

fileName = "data0.json"
readingSave = "readingSave.txt"
NOT_MARKED = 9

def saveJson(data):
    with open(fileName, 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(data,indent=4,sort_keys=False,ensure_ascii=False))

def updateLabel(new, ori):
    if ori == 0: return new
    elif ori == 2 and new > 0: return new
    else: return 1
    

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
            carIndex = i

            nowRec = 0
            while nowRec < len(car['records']):
                os.system("cls")
                rec = car['records'][nowRec]
                
                if rec['label'] is not NOT_MARKED: # filting marked record
                    nowRec += 1
                    continue
                
                print("Now checking car", i, ":", nowRec, "/", len(car['records']))
                print('type:', rec['type'])
                print('detail:', rec['detail'])
                print('other:', rec['other'])

                label = input()
                if label in ['1', '2', '']: # 1 = accident, 2 = not sure, null = 0 = not accident         
                    label = int(label) if label is not '' else 0
                    rec['lebel'] = label
                    carLabel = updateLabel(label, carLabel)

                elif label == 'r': # turn to prev rec
                    nowRec -= 2
                    if nowRec < -1: 
                        nowRec = -1

                elif label == 'exit': # exit the checker
                    f = open('readingSave.txt', 'w')
                    f.write(str(carIndex))
                    f.close()
                    exit()

                nowRec += 1

            car['label'] = carLabel
            saveJson(data)
            




