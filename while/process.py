# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-7
# Version: 1.3

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
            if y['detail'] in type_drop and y['label'] == 9:
                y['label'] = 0
                y['reason'] = 'detail过滤i:' + y['detail']
                print('detail_filter find:' + y['detail'] + ' and label it:' + '0')
    return data


def type_filter_new1(data):
    new_type_delete = ['一般:客户付款', "喷漆:客户付款", "服务节免费检查", "召回活动", "召回行动", '小修', '更换机油机滤', '更换机油机油格', '换机油', '换机油机滤',
                       '首保工时', '更换曲轴前油封', '按10000公里规范常规保养;', '换机油机滤;', '清洗空调系统']
    for x in data:
        for y in x['records']:
            if y['type'] in new_type_delete and y['label'] == 9:
                y['label'] = 0
                y['reason'] = 'new_type过滤:' + y['type']
                print('self added type_filter find:' + y['type'] + ' and label it:' + '0')
            if y['detail'] in new_type_delete and y['label'] == 9:
                y['label'] = 0
                y['reason'] = 'new_detail过滤:' + y['detail']
                print('self added type_filter find in detail:' + y['detail'] + ' and label it:' + '0')
    return data


def recall_filter(data):
    for x in data:
        for y in x['records']:
            if y['type'] != None:
                if "召回" in y['type'] and y['label'] == 9:
                    y['label'] = 0
                    y['reason'] = '召回活动'
                    print('recall_filter find:' + y['type'] + ' and label it:' + '0')
    return data


def short_filter(data):
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


def fussy_match_filter(data):
    new_type_delete = ['更换机油机滤']
    for x in data:
        for y in x['records']:
            if y['type'] != None and y['label'] == 9:
                for z in new_type_delete:
                    if z in y['type'] and len(y['type']) <= 10:
                        y['label'] = 0
                        y['reason'] = '模糊 new_type过滤:' + y['type']
                        print('self added type_filter fussy match find:' + z + ' and label it:' + '0')
    return data


def fussy_detail_match_filter(data):
    new_type_delete = ['公里规范常规保养;', "公里保养;"]
    for x in data:
        for y in x['records']:
            if y['detail'] != None and y['label'] == 9:
                for z in new_type_delete:
                    if z in y['detail'] and len(y['detail']) <= 27:
                        y['label'] = 0
                        y['reason'] = '模糊 new_detail过滤:' + y['type']
                        print('self added detail_filter fussy match find:' + z + ' and label it:' + '0')
    return data


def type_detail_filter(data):
    type_list = ['其他', '-', '无', '保养']
    detail_delete = ['定期保养', '冬季保养', '免费检测', '免费检查', '冬季检查', '春季保养', '春季检查', '保养标准范围', '标准保养', '秋季保养',
                     '秋季免检', '发动机油保养']
    for x in data:
        for y in x['records']:
            if y['type'] in type_list and y['label'] == 9:
                for z in detail_delete:
                    if y['detail'].find(z) != -1:
                        y['label'] = 0
                        y['reason'] = 'type:' + y['type'] + ' 模糊detail过滤' + z
                        print(y['type'], ' 模糊detail ', z)
                        continue
    return data


def auto_vin_label_check(data):
    for x in data:
        finished = True
        label = 0
        for y in x['records']:
            if y['label'] == 2 and label == 0:
                label = 2
            if y['label'] == 1:
                label = 1
            if y['label'] == 9:
                finished = False
                break
        if x['label'] != label and finished:
            x['label'] = label
            print('auto_check find an vin label error')
    return data


filters = [type_filter, short_filter, type_filter_new1, recall_filter, fussy_match_filter, fussy_detail_match_filter,
           type_detail_filter]

if __name__ == '__main__':
    dat = read_json(origin_json_path)
    for i in filters:
        dat = i(dat)
    dat = auto_vin_label_check(dat)
    save_json(save_json_path, dat)
