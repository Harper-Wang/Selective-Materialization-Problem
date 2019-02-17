#%%
import numpy as np 
import pandas as pd 

# testdata
data=dict(abcde=[12], abcd=[9], abce=[10], abde=[8], acde=[7], bcde=[4], abc=[2.5], abd=[3], abe=[5], acd=[2.8], ace=[3], ade=[2.2], bcd=[2], bce=[1.9], bde=[1.7], 
cde=[3.7], ab=[1.9], ac=[2.1], ad=[0.5], ae=[2.1], bc=[0.7], bd=[0.3], be=[1.4], 
cd=[0.4], ce=[1.7], de=[0.6], a=[0.1], b=[0.3], c=[0.1], d=[0.2], e=[0.2])
topview = 'abcde'
for view in data.keys():
    data[view].append(data[topview][0]) 
# print(data)
# print(data.items())
# print(data.keys())
# print(data.values())
# print(len(data))
# for i in data.keys():
#     print (i)
#%%
# decide if x belong to y
def belong(x,y):
    x=set(x)
    y=set(y)
    if x.issubset(y):
        return True
    else:
        return False

# get gain for one sample
def Gain(dict1,x,y):
    if belong(y,x):
        a = dict1[y][1]-dict1[x][0]
        if a>=0:
            return a
        else:
            return 0
    else :
        return 0

#%%
# update cost for one sample
def updatecost(dict1,x):
    for i in dict1.keys():
        if belong(i,x) and dict1[i][1]>dict1[x][0]:
            dict1[i][1]=dict1[x][0]

        
#%%
# main function
def selectiveM(dict1,k,topview):
    view_selected = []
    for i in range(k):
        gain_v={}
        for j in dict1.keys():
            gain=0
            for k in dict1.keys():
                gain +=Gain(dict1,j,k)
            gain_v[j] = gain
        view_selected.append(max(gain_v,key=gain_v.get))
        updatecost(dict1,view_selected[i])
        print(dict1)
    return view_selected

# get result
print(selectiveM(data,3,topview)) 
            




        

