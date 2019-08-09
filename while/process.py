# -*- coding:utf-8 -*-
# Author: owhileo
# Date: 2019-8-7
# Version: 2.0

import json

origin_json_path = 'C:\\Users\\DELL\\Desktop\\car300\\data\\data_2.json'
save_json_path = 'C:\\Users\\DELL\\Desktop\\car300\\data\\data_2.json'
type_delete_path = 'C:\\Users\\DELL\\Desktop\\car300\\data\\types_delete.txt'



key_v = ['更换', '维修', '修复', '修理', '校正', '变形', '矫正', '校修', '校', '修', '整形', '焊接', '切割',
         '整漆', '更新', '换', '焊割', '钣金', '拆装']
key_n = ['大梁', '左前大梁', '后大梁', '右大梁', '前梁', '左前梁', '前大梁', '右前大梁', '两前大梁', '纵梁',
         '左前纵梁', '右前纵梁', '左右纵梁', '左右前纵梁', '前纵梁', '后纵梁', '减震包', '减震大包', '避震壳体',
         '避震座', '牛腿', '减震腿', '防火墙', '前防撞梁', '悬挂系统', 'a柱', '右前柱', 'b柱', 'c柱', '中柱',
         '右中柱', '左A柱', '左b柱', '左侧a柱', '左侧中柱', '右侧中柱', '左侧b柱', '左侧c柱', '右侧a柱',
         '右侧a柱', '右侧c柱', '右a柱', '左前a柱', '右前a柱', '中立柱', '中柱']  # 左后叶可能有点问题
key_n_434 = ['大梁', '左前大梁', '后大梁', '右大梁', '前梁', '左前梁', '右前梁头', '梁头', '左梁头', '右梁头',
             '左右梁头', '前大梁', '右前大梁', '两前大梁', '纵梁', '左前纵梁', '右前纵梁', '左右纵梁', '左右前纵梁',
             '前纵梁', '后纵梁', '减震包', '减震大包', '避震壳体', '避震座', '牛腿', '减震腿', '防火墙', '前防撞梁',
             '悬挂系统']
sentences = ['更换后围板', '更换后尾板', '更换后侧围', '更换左侧侧围', '更换后翼子板', '后围更换', '换后翼子板',
             '更新后围板', '更新尾板', '更新后围', '前叶加强板更换', '焊接后围', '焊割左后叶', '切焊后围板',
             '侧围焊接', '侧围更换', '切割后围', '切割后翼子板']
houwei = ['后围', '后围板', '后侧围', '后翼子板', '后翼', '车顶', '侧围', '侧围板']
shuiyan = ['车辆涉水', '水淹车', '水浸车', '水淹事故', '水淹', '涉水车', '泡水车', '进水车', '车辆泡水']
quansun = ['全损车']
first2 = ['水箱框架', '后围', '散热器', '翼子板', '前翼子板', '后翼子板', '保险扛', '挡风玻璃', '后减震器',
          '减震包', '发动机', '仪表台', '门', '散热器', '行李箱', '仪表板', '变速器']
maybe2 = ['纵梁端板', '纵梁', 'a柱', 'b柱', 'c柱', '右前大梁', '大梁', '车顶纵梁', '前纵梁', '立柱',
          '中柱', '右中柱', '梁头']
first3 = ['水箱框架', '后围', '散热器', '翼子板', '前翼子板', '后翼子板', '保险杠', '挡风玻璃', '减震器',
          '发动机', '仪表台', '门', '散热器', '行李箱', '仪表板', '变速器', '减震']
maybe3 = ['气囊', '气囊控制单元', '气囊传感器']
first4 = ['水箱框架', '散热器', '冷凝器', '保险杠', '发动机', '仪表台', '门', '散热器', '行李箱',
          '行李箱盖', '风挡玻璃', '右后门', '安全带', '座椅', '减震', '下裙边', '后梁', '底板', '减震支柱']
maybe4 = ['后围', '后围板', '侧围', '侧围板', '左侧围', '右侧围', '后侧围', '后翼子板']



