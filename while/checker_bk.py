# version 2.0
# date 8.9
# time 10:36

import json, os
import platform

fileName = r"data4.json"
readingSave = r"readingSave.txt"
NOT_MARKED = 9

high_stru = ["纵梁","边梁","梁头","大梁","纵粱","边粱","粱头","大粱","减振器座", "避振器座",  "避震器座", "减震器座","防火墙", "A柱", "B柱", "C柱", "D柱","车顶侧围","车门柱","柱","前轮旋"]
high_enha=["车顶","顶棚","大顶","后叶","后翼","下边梁","下坎","下槛","下砍","下裙","大边","后翅","横梁","后围","后围板","后尾板","后侧围件","框架"]
high_spec=["气囊","发动机"]
high_wate=["进水","排水","污泥","水渍","淤泥","泥沙"]
high_verb=["切","割","焊","焊接","更换"]

__while__=True
if __while__:
    import jieba
    jieba.load_userdict("d:/NJU/che300/car300/while/car_parts_all.txt")

def saveJson(data):
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False))


def saveHistory(index):
    f = open('readingSave.txt', 'w')
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

    with open(fileName, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())

        for i in range(len(data)):
            if (i < carIndex):
                continue
            car = data[i]
            carLabel = updateLabel(car)
            carvin = car['vin']
            carIndex = i

            nowRec = 0
            while nowRec < len(car['records']):
                if(platform.platform()[0]=="L"):
                    os.system("clear")
                elif(platform.platform()[0]=="W"):
                    os.system("cls")
                else:
                    print("unknown os!")
                rec = car['records'][nowRec]
                mashineChecked = rec['reason'] is not ' '

                # if 'type' == rec['reason'][:4]:  # filting marked record
                if ' ' != rec['reason']:
                    nowRec += 1
                    continue

                det = "|".join(jieba.cut(rec['detail']))
                oth = "|".join(jieba.cut(rec['other']))

                # 结构件：红色
                # 加强件：黄色
                # 气囊、发动机：绿色
                # 进水：蓝色
                # 动词：紫色
                for k in high_stru:
                    det = det.replace(k, '\033[1;31;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;31;40m' + k + '\033[0m')
                for k in high_enha:
                    det = det.replace(k, '\033[1;33;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;33;40m' + k + '\033[0m')
                for k in high_spec:
                    det = det.replace(k, '\033[1;32;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;32;40m' + k + '\033[0m')
                for k in high_wate:
                    det = det.replace(k, '\033[1;34;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;34;40m' + k + '\033[0m')
                for k in high_verb:
                    det = det.replace(k, '\033[1;35;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;35;40m' + k + '\033[0m')

                print("Now checking car", i + 1, "/", len(data), ":", nowRec + 1, "/", len(car['records']))
                print('vin:', carvin)
                print('present car label:', carLabel)
                print('type:', rec['type'])
                print('detail:', det)
                print('other:', oth)
                print('label:', rec['label'])
                if mashineChecked:  # machine checked
                    print('reason by machine:', rec['reason'])

                print('your input:', end='')
                label = input()
                if label in ['1', '2', '', '0']:  # 1 = accident, 2 = not sure, null = 0 = not accident
                    if mashineChecked:  # 被机器检测过的
                        if label != '':  # 不跳过
                            rec['label'] = int(label)
                            carLabel = updateLabel(car)
                            rec['reason'] = ' '  # reset reason
                        # else skip
                    else:  # human judge
                        if rec['label'] == NOT_MARKED:
                            rec['label'] = 0
                        if label != '':
                            rec['label'] = int(label)
                        carLabel = updateLabel(car)



                elif label == 'r':  # turn to prev rec
                    nowRec -= 1
                    while nowRec >= -1 and car['records'][nowRec]['reason'] != ' ':
                        nowRec -= 1
                    if nowRec != -1:
                        nowRec -= 1

                elif label == 'exit':  # exit the checker
                    saveHistory(carIndex)
                    exit()

                else:
                    nowRec -= 1  # recheck this record

                nowRec += 1

            car['label'] = carLabel
            saveJson(data)
            saveHistory(carIndex)
