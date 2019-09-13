
# coding: utf-8

# In[6]:


import requests
import numpy as np
import json
import re
import os

######accounting
with open('/Users/yuxinliu/INF551_project/accounting_meta.json') as f:
    data = json.load(f)
ISBN_list = []
for i in range(len(data)):
    a = data[i]['ISBN'].replace("-","")
    #print(a)
    ISBN_list.append({a:{'id':data[i]['id']}})

print(ISBN_list)


# In[7]:


#####Economics
with open('/Users/yuxinliu/INF551_project/Economics_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    a = data[i]['ISBN'].replace("-","")
    #print(a)
    ISBN_list.append({a:{'id':data[i]['id']}})
    

#####Engineering
with open('/Users/yuxinliu/INF551_project/Engineering_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    a = data[i]['ISBN'].replace("-","")
    #print(a)
    ISBN_list.append({a:{'id':data[i]['id']}})

#####Natural Sciences
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    a = data[i]['ISBN'].replace("-","")
    #print(a)
    ISBN_list.append({a:{'id':data[i]['id']}})

#####IT Management
with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    a = data[i]['ISBN'].replace("-","")
    #print(a)
    ISBN_list.append({a:{'id':data[i]['id']}})

    



# In[8]:


print(ISBN_list)


# In[14]:


####upload
for i in range(len(ISBN_list)):
    a = ISBN_list[i].keys()
    text = str(a)
    text = text[12:-3]
    meta_isbn = json.dumps(ISBN_list[i][text])
    #print(meta_isbn)
    i_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/ISBN/%s.json' %text, data = meta_isbn)


# In[12]:


for i in range(len(ISBN_list)):
    a = ISBN_list[i].keys()
    text = str(a)
    print(text[12:-3])

