# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-7
# Version: 1.7

import json

origin_json_path = 'data4.json'
save_json_path = "data4.json"
type_delete_path = 'types_delete.txt'


def test(s, ss):
    high1 = ["纵梁", "车顶", "避震器", "防火墙", "A柱", "B柱", "C柱", "气囊", "备胎室", "泡水", "火烧", "水泡", "翼子板", "后叶", '叶子板', '前柱',
             '后柱', '梁头', '气帘', '焊', '切', '大梁', '加强件', '后侧围件', '中立柱', 'D柱', '校','减震器','钣金']
    for x in high1:
        if s != None:
            if x in s:
                return True
        if ss != None:
            if x in ss:
                return True
    return False


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
                       '首保工时', '更换曲轴前油封', '按10000公里规范常规保养;', '换机油机滤;', '清洗空调系统', '更换机滤、机油;', '更换灯泡', '水箱漏水']

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
    li = ["召回", '软件升级']

    for x in data:
        for y in x['records']:
            if y['type'] != None:
                for z in li:
                    if z in y['type'] and y['label'] == 9:
                        y['label'] = 0
                        y['reason'] = "recall_filter" + z

                        print('recall_filter find:' + y['type'] + ' and label it:' + '0')
            # if y['detail'] != None:
            #     for z in li:
            #         if z in y['detail'] and y['label'] == 9:
            #             y['label'] = 0
            #             y['reason'] = "recall_filter"+z
            #             print('recall_filter find:' + y['detail'] + ' and label it:' + '0')
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
    new_type_delete = ['更换机油机滤', '更换机油、机滤']
    for x in data:
        for y in x['records']:
            if y['type'] != None and y['label'] == 9:
                for z in new_type_delete:
                    if z in y['type'] and len(y['type']) <= 15:
                        y['label'] = 0
                        y['reason'] = '模糊 new_type过滤:' + z
                        print('self added type_filter fussy match find:' + z + ' and label it:' + '0')
    return data


def fussy_detail_match_filter(data):
    new_type_delete = ['公里规范常规保养;', "公里保养;", "首次保养;", "KM保养", '00公里', '间隔保养', '更换火花塞', '更换制动液', '更换机滤',
                       '更换油水分离器','免费检测','更换空气格','00保养','更换蓄电池','更换天窗','免检','更换机油','更换空调','电瓶更换','完工检测',
                       '更换水箱','冷却器更换','完工检查','换机油','四轮定位','更换左侧转向节臂','更换右侧转向节臂','免费保养','常规保养','储物盒更换',
                       '碳罐更换','更换灯光','更换转向轴承','更换制动液','更换压缩机']

    for x in data:
        for y in x['records']:
            if y['detail'] != None and not test(y['detail'], y['other']) and y['label'] == 9:

                for z in new_type_delete:
                    if z in y['detail'] and len(y['detail']) <= 40:
                        y['label'] = 0
                        y['reason'] = '模糊 new_detail过滤:' + z
                        print('self added detail_filter fussy match find:' + y['detail'] + ' and label it:' + '0')
    return data


def suopei_len_filter(data):
    new_type_delete = ['普通索赔', '索赔']

    for x in data:
        for y in x['records']:
            if y['type'] != None and y['detail'] != None:
                if y['type'] in new_type_delete and len(y['detail']) <= 30 and y['label'] == 9:
                    y['label'] = 0
                    y['reason'] = '索赔 过滤:' + y['detail']
                    print('索赔_filter fussy match find:' + y['detail'] + ' and label it:' + '0')
    return data


def type_detail_filter(data):
    type_list = ['其他', '其它', '-', '无', '保养', '.', '客户自费', '内部结算']
    detail_delete = ['定期保养', '冬季保养', '免费检测', '免费检查', '冬季检查', '春季保养', '春季检查', '保养标准范围', '标准保养范围', '标准保养', '秋季保养',
                     '秋季免检', '发动机油保养', '发动机保养', '免费的移交检查', '机油保养', '润滑保养', '保养套餐', '保养项目', '夏季关怀', '春季关怀', '秋季关怀',
                     '冬季关怀', '真情关怀']
    for x in data:
        for y in x['records']:
            if y['type'] in type_list and y['label'] == 9:
                for z in detail_delete:
                    if y['detail'] != None and y['detail'].find(z) != -1:
                        y['label'] = 0
                        y['reason'] = 'type:' + y['type'] + ' 模糊detail过滤' + z
                        print(y['type'], ' 模糊detail ', z)
                        continue
    return data


def shigu_filter(data):
    li = ["后叶拆装"]
    for x in data:
        for y in x['records']:
            if y['type'] != None:
                for z in li:
                    if z in y['type'] and y['label'] == 9:
                        y['label'] = 1
                        y['reason'] = "shigu:" + z
                        print('shigu_filter find:' + y['type'] + ' and label it:' + '1')
            if y['detail'] != None:
                for z in li:
                    if z in y['detail'] and y['label'] == 9:
                        y['label'] = 1
                        y['reason'] = "shigu:" + z
                        print('shigu_filter find:' + y['detail'] + ' and label it:' + '1')
    return data


def shigu_filter(data):
    li = ["后叶拆装", '修复A柱','修复B柱','修复C柱','B柱钣金','C柱钣金','A柱钣金']
    for x in data:
        for y in x['records']:
            if y['type'] != None:
                for z in li:
                    if z in y['type'] and y['label'] == 9:
                        y['label'] = 1
                        y['reason'] = "shigu:" + z
                        print('shigu_filter find:' + y['type'] + ' and label it:' + '1')
            if y['detail'] != None:
                for z in li:
                    if z in y['detail'] and y['label'] == 9:
                        y['label'] = 1
                        y['reason'] = "shigu:" + z
                        print('shigu_filter find:' + y['detail'] + ' and label it:' + '1')
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


def type_detail_length_filter(data):
    type_list = ['其他', '-', '无', '保养', '.']
    for x in data:
        for y in x['records']:
            if y['label'] == 9 and y['type'] in type_list and len(y['detail']) < 20 and len(y['other']) < 20:
                y['label'] = 0
                y['reason'] = 'type:' + y['type'] + ' 长度过短'
                print(y['type'], ' length too short ')
                continue
    return data


filters = [type_filter, short_filter, type_filter_new1, recall_filter, fussy_match_filter, fussy_detail_match_filter,
           type_detail_filter, suopei_len_filter, shigu_filter, type_detail_length_filter]

if __name__ == '__main__':
    dat = read_json(origin_json_path)
    for i in filters:
        dat = i(dat)
    dat = auto_vin_label_check(dat)
    save_json(save_json_path, dat)
