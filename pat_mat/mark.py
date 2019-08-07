# -*- coding:utf-8 -*-
# Author: owhileo sevenaddsix
# Date: 2019-8-7
# Version: 1.0

import json,sys

filename="data3.json"

high1=["纵梁","车顶","避震器","防火墙","A柱","B柱","C柱","气囊","备胎室","泡水","火烧","水泡","翼子板","后叶"]
#high2=["切割","钣金","焊接",]

def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False, indent=4)


def mark(data):
    for ix,x in enumerate(data):
        for iy,y in enumerate(x['records']):
            if y['label']==9:
                print(str(iy+1)+"/"+str(len(x['records']))+"   "+str(ix+1)+"/"+str(len(data)))
                print("type:"+y["type"])
                det=y["detail"]
                oth=y["other"]
                for k in high1:
                    det=det.replace(k,'\033[1;32;40m'+k+'\033[0m')
                    oth=oth.replace(k,'\033[1;32;40m'+k+'\033[0m')
                print("detail:"+det)
                print("other:"+oth)
                mylabel=input()
                if mylabel=="":
                    mylabel=0
                elif mylabel=="exit":
                    save_json(filename, data)
                    exit()
                mylabel=int(mylabel)
                if(mylabel<0 or mylabel >2):
                    print("wrong label, this record passed")
                else:
                    y['label']=mylabel
                    print("label "+str(mylabel)+" success.")
                    print("")

    # #sum_s = 0
    # #labeled = 0
    # #auto_labeled = 0
    # for x in data:
    #     for y in x['records']:
    #         sum_s += 1
    #         if y['label'] == 0 or y['label'] == 1:
    #             labeled += 1
    #             if y['reason'] != ' ':
    #                 auto_labeled += 1
    # print("totoal records:{}".format(sum_s))
    # print("labeled records:(include auto_labeled records){},{:.2f}%".format(labeled, labeled / sum_s * 100))
    # print("auto_labeled records:{},{:.2f}%".format(auto_labeled, auto_labeled / sum_s * 100))
    # return data


if __name__ == '__main__':
    if(sys.version[0]!="3"):
        print("use python3 pls!")
        exit()
    dat = read_json(filename)
    mark(dat)
