# -*- coding:utf-8 -*-
# Author: owhileo sevenaddsix
# Date: 2019-8-7
# Version: 1.0

import json,sys

filename='C:\\Users\\DELL\\Desktop\\car300\\che300\\car300\\data_2.json'
newfilename='C:\\Users\\DELL\\Desktop\\car300\\data\\data_2_with_2.json'


def read_json(path):
    with open(path, 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False, indent=4)


data_with_2={}

def pick_2(data):
    for ix,x in enumerate(data):
        is_2=False
        for iy,y in enumerate(x['records']):
            if y['label']==2:
                is_2=True
                break
        if is_2:
            data_with_2[ix]=x
    save_json(newfilename, data_with_2)



if __name__ == '__main__':
    if(sys.version[0]!="3"):
        print("use python3 pls!")
        exit()
    dat = read_json(filename)
    pick_2(dat)
