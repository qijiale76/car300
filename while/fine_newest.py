# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-8
# Version: 1.0

import json


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def find_new(data):
    summ = 0
    for x in data:
        label = True
        for y in x['records']:
            if y['label'] == 9:
                label = False
        if not label:
            break
        summ += 1
    print("newest car:{}".format(summ))


if __name__ == '__main__':
    dat = read_json(r'data4.json')
    find_new(dat)
