
# coding: utf-8

# In[10]:


import requests
import numpy as np
import json
import re
import os

#author_name_list = []
#author_content = []
author_split_list=[]
author_id_dic = {}
######accounting
with open('/Users/yuxinliu/INF551_project/accounting_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    title = data[i]['Author']
    print(title)
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title = title.replace('.','')
    title = title.replace(';','')
    author_split = title.split(' ')
    if '' in author_split:
        author_split.remove('')
    #print(title_split)
    for j in author_split:
        if j in author_split_list:
            author_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            author_split_list.append(j)
            author_id_dic.update({j:{'id':[data[i]['id']]}})
print(author_id_dic)


# In[11]:


######Engineering
with open('/Users/yuxinliu/INF551_project/Engineering_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    title = data[i]['Author']
    print(title)
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title = title.replace('.','')
    title = title.replace(';','')
    author_split = title.split(' ')
    if '' in author_split:
        author_split.remove('')
    #print(title_split)
    for j in author_split:
        if j in author_split_list:
            author_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            author_split_list.append(j)
            author_id_dic.update({j:{'id':[data[i]['id']]}})
print(author_id_dic)


# In[12]:


#####Economics
with open('/Users/yuxinliu/INF551_project/Economics_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    title = data[i]['Author']
    print(title)
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title = title.replace('.','')
    title = title.replace(';','')
    author_split = title.split(' ')
    if '' in author_split:
        author_split.remove('')
    #print(title_split)
    for j in author_split:
        if j in author_split_list:
            author_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            author_split_list.append(j)
            author_id_dic.update({j:{'id':[data[i]['id']]}})
print(author_id_dic)


# In[13]:


#####Natural Sciences
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    title = data[i]['Author']
    print(title)
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title = title.replace('.','')
    title = title.replace(';','')
    author_split = title.split(' ')
    if '' in author_split:
        author_split.remove('')
    #print(title_split)
    for j in author_split:
        if j in author_split_list:
            author_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            author_split_list.append(j)
            author_id_dic.update({j:{'id':[data[i]['id']]}})
print(author_id_dic)


# In[14]:


#####IT Management
with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    title = data[i]['Author']
    print(title)
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title = title.replace('.','')
    title = title.replace(';','')
    author_split = title.split(' ')
    if '' in author_split:
        author_split.remove('')
    #print(title_split)
    for j in author_split:
        if j in author_split_list:
            author_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            author_split_list.append(j)
            author_id_dic.update({j:{'id':[data[i]['id']]}})
print(author_id_dic)


# In[16]:


for i in author_split_list:
    a = author_id_dic[i]
    #text = str(a)
    print(a)
   
    
    
    meta_title = json.dumps(a)
    #print(meta_title)
    #print(meta_isbn)
    t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author/%s.json' %i, data = meta_title)


# In[29]:


meta_year = json.dumps(list_2008)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2008.json', data = meta_year)


# In[30]:



for j in author_name_list:
    #list_name = i+'_list'
    #list_a = repr(list_name)
    #print(eval(j))
    #print(j)
    #exec ("print(" j + "_list)")
    #exec ("meta_author = json.dumps(" list_name + ")")
    meta_author = json.dumps(eval(j))
    name = j[:-5]
    #print(name)
    #print(meta_author)
    a_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/author/%s.json' %name, data = meta_author)

