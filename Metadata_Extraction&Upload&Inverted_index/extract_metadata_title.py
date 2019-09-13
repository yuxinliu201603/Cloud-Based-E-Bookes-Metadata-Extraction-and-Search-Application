
# coding: utf-8

# In[10]:


import requests
import numpy as np
import json
import re
import os


title_split_list=[]


######accounting
with open('/Users/yuxinliu/INF551_project/accounting_meta.json') as f:
    data = json.load(f)

for i in range(len(data)):

    data[i]

#####Economics
with open('/Users/yuxinliu/INF551_project/Economics_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    title_list.append({data[i]['Title']:data[i]})

#####Engineering
with open('/Users/yuxinliu/INF551_project/Engineering_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    title_list.append({data[i]['Title']:data[i]})

#####Natural Sciences
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    title_list.append({data[i]['Title']:data[i]})

#####IT Management
with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    title_list.append({data[i]['Title']:data[i]})

    



# In[11]:


print(len(title_list))


# In[12]:


for i in range(len(title_list)):
    a = title_list[i].keys()
    text = str(a)
    title = text[12:-3]
   
    
    
    meta_title = json.dumps(title_list[i][title])
    #print(meta_title)
    #print(meta_isbn)
    t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Title/%s.json' %title, data = meta_title)


# In[22]:


import requests
import numpy as np
import json
import re
import os


title_split_list=[]
title_id_dic = {}

######accounting
with open('/Users/yuxinliu/INF551_project/accounting_meta.json') as f:
    data = json.load(f)

for i in range(len(data)):

    title = data[i]['Title']
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    #title = title.replace('','')
    title_split = title.split(' ')
    if '' in title_split:
        title_split.remove('')
    #print(title_split)
    for j in title_split:
        if j in title_split_list:
            title_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            title_split_list.append(j)
            title_id_dic.update({j:{'id':[data[i]['id']]}})
print(title_id_dic)


# In[23]:


#####Economics
with open('/Users/yuxinliu/INF551_project/Economics_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):

    title = data[i]['Title']
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title_split = title.split(' ')
    if '' in title_split:
        title_split.remove('')
    #print(title_split)
    for j in title_split:
        if j in title_split_list:
            title_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            title_split_list.append(j)
            title_id_dic.update({j:{'id':[data[i]['id']]}})
print(title_id_dic)


# In[24]:


#####Engineering
with open('/Users/yuxinliu/INF551_project/Engineering_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):

    title = data[i]['Title']
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title_split = title.split(' ')
    if '' in title_split:
        title_split.remove('')
    #print(title_split)
    for j in title_split:
        if j in title_split_list:
            title_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            title_split_list.append(j)
            title_id_dic.update({j:{'id':[data[i]['id']]}})
print(title_id_dic)


# In[25]:


#####Natural Sciences
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):

    title = data[i]['Title']
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title_split = title.split(' ')
    if '' in title_split:
        title_split.remove('')
    #print(title_split)
    for j in title_split:
        if j in title_split_list:
            title_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            title_split_list.append(j)
            title_id_dic.update({j:{'id':[data[i]['id']]}})
print(title_id_dic)


# In[26]:


#####IT Management
with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):

    title = data[i]['Title']
    title = title.replace('&','')
    title = title.replace('-','')
    title = title.replace(':','')
    title = title.replace(',','')
    title_split = title.split(' ')
    if '' in title_split:
        title_split.remove('')
    #print(title_split)
    for j in title_split:
        if j in title_split_list:
            title_id_dic[j]['id'].append(data[i]['id'])
            
        else:
            title_split_list.append(j)
            title_id_dic.update({j:{'id':[data[i]['id']]}})
print(title_id_dic)


# In[30]:


for i in title_split_list:
    a = title_id_dic[i]
    #text = str(a)
    print(a)
   
    
    
    meta_title = json.dumps(a)
    #print(meta_title)
    #print(meta_isbn)
    t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Title/%s.json' %i, data = meta_title)


# In[21]:


print(title_id_dic['-'])


# In[28]:


print(title_split_list)

