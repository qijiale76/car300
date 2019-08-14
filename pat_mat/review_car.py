import json, os,sys

filename = "data3.json"

high_stru = ['纵梁', '梁头', '大梁', '纵粱', '边粱', '粱头', '大粱', '前梁', '前粱', '防火墙', 'A柱', 'B柱', 'C柱', 'D柱', '车顶侧围', '车门柱', '柱','前轮旋', '牛腿',
             '避震座', '避震包', '避震器座', '避震壳体', '避震大包',
             '避振座', '避振包', '避振器座', '避振壳体', '避振大包',
             '减震座', '减震包', '减震器座', '减震壳体', '减震大包',
             '减振座', '减振包', '减振器座', '减振壳体', '减振大包']
high_enha = ['边梁', '车顶', '大顶', '后叶', '后翼', '下边梁', '下坎', '下槛', '下砍', '下裙', '大边', '后翅', '后围', '后围板', '后尾板', '后侧围件', '框架',
             '灯座', '后幅', '后墙']

high_spec = ['气囊', '发动机', '气帘','气枕']
high_wate = ['进水', '排水', '污泥', '水渍', '淤泥', '泥沙', '车辆涉水', '水淹车', '水浸车', '水淹事故', '水淹', '涉水车', '泡水车', '进水车', '车辆泡水']
high_verb = ['焊接', '更换', '更新', '换', '切', '割', '焊']

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
            goto=True
            if y['label']==0:
                for i in []]:
                    if i in y['detail'] or i in y['other']:
                        goto= False
                        break
                for i in :
                    if i in y['detail'] or i in y['other']:
                        goto= True
                        break
                if goto:
                    break
                print(str(iy+1)+"/"+str(len(x['records']))+"   "+str(ix+1)+"/"+str(len(data)))
                if y['type'] !=None:
                    print("type:"+y["type"])
                det=y["detail"]
                oth=y["other"]
                for k in high_stru:
                    det = det.replace(k, '\033[1;31;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;31;40m' + k + '\033[0m')
                for k in high_enha:
                    det = det.replace(k, '\033[1;33;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;33;40m' + k + '\033[0m')
                for k in high_spec:
                    det = det.replace(k, '\033[1;32;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;32;40m' + k + '\033[0m')
                for k in high_wate:
                    det = det.replace(k, '\033[1;34;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;34;40m' + k + '\033[0m')
                for k in high_verb:
                    det = det.replace(k, '\033[1;35;40m' + k + '\033[0m')
                    oth = oth.replace(k, '\033[1;35;40m' + k + '\033[0m')
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
                os.system("clear")
        save_json(filename, data)


if __name__ == '__main__':
    if(sys.version[0]!="3"):
        print("use python3 pls!")
        exit()
    dat = read_json(filename)
    mark(dat)