def test(s, ss):
    high1 = ["纵梁", "车顶", "避震器", "防火墙", "A柱", "B柱", "C柱", "气囊", "备胎室", "泡水", "火烧", "水泡", "翼子板", "后叶", '叶子板', '前柱',
             '后柱', '梁头', '气帘', '焊', '切', '大梁', '加强件', '后侧围件', '中立柱', 'D柱', '校', '减震器', '梁', '柱', '叶', '翼', '粱', '减振器','后围'
             ,'切割','翅','车顶','全损','事故','上边梁','气囊','纵','拆装','火烧','水泡','后围', '后围板', '侧围', '侧围板', '左侧围', '右侧围', '后侧围', '后翼子板'
             ,'气囊', '气囊控制单元', '气囊传感器','气','涉水', '水淹', '水浸', '水淹', '涉水车', '泡水车', '进水车', '车辆泡水','全损车','围','废','门'
             ,'分解','烘','发动机','事故','钣','拆','卸','修']



    rep = ['翼子板(喷漆)','钣金:客户付款;','前叶','前翼']
    a = s
    b = ss
    for x in rep:
        if a != None:
            a = a.replace(x, '')
        if b != None:
            b = b.replace(x, '')
    for x in high1:
        if a != None:
            if x in a:
                return True
        if b != None:
            if x in b:
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
                       '首保工时', '更换曲轴前油封', '按10000公里规范常规保养;', '换机油机滤;', '清洗空调系统', '更换机滤、机油;', '更换灯泡', '水箱漏水',
                       '年审', '附件安装']

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
                       '更换油水分离器', '免费检测', '更换空气格', '00保养', '更换蓄电池', '更换天窗', '免检', '更换机油', '更换空调', '电瓶更换', '完工检测',
                       '更换水箱', '冷却器更换', '完工检查', '换机油', '四轮定位', '更换左侧转向节臂', '更换右侧转向节臂', '免费保养', '常规保养', '储物盒更换',
                       '碳罐更换', '更换灯光', '更换转向轴承', '更换制动液', '更换压缩机', '更换刹车油', '清洗空调', '挡泥板拆卸', 'PDI检测', '汽油添加剂', '匹配钥匙',
                       '火花塞(每只)更换', '空调清洗', '换油保养', '花粉滤清器更换', '更换杂物箱', '添加玻璃水', '更换电瓶', '更换EPS', '更换制动主泵',
                       '更换两侧防尘套', '渗漏检查', '漏油检查', '前风挡玻璃左右外侧胶条', '拆装前杠', '免费检查', '换右后刹车', '换左后刹车', '前保险杠盖拆装',
                       '后保险杠盖拆装', '定期保养', '更换前挡风玻璃', '更换前杠', '前杠油漆', '前杠拆装', '更换后杠', '发动机漏油', '更换前风挡玻璃', '后杠拆装',
                       '后保更换', '后保拆装', '发动机油更换', '更换右后视镜', '更换左后视镜', '更换前挡', '密封条拆装', '滤芯拆装', 'PDS检查', '换前杠','泄露检查']

    for x in data:
        for y in x['records']:
            if y['detail'] != None and not test(y['detail'], y['other']) and y['label'] == 9:

                for z in new_type_delete:
                    if z in y['detail'] and len(y['detail']) <= 67:
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
                     '冬季关怀', '真情关怀','发动机灯报警','发动机报警','机油报警','仪表报警','报警灯亮','车辆测试']

    for x in data:
        for y in x['records']:
            if y['type'] in type_list and y['label'] == 9:
                for z in detail_delete:
                    if y['detail'] != None and y['detail'].find(z) != -1 and not test(y['detail'],y['other']):
                        y['label'] = 0
                        y['reason'] = 'type:' + y['type'] + ' 模糊detail过滤' + z
                        print(y['type'], ' 模糊detail ', z)
                        continue
    return data




def shigu_filter(data):
    li = ["后叶拆装", '修复A柱;', '修复B柱', '修复C柱', 'B柱钣金', 'C柱钣金', 'A柱钣金', 'A柱修复', 'B柱修复', 'C柱修复', ':气囊:', ';气囊;', ';安全气囊;',
          ';气枕;','校修右前大梁','校正大梁','大梁校正']
    for x in data:
        for y in x['records']:
            if y['type'] != None:
                for z in li:
                    if z in y['type'] and y['label'] == 9:
                        y['label'] = 1
                        y['reason'] = "shigu:" + z
                        print('shigu_filter find:' + y['type'] + '||' + y['detail'] + ' and label it:' + '1')
            if y['detail'] != None:
                for z in li:
                    if z in y['detail'] and y['label'] == 9:
                        y['label'] = 1
                        y['reason'] = "shigu:" + z
                        print('shigu_filter find:' + y['type'] + '||' + y['detail'] + ' and label it:' + '1')
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
    return data

def none_keyword_filter(data):
    for x in data:
        for y in x['records']:
            if not test(y['detail'],y['other']) and (len(y['detail'])+len(y['other']))<70 and y['label']==9:
                y['label'] = 0
                y['reason'] = '未找到关键词 and 长度太短'
                print('none keyword found and short, label it 0:'+y['detail']+''+y['other'])
    return data

#备用
def recover(data):
    for x in data:
        for y in x['records']:
           if y['reason']=='未找到关键词 and 长度太短':
                y['label'] = 9
                y['reason'] = ' '
                print('recover')
    return data



filters = [type_filter, short_filter, type_filter_new1, recall_filter, fussy_match_filter,
           suopei_len_filter, shigu_filter, type_detail_length_filter,fussy_detail_match_filter, type_detail_filter,none_keyword_filter]

if __name__ == '__main__':
    dat = read_json(origin_json_path)
    for i in filters:
        dat = i(dat)
    dat = auto_vin_label_check(dat)
    save_json(save_json_path, dat)
