
# coding: utf-8

# In[5]:


import requests
import numpy as np
import json
import re
import os
with open('/Users/yuxinliu/INF551_project/accounting_meta.json') as f:
    data = json.load(f)

list_2009 = []
list_2010 = []
list_2013 = []
list_2014 = []
list_2015 = []
list_2018 = []

#meta_data = json.dumps(data)
for i in range(len(data)):
    #print(type(data[i]['Creation Year']))
    if data[i]['Creation_Year'] == '2009':
        list_2009.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2010':
        list_2010.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2013':
        list_2013.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2014':
        list_2014.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2015':
        list_2015.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2018':
        list_2018.append(data[i]['id'])
    #else:
        #print(data[i]['Creation Year'])
#print(list_2010)


# In[6]:


with open('/Users/yuxinliu/INF551_project/Economics_meta.json') as f:
    data = json.load(f)
list_2008 = []
list_2017 = []
list_2016 = []
for i in range(len(data)):
    #print(data[i]['Creation Year'])
    if data[i]['Creation_Year'] == '2009':
        list_2009.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2010':
        list_2010.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2013':
        list_2013.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2014':
        list_2014.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2015':
        list_2015.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2018':
        list_2018.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2008':
        list_2008.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2017':
        list_2017.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2016':
        list_2016.append(data[i]['id'])


# In[7]:


with open('/Users/yuxinliu/INF551_project/Engineering_meta.json') as f:
    data = json.load(f)
#list_2008 = []
#ist_2017 = []
#list_2016 = []
for i in range(len(data)):
    #print(data[i]['Creation Year'])
    if data[i]['Creation_Year'] == '2009':
        list_2009.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2010':
        list_2010.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2013':
        list_2013.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2014':
        list_2014.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2015':
        list_2015.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2018':
        list_2018.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2008':
        list_2008.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2017':
        list_2017.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2016':
        list_2016.append(data[i]['id'])



# In[8]:


with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
#list_2008 = []
#ist_2017 = []
#list_2016 = []
for i in range(len(data)):
    #print(data[i]['Creation Year'])
    if data[i]['Creation_Year'] == '2009':
        list_2009.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2010':
        list_2010.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2013':
        list_2013.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2014':
        list_2014.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2015':
        list_2015.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2018':
        list_2018.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2008':
        list_2008.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2017':
        list_2017.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2016':
        list_2016.append(data[i]['id'])



# In[9]:


with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta.json') as f:
    data = json.load(f)
#list_2008 = []
#ist_2017 = []
#list_2016 = []
for i in range(len(data)):
    #print(data[i]['Creation Year'])
    if data[i]['Creation_Year'] == '2009':
        list_2009.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2010':
        list_2010.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2013':
        list_2013.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2014':
        list_2014.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2015':
        list_2015.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2018':
        list_2018.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2008':
        list_2008.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2017':
        list_2017.append(data[i]['id'])
    if data[i]['Creation_Year'] == '2016':
        list_2016.append(data[i]['id'])




# In[17]:


list_2008_json = {'count':len(list_2008),'id':list_2008}
list_2009_json = {'count':len(list_2009),'id':list_2009}
list_2010_json = {'count':len(list_2010),'id':list_2010}
list_2013_json = {'count':len(list_2013),'id':list_2013}
list_2014_json = {'count':len(list_2014),'id':list_2014}
list_2015_json = {'count':len(list_2015),'id':list_2015}
list_2016_json = {'count':len(list_2016),'id':list_2016}
list_2017_json = {'count':len(list_2017),'id':list_2017}
list_2018_json = {'count':len(list_2018),'id':list_2018}


# In[18]:


meta_year = json.dumps(list_2008_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2008.json', data = meta_year)
meta_year = json.dumps(list_2009_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2009.json', data = meta_year)
meta_year = json.dumps(list_2010_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2010.json', data = meta_year)
meta_year = json.dumps(list_2013_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2013.json', data = meta_year)
meta_year = json.dumps(list_2014_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2014.json', data = meta_year)
meta_year = json.dumps(list_2015_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2015.json', data = meta_year)
meta_year = json.dumps(list_2016_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2016.json', data = meta_year)
meta_year = json.dumps(list_2017_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2017.json', data = meta_year)
meta_year = json.dumps(list_2018_json)
y_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/year/2018.json', data = meta_year)

