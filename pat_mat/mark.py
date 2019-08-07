# -*- coding:utf-8 -*-
# Author: owhileo sevenaddsix
# Date: 2019-8-7
# Version: 1.0

import json

filename="data3_new.json"

def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False, indent=4)


def mark(data):
    for x in data:
        for y in x['records']:
            if y['label']==9:
                print("type:"+y["type"])
                print("detail:"+y["detail"])
                print("other"+y["other"])
                if mylabel=="":
                    mylabel=0
                mylabel=int(input())
                if(mylabel<0 or mylabel >2):
                    print("wrong label, this record passed")
                else:
                    y['label']=mylabel
                    save_json(filename, data)
                    print("label "+str(mylabel)+" success.")

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
    dat = read_json(filename)
    mark(dat)