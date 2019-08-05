#!/usr/bin/python
# coding=utf-8

AUTHOR="齐家乐"

import sys 
import json
import pandas as pd 
import jieba

stopwords_path="stopwords/哈工大停用词表.txt"
if sys.argv[1]=="p":
    filename="positive_500_0802.csv"
    file_to_print_name="positive_print_500.txt"
    print_label=" __label__positeive\n"
elif sys.argv[1]=="n":
    filename="negative_500_0802.csv"
    file_to_print_name="negative_print_500.txt"
    print_label=" __label__nagetive\n"
else:
    print("p for positive, n for negative")

data=pd.read_csv(filename,encoding="gb18030")
file_to_print=[]


#this fuction copy from : https://blog.csdn.net/FontThrone/article/details/72782499
def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read( )
        f_stop_text=unicode(f_stop_text,'utf-8')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)
#copy end

for index, row in data.iterrows():
    string=""
    label=row["label"]
    records=json.loads(row["callback_content"])
    for rec in records["result"]:
        try:
            string=string+rec["type"]+" "+rec["detail"]+" "+rec["other"]+" "
        except:
            print("except")
    string = jiebaclearText(string)
    #seg_list = jieba.cut(string)
    #seg = " ".join(seg_list)
    seg=string+print_label
    file_to_print.append(seg.encode("utf-8"))

for i in file_to_print:
    if type(i)!=str:
        print(i)
        print(type(i))
        break

with open(file_to_print_name,"w") as f:
    f.writelines(file_to_print)