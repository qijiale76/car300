import pandas as pd
import json
import re
import sys

if int(sys.argv[1])<0 or int(sys.argv[1])>=5:
    print("wrong input")
    exit()

# newTable = pd.DataFrame(columns=["type","detail","other","lable","newlable","vin"])
data = pd.read_csv(
    "../../pat_mat/data/data"+sys.argv[1]+".csv", encoding='utf-8')
infos = []

# types_delete=[]
# with open("E:\\CS\\internship\\types_delete.txt",'r' ,encoding='utf-8') as ft:
#     for l in ft:
#         types_delete.append(l)

for i in range(len(data)):
    try:
        newinfo = {}
        carinfo = data.loc[i]
        newinfo['vin'] = str(carinfo['vin'])

        records = json.loads(carinfo['callback_content'])
        #print(vin, lable, records)
        newinfo['records'] = []
        for rec in records['result']:
            # print(rec)
            temp = {}
            temp['type'] = rec['type']
            temp['detail'] = rec['detail']
            temp['other'] = re.sub(r"[0-9a-zA-Z\- \*]+;", "", rec['other'])
            temp['label']=9
            temp['reason'] = ' '
            # if rec['type'] in types_delete:
            #     temp['label']=0
            newinfo['records'].append(temp)
            # newTable.loc[len(newTable)] = [rec['type'],rec['detail'],rec['other'],'','','']

        # newinfo['label'] = int(carinfo['label'])
        newinfo['label'] = 0

        jsoninfo = json.dumps(newinfo,ensure_ascii=False)
        # jsoninfo=str(newinfo)
        infos.append(jsoninfo)
    except :
        print("wrong!!! no: ",i,'\n')

with open("../../pat_mat/temp/temp"+sys.argv[1]+".json", 'w', encoding='utf-8') as fout:
    fout.write('[\n')
    for i in infos[:-1]:
        i+=',\n'
        fout.write(i)
    fout.write(infos[-1]+'\n')
    fout.write(']')
