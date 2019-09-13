
# coding: utf-8

# In[18]:


import requests
import numpy as np
import json
import re
import os
author_list = []

author_id = {}

with open('/Users/yuxinliu/INF551_project/accounting_meta_2.json') as f:
    data = json.load(f)

for i in range(len(data)):
    au = data[i]['Author']
    #print(au)
    if au in author_list:
        author_id[au]['id'].append(data[i]['id'])
            
    else:
        author_list.append(au)
        author_id.update({au:{'id':[data[i]['id']]}})


######Engineering
with open('/Users/yuxinliu/INF551_project/Engineering_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    au = data[i]['Author']
    #print(au)
    if au in author_list:
        author_id[au]['id'].append(data[i]['id'])
            
    else:
        author_list.append(au)
        author_id.update({au:{'id':[data[i]['id']]}})

#####Economics
with open('/Users/yuxinliu/INF551_project/Economics_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    au = data[i]['Author']
    #print(au)
    if au in author_list:
        author_id[au]['id'].append(data[i]['id'])
            
    else:
        author_list.append(au)
        author_id.update({au:{'id':[data[i]['id']]}})

#####Natural Sciences
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    au = data[i]['Author']
    #print(au)
    if au in author_list:
        author_id[au]['id'].append(data[i]['id'])
            
    else:
        author_list.append(au)
        author_id.update({au:{'id':[data[i]['id']]}})

#####IT Management
with open('/Users/yuxinliu/INF551_project/IT Management_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    au = data[i]['Author']
    #print(au)
    if au in author_list:
        author_id[au]['id'].append(data[i]['id'])
            
    else:
        author_list.append(au)
        author_id.update({au:{'id':[data[i]['id']]}})


# In[23]:


#print(author_id)
print(author_list)


# In[25]:


for i in author_list:
    print(i)
    a = author_id[i]
    #text = str(a)
    print(a)
   
    
    
    meta_author = json.dumps(a)
    #print(meta_title)
    #print(meta_isbn)
    t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %i, data = meta_author)


# In[26]:


print(len(author_list))


# In[34]:


b = 'Christopher J Skousen; Larry M Walther'
a = author_id['Christopher J. Skousen; Larry M. Walther']
print(a)
meta_author = json.dumps(a)


# In[35]:


t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %b, data = meta_author)


# In[36]:


c = 'C T Draijer; D J Schenk'
a = author_id['C.T. Draijer; D.J. Schenk']
print(a)
meta_author = json.dumps(a)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %c, data = meta_author)


# In[37]:


d = 'J E Parker'
a = author_id['J. E. Parker']
print(a)
meta_author = json.dumps(a)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %d, data = meta_author)


# In[38]:


a = 'Dr Wilhelm Schmeisser; Lydia Clausen; Martina Lukowsky'
b = author_id['Dr. Wilhelm Schmeisser; Lydia Clausen; Martina Lukowsky']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[39]:


a = 'Prof Dr Dieter Gerdesmeier'
b = author_id['Prof. Dr. Dieter Gerdesmeier']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[41]:


#Elly R. Twineyo Kamugisha
a = 'Elly R Twineyo Kamugisha'
b = author_id['Elly R. Twineyo Kamugisha']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[42]:


#Dr. Jinliao He; Ke He; Wei Linlin
a = 'Dr Jinliao He; Ke He; Wei Linlin'
b = author_id['Dr. Jinliao He; Ke He; Wei Linlin']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[43]:


#A. W. Mullineux
a = 'A W Mullineux'
b = author_id['A. W. Mullineux']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[44]:


#W. David McComb
a = 'W David McComb'
b = author_id['W. David McComb']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[45]:


#Thomas L. Isenhour
a = 'Thomas L Isenhour'
b = author_id['Thomas L. Isenhour']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[47]:


#Nicholas N.N. Nsowah-Nuamah
a = 'Nicholas N N Nsowah-Nuamah'
b = author_id['Nicholas N.N. Nsowah-Nuamah']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[48]:


#Prof. Dr J. Clifford Jones
a = 'Prof Dr J Clifford Jones'
b = author_id['Prof. Dr J. Clifford Jones']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[49]:


#Dr. Jixiang Yang
a = 'Dr Jixiang Yang'
b = author_id['Dr. Jixiang Yang']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[51]:


#Dr. Geert Potters
a = 'Dr Geert Potters'
b = author_id['Dr. Geert Potters']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)


# In[52]:


#Dr. Julie Reinhart; Dr. Renee Robinson
a = 'Dr Julie Reinhart; Dr Renee Robinson'
b = author_id['Dr. Julie Reinhart; Dr. Renee Robinson']
print(b)
meta_author = json.dumps(b)
t_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/Author_Upper/%s.json' %a, data = meta_author)

