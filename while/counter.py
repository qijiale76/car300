# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-6
# Version: 1.0

import json


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def count(data):
    summ = 0
    labeled = 0
    auto_labeled = 0
    for x in data:
        for y in x['records']:
            summ += 1
            if y['label'] == 0 or y['label'] == 1:
                labeled += 1
                if y['reason'] != ' ':
                    auto_labeled += 1
    print("totoal records:{}".format(summ))
    print("labeled records:(include auto_labeled records){},{:.2f}%".format(labeled, labeled / summ * 100))
    print("auto_labeled records:{},{:.2f}%".format(auto_labeled, auto_labeled / summ * 100))
    return data


if __name__ == '__main__':
    dat = read_json(r'data4.json')
    count(dat)
