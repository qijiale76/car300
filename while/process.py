# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-6
# Version: 1.0

import json

origin_json_path = r'data4.json'
save_json_path = r'data4.json'
type_delete_path = r'types_delete.txt'


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False, indent=4)


# 过滤器从这里开始,写好函数后加入最后filters的list中
# 输入为data,整个json文件，为dict的list,每个dict的'records'字段又为一个dict的list
# 最后返回修改过的data
# 写规则的时候记得加一条 y['label'] == 9 对未标定的应用这条 ***
def type_filter(data):
    with open(type_delete_path, 'r', encoding='utf-8') as f:
        type_drop = [x[:-1] for x in f.readlines()]  # 可能是linux特性？直接读每行末尾有\n,故虑去最后一个字符
    for x in data:
        for y in x['records']:
            if y['type'] in type_drop and y['label'] == 9:
                y['label'] = 0
                y['reason'] = 'type过滤:' + y['type']
                print('type_filter find:' + y['type'] + ' and label it:' + '0')
    return data


def type_filter_new1(data):
    new_type_delete = ['一般:客户付款', "喷漆:客户付款", "服务节免费检查", "召回活动", "召回行动"]
    for x in data:
        for y in x['records']:
            if y['type'] in new_type_delete and y['label'] == 9:
                y['label'] = 0
                y['reason'] = 'new_type过滤:' + y['type']
                print('self added type_filter find:' + y['type'] + ' and label it:' + '0')
    return data


def recall_filter(data):
    for x in data:
        for y in x['records']:
            if "召回" in y['type'] and y['label'] == 9:
                y['label'] = 0
                y['reason'] = '召回活动'
                print('recall_filter find:' + y['type'] + ' and label it:' + '0')
    return data


def short_filter(data):
    # with open(r'E:\CS\Git_repo\car300\types_delete.txt', 'r', encoding='utf-8') as f:
    #     type_drop = [x[:-1] for x in f.readlines()]  # 可能是linux特性？直接读每行末尾有\n,故虑去最后一个字符
    for x in data:
        for y in x['records']:
            if y['detail'] == None:
                a = 0
            else:
                a = len(y['detail'])
            if y['other'] == None:
                b = 0
            else:
                b = len(y['other'])
            if a + b < 15 and y['label'] == 9:
                y['label'] = 0
                y['reason'] = 'detail和other内容少于15字过滤'
                print('short_filter find:' + ' and label it:' + '0')
    return data


filters = [type_filter, short_filter, type_filter_new1]

if __name__ == '__main__':
    dat = read_json(origin_json_path)
    for i in filters:
        dat = i(dat)
    save_json(save_json_path, dat)
