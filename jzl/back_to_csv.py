# -*- coding:utf-8 -*-
# Author: owhileo sevenaddsix
# Date: 2019-8-7
# Version: 1.0

import json,sys
import pandas as pd

jfilename='C:\\Users\\DELL\\Desktop\\car300\\che300\\car300\\data_2.json'



def read_json(path):
    with open(path, 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False, indent=4)



def go_back(jdata,cdata):

    if len(jdata)!=len(cdata):
        print('wrong size')
        return None
    for ix,x in enumerate(jdata):
        carinfo = cdata.loc[ix]
        #print(carinfo)

        records = json.loads(carinfo['callback_content'])#最后赋值回去
        temp=[]
        # print(vin, lable, records)
        for jrec in x['records']:
            temp.append(jrec['label'])

        for k,kx in enumerate(records['result']):
            kx['label']=temp[k]

        jsoninfo = json.dumps(records, ensure_ascii=False)
        cdata.loc[ix,'callback_content']=jsoninfo

        cdata.loc[ix,'label']=x['label']
        #print(cdata.loc[ix])

    print(cdata)
    return cdata


if __name__ == '__main__':

    jdat = read_json(jfilename)
    cdat = pd.read_csv('C:\\Users\\DELL\\Desktop\\car300\\data\\data2.csv', encoding='utf-8')
    cdata=go_back(jdat,cdat)
    cdata.to_csv('C:\\Users\\DELL\\Desktop\\car300\\data\\data2_new.csv')
