#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import jieba
from torchtext.vocab import FastText
import torch
import numpy as np


# In[32]:


#是否使用gpu
use_cuda=False


# In[33]:


def get_text(x):
    record=x["result"]
    t=''.join([str(i["type"]) for i in record])
    detail=''.join([str(i["detail"]) for i in record])
    other=''.join([str(i["other"]) for i in record])
    return "".join([t,detail,other])


# In[34]:


class fasttext(torch.nn.Module):
    def __init__(self):
        super(fasttext,self).__init__()
        self.net=torch.nn.Sequential(
        torch.nn.Linear(300,256),
        torch.nn.ReLU(),
        torch.nn.Linear(256,32),
        torch.nn.ReLU(),
        torch.nn.Linear(32,2),
        torch.nn.Softmax(dim=1))
    
    def forward(self,x):
        out=self.net(x)
        return out


# In[35]:


def bigram(x):
    vectors=FastText(language="zh")
    xx=[]
    for i in range(len(x)-1):
        xx+=[x[i]+x[i+1]]
    if use_cuda:
        return torch.mean(torch.stack(list(map(lambda y:vectors[y],xx))),dim=0).to("cuda")
    else:
        return torch.mean(torch.stack(list(map(lambda y:vectors[y],xx))),dim=0).to("cuda")


# In[36]:


#vscode csv to json插件转换的
data_n=pd.read_json('/home/yuanmanjie/che300/negative_500.json',orient='records')
data_p=pd.read_json('/home/yuanmanjie/che300/positive_500.json',orient='records')


# In[37]:


data_n["data"]=data_n.iloc[:,1].map(get_text)
data_p["data"]=data_p.iloc[:,1].map(get_text)


# In[38]:


data=pd.concat([data_n,data_p])
data["embed"]=data["data"].map(bigram)
data=data.sample(frac=1)


# In[39]:


#保存一下避免之后重跑上面的代码 很耗时……
data.to_excel(r"processed_data.xlsx",index=0)
data=pd.read_excel(r"processed_data.xlsx")


# In[40]:


if use_cuda:
    train_x=torch.stack(list(data["embed"]),dim=0).to("cuda")
    train_y=torch.tensor(list(data["label"])).long().to("cuda")
else:
    train_x=torch.stack(list(data["embed"]),dim=0)
    train_y=torch.tensor(list(data["label"])).long()    
#ones=torch.sparse.torch.eye(2)
#train_y=ones.index_select(0,train_y).long()


# In[ ]:


if use_cuda:
    loss=torch.nn.CrossEntropyLoss(weight=torch.tensor([1.,5.]).to("cuda"))
else:
    loss=torch.nn.CrossEntropyLoss(weight=torch.tensor([1.,5.])
#loss=torch.nn.MSELoss()
epoch_n=1000
learning_rate=1e-3


# In[ ]:


if use_cuda:
    model=fasttext().to("cuda")
else:
    model=fasttext()
optimzer = torch.optim.Adam(model.parameters(),lr = learning_rate)


# In[ ]:


ttrain_x=train_x[:800]
ttrain_y=train_y[:800]
pre_x=train_x[800:]
pre_y=train_y[800:]


# In[ ]:


def test(y,pred):
    l=loss(pred,y)
    print("Loss:{:.4f}".format(l.data),end='')
    ly=pred[:,0]<pred[:,1]
    TP=int(((y==1)&(ly==1)).sum())
    TN=int(((y==0)&(ly==0)).sum())
    FN=int(((y==1)&(ly==0)).sum())
    FP=int(((y==0)&(ly==1)).sum())
    if TP+FN!=0:
        r=TP/(TP+FN)
    else:
        r=-1
    if TP+FP!=0:
        p=TP/(TP+FP)
    else:
        p=-1
    print("p:{:.4f}".format(p),end='')
    print("r:{:.4f}".format(r),end='')
    if r>=0 and p >=0:
        print("acc:{:.4f}".format((TP+TN)/(TP+FP+FN+TN)),end='')
    if r!=0 or p!=0:
        print("F1:{:.4f}".format(2*r*p/(r+p)),end='')
    print("")


# In[ ]:


def te(m,mode=0):
    if mode==0:
        pred=m(pre_x)
        test(pre_y,pred)
    else:
        pred=m(ttrain_x)
        test(ttrain_y,pred)


# In[43]:


for epoch in range(epoch_n):
    y_pred=model(ttrain_x)
    #print(y_pred)
    l=loss(y_pred,ttrain_y)
    if epoch%100==0:
        print("Epoch:{},Loss:{:.4f}".format(epoch,l.data))
#     if epoch%100==0:
        print("training set:",end='')
        te(model,1)
        print("test set:",end='')
        te(model,0)
        
    optimzer.zero_grad()
    l.backward()
    #for param in model.parameters():
    #    param.data-=param.grad.data*lr
    optimzer.step()


# In[10]:





# In[30]:





# In[41]:


data


# In[68]:




