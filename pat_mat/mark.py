# -*- coding:utf-8 -*-
# Author: owhileo sevenaddsix
# Date: 2019-8-7
# Version: 1.0

import json,sys

filename='C:\\Users\\DELL\\Desktop\\car300\\che300\\car300\\data_2.json'

#high1=["纵梁","车顶","避震器","防火墙","A柱","B柱","C柱","气囊","备胎室","泡水","火烧","水泡","翼子板","后叶",'叶子板','前柱',
#       '后柱','梁头','气帘','焊','切','大梁','加强件','后侧围件','中立柱','D柱','拆装','更换','校', "车顶", "避震器",'减震器','钣金','后围']

high_stru = ['纵梁', '梁头', '大梁', '纵粱', '边粱', '粱头', '大粱', '前梁', '前粱', '防火墙', 'A柱', 'B柱', 'C柱', 'D柱', '车顶侧围', '车门柱', '柱',
             '前轮旋', '牛腿',
             '避震座', '避震包', '避震器座', '避震壳体', '避震大包',
             '避振座', '避振包', '避振器座', '避振壳体', '避振大包',
             '减震座', '减震包', '减震器座', '减震壳体', '减震大包',
             '减振座', '减振包', '减振器座', '减振壳体', '减振大包']
high_enha = ['边梁', '车顶', '大顶', '后叶', '后翼', '下边梁', '下坎', '下槛', '下砍', '下裙', '大边', '后翅', '后围', '后围板', '后尾板', '后侧围件', '框架',
             '灯座', '后幅', '后墙','翼子板','叶子板']

high_spec = ['气囊', '发动机', '气帘','气枕']
high_wate = ['进水', '排水', '污泥', '水渍', '淤泥', '泥沙', '车辆涉水', '水淹车', '水浸车', '水淹事故', '水淹', '涉水车', '泡水车', '进水车', '车辆泡水']
high_verb = ['焊接', '更换', '更新', '换', '切', '割', '焊']



def read_json(path):
    with open(path, 'r',encoding='utf-8') as f:
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

                for k in high_stru:
                    det = det.replace(k, '\033[1;31;48m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;31;48m' + k + '\033[0m')
                for k in high_enha:
                    det = det.replace(k, '\033[1;33;48m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;33;48m' + k + '\033[0m')
                for k in high_spec:
                    det = det.replace(k, '\033[1;32;48m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;32;48m' + k + '\033[0m')
                for k in high_wate:
                    det = det.replace(k, '\033[1;44;48m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;44;48m' + k + '\033[0m')
                for k in high_verb:
                    det = det.replace(k, '\033[1;35;48m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;35;48m' + k + '\033[0m')

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
