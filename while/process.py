# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-6
# Version: 1.0

import json


def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)


# 过滤器从这里开始,写好函数后加入最后filters的list中
# 输入为data,整个json文件，为dict的list,每个dict的'records'字段又为一个dict的list
# 最后返回修改过的data
def type_filter(data):
    with open(r'types_delete.txt', 'r') as f:
        type_drop = [x[:-1] for x in f.readlines()]  # 可能是linux特性？直接读每行末尾有\n,故虑去最后一个字符
    for x in data:
        for y in x['records']:
            if y['type'] in type_drop and y['label'] != 0:
                y['label'] = 0
                y['reason'] = 'type过滤:' + y['type']
                print('type_filter find:' + y['type'] + ' and label it:' + '0')
    return data


filters = [type_filter]

if __name__ == '__main__':
    dat = read_json(r'data4.json')
    for i in filters:
        dat = i(dat)
    save_json(r'data4_new.json', dat)
