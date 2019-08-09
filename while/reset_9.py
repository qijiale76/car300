import json

origin_json_path = 'data4.json'
save_json_path = "data4.json"


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False, indent=4)


high_stru = ["纵梁", "边梁", "梁头", "大梁", "纵粱", "边粱", "粱头", "大粱", "减振器座", "避振器座", "避震器座", "减震器座", "防火墙", "A柱", "B柱", "C柱",
             "D柱", "车顶侧围", "车门柱", "柱", "前轮旋"]
high_enha = ["车顶", "顶棚", "大顶", "后叶", "后翼", "下边梁", "下坎", "下槛", "下砍", "下裙", "大边", "后翅", "横梁", "后围", "后围板", "后尾板", "后侧围件",
             "框架"]
high_spec = ["气囊", "发动机"]
high_wate = ["进水", "排水", "污泥", "水渍", "淤泥", "泥沙"]
total = high_enha + high_spec + high_stru + high_wate

if __name__ == '__main__':
    dat = read_json(origin_json_path)
    for x in dat:
        for y in x['records']:
            if y['label'] == 0 or y['label'] == 2:
                for xx in total:
                    if xx in y['detail'] or xx in y['other']:
                        y['label'] = 9
                        y['reason'] = ' '
                        print('reset label as 9')
                        continue
    save_json(save_json_path, dat)
