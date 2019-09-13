
# coding: utf-8

# In[35]:


import PIL
from PyPDF2 import PdfFileReader
import regex as re
import minecart
from pdf2image import convert_from_path


#define get_metadata function
def get_metadata(name):

    
    pdf = PdfFileReader(name)

    if pdf.isEncrypted:
        pdf.decrypt('')
    info = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    
    dic_meta = {}
    author_lower = info.author.lower()
    title_lower = info.title.lower()
    dic_meta.update({'Author':author_lower})
    #dic_meta.update({'Creator':info.creator})
    dic_meta.update({'Title':title_lower})
    dic_meta.update({'Page_Number':number_of_pages})
    
        
    return dic_meta


# In[36]:


edition_dic = {}
#define get extra metadata function
def get_edition1(i):
    
    pdf = PdfFileReader(i)

    if pdf.isEncrypted:
        pdf.decrypt('')
    list_me = []    
    for j in (1,2):
        
        pageObj = pdf.getPage(j)
        text = pageObj.extractText()
    
        year = re.search(r'© \d\d\d\d', text)
        if year :
            
            edition_dic.update({'Creation_Year':year.group()[2:6]})
        edition = re.search(r'\d*\w\w edition', text)
   
        if edition:
            
            edition_dic.update({'Edition':edition.group()})
            
        match = re.search(r'ISBN [\d*-]*\d*', text)
        if match :
           
            edition_dic.update({'ISBN':match.group()[5:]})
            
    
    return edition_dic


# In[37]:


######Accounting
import requests
import numpy as np
import json
import re
import os
#print (os.getcwd())
os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Accounting')
a.remove('.ipynb_checkpoints')
os.chdir('Accounting')
dic_meta = {}
list_meta = []
a_list = []
year_list = []
merge_meta = {}
id_count = 0
for i in a:
    
    cate = {'category':'accounting'}
    meta_1 = get_metadata(i)#提取基本metadata
    meta_2 = get_edition1(i)#提取匹配metadata
    meta_1.update(meta_2)
    meta_1.update(cate)
    meta_1.update({'id':id_count})
    #cate = {'category':'Accounting'}
    a_list.append(meta_1)
    #a_list.append(cate)
    id_count+=1
    
#dic_meta.update({'Accounting':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/accounting_meta.json","w") as f:
    json.dump(a_list,f)

#load index json文件并且上传到firebase里
with open('/Users/yuxinliu/INF551_project/accounting_meta.json') as f:
    data = json.load(f)

list_accounting_id =[]
for i in range(len(data)):
    #print(data[i]['id'])
#meta_data = json.dumps(data)
    meta_data = data[i]['id']
    list_accounting_id.append(meta_data)
    #list_accounting_id.append(meta_data)
list_accounting_dic = {}
list_accounting_dic.update({'count':33})
list_accounting_dic.update({'id':list_accounting_id})
meta_data = json.dumps(data)
print(list_accounting_dic)
meta_data = json.dumps(list_accounting_dic)
r_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/category/accounting.json', data = meta_data)


# In[38]:


######Natural Sciences

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Natural Sciences')
a.remove('.ipynb_checkpoints')
os.chdir('Natural Sciences')
dic_meta = {}
list_meta = []
a_list = []
year_list = []
merge_meta = {}
for i in a:
    
    cate = {'category':'natural sciences'}
    meta_1 = get_metadata(i)#提取基本metadata
    meta_2 = get_edition1(i)#提取匹配metadata
    meta_1.update(meta_2)
    meta_1.update(cate)
    #cate = {'category':'Accounting'}
    a_list.append(meta_1)
    #a_list.append(cate)
    meta_1.update({'id':id_count})
    id_count+=1
    
    
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/Natural Sciences_meta.json","w") as f:
    json.dump(a_list,f)

#load index json文件并且上传到firebase里
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta.json') as f:
    data = json.load(f)

list_accounting_id =[]
for i in range(len(data)):
    #print(data[i]['id'])
#meta_data = json.dumps(data)
    meta_data = data[i]['id']
    list_accounting_id.append(meta_data)
    #list_accounting_id.append(meta_data)
list_accounting_dic = {}
list_accounting_dic.update({'count':len(data)})
list_accounting_dic.update({'id':list_accounting_id})
meta_data = json.dumps(data)
print(list_accounting_dic)
meta_data = json.dumps(list_accounting_dic)

r_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/category/natural_sciences.json', data = meta_data)


# In[39]:


######Economics

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Economics')
a.remove('.ipynb_checkpoints')
os.chdir('Economics')
dic_meta = {}
list_meta = []
a_list = []
year_list = []
merge_meta = {}
for i in a:
    
    cate = {'category':'economics'}
    meta_1 = get_metadata(i)#提取基本metadata
    meta_2 = get_edition1(i)#提取匹配metadata
    meta_1.update(meta_2)
    meta_1.update(cate)
    #cate = {'category':'Accounting'}
    a_list.append(meta_1)
    #a_list.append(cate)
    meta_1.update({'id':id_count})
    id_count+=1
    
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/Economics_meta.json","w") as f:
    json.dump(a_list,f)

#load index json文件并且上传到firebase里
with open('/Users/yuxinliu/INF551_project/Economics_meta.json') as f:
    data = json.load(f)

    
list_accounting_id =[]
for i in range(len(data)):
    #print(data[i]['id'])
#meta_data = json.dumps(data)
    meta_data = data[i]['id']
    list_accounting_id.append(meta_data)
    #list_accounting_id.append(meta_data)
list_accounting_dic = {}
list_accounting_dic.update({'count':len(data)})
list_accounting_dic.update({'id':list_accounting_id})
meta_data = json.dumps(data)
print(list_accounting_dic)
meta_data = json.dumps(list_accounting_dic)    
    

r_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/category/economics.json', data = meta_data)


# In[40]:


######Engineering

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Engineering')
a.remove('.ipynb_checkpoints')
os.chdir('Engineering')
dic_meta = {}
list_meta = []
a_list = []
year_list = []
merge_meta = {}
for i in a:
    
    cate = {'category':'engineering'}
    meta_1 = get_metadata(i)#提取基本metadata
    meta_2 = get_edition1(i)#提取匹配metadata
    meta_1.update(meta_2)
    meta_1.update(cate)
    #cate = {'category':'Accounting'}
    a_list.append(meta_1)
    #a_list.append(cate)
    meta_1.update({'id':id_count})
    id_count+=1
    
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/Engineering_meta.json","w") as f:
    json.dump(a_list,f)

#load index json文件并且上传到firebase里
with open('/Users/yuxinliu/INF551_project/Engineering_meta.json') as f:
    data = json.load(f)
    
list_accounting_id =[]
for i in range(len(data)):
    #print(data[i]['id'])
#meta_data = json.dumps(data)
    meta_data = data[i]['id']
    list_accounting_id.append(meta_data)
    #list_accounting_id.append(meta_data)
list_accounting_dic = {}
list_accounting_dic.update({'count':len(data)})
list_accounting_dic.update({'id':list_accounting_id})
meta_data = json.dumps(data)
print(list_accounting_dic)
meta_data = json.dumps(list_accounting_dic)
r_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/category/engineering.json', data = meta_data)


# In[41]:



######IT Management

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('IT Management')
a.remove('.ipynb_checkpoints')
os.chdir('IT Management')
dic_meta = {}
list_meta = []
a_list = []
year_list = []
merge_meta = {}
for i in a:
    
    cate = {'category':'it management'}
    meta_1 = get_metadata(i)#提取基本metadata
    meta_2 = get_edition1(i)#提取匹配metadata
    meta_1.update(meta_2)
    meta_1.update(cate)
    #cate = {'category':'Accounting'}
    a_list.append(meta_1)
    #a_list.append(cate)
    meta_1.update({'id':id_count})
    id_count+=1
    
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/IT Management_meta.json","w") as f:
    json.dump(a_list,f)

#load index json文件并且上传到firebase里
with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
    
list_accounting_id =[]
for i in range(len(data)):
    #print(data[i]['id'])
#meta_data = json.dumps(data)
    meta_data = data[i]['id']
    list_accounting_id.append(meta_data)
    #list_accounting_id.append(meta_data)
list_accounting_dic = {}
list_accounting_dic.update({'count':len(data)})
list_accounting_dic.update({'id':list_accounting_id})
meta_data = json.dumps(data)
print(list_accounting_dic)
meta_data = json.dumps(list_accounting_dic)
r_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/category/it_management.json', data = meta_data)


# In[42]:


######accounting
with open('/Users/yuxinliu/INF551_project/accounting_meta.json') as f:
    data = json.load(f)
id_list = []
for i in range(len(data)):

    id_list.append({data[i]['id']:data[i]})
    
#####Economics
with open('/Users/yuxinliu/INF551_project/Economics_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})

#####Engineering
with open('/Users/yuxinliu/INF551_project/Engineering_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})

#####Natural Sciences
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})

#####IT Management
with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})



# In[43]:


print(id_list)


# In[44]:


def get_metadata(name):

    
    pdf = PdfFileReader(name)

    if pdf.isEncrypted:
        pdf.decrypt('')
    info = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    
    dic_meta = {}
    author_lower = info.author.lower()
    title_lower = info.title.lower()
    dic_meta.update({'Author':author_lower})
    #dic_meta.update({'Creator':info.creator})
    dic_meta.update({'Title':title_lower})
    dic_meta.update({'Page_Number':number_of_pages})
    
        
    return dic_meta



# In[35]:





# In[45]:


import requests
import numpy as np
import json
import re

accounting_data = json.dumps(dic_meta)
#print accounting_data.isalpha();
#print(accounting_data)

r = requests.put('https://inf551project-c1290.firebaseio.com/accounting.json', data = accounting_data)
#k = index_dic['index']


# In[46]:


os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Accounting')
print(a)


index_data = json.dumps(index_dic)
loadindex = requests.put('https://inf551project-c1290.firebaseio.com/accounting.json', data = index_data)
#k = index_dic['index']
#k1 = list(k.keys())


# In[59]:


def get_metadata2(name):

    
    pdf = PdfFileReader(name)

    if pdf.isEncrypted:
        pdf.decrypt('')
    info = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    
    dic_meta_2 = {}
    #author_lower = info.author.lower()
    #title_lower = info.title.lower()
    dic_meta_2.update({'Author':info.author})
    #dic_meta.update({'Creator':info.creator})
    dic_meta_2.update({'Title':info.title})
    dic_meta_2.update({'Page_Number':number_of_pages})
    
        
    return dic_meta_2


# In[60]:


edition_dic = {}
#define get extra metadata function
def get_edition2(i):
    
    pdf = PdfFileReader(i)

    if pdf.isEncrypted:
        pdf.decrypt('')
    list_me = []    
    for j in (1,2):
        
        pageObj = pdf.getPage(j)
        text = pageObj.extractText()
    
        year = re.search(r'© \d\d\d\d', text)
        if year :
            
            edition_dic.update({'Creation_Year':year.group()[2:6]})
        edition = re.search(r'\d*\w\w edition', text)
   
        if edition:
            
            edition_dic.update({'Edition':edition.group()})
            
        match = re.search(r'ISBN [\d*-]*\d*', text)
        if match :
           
            edition_dic.update({'ISBN':match.group()[5:]})
            
    
    return edition_dic



# In[61]:


######Accounting
import requests
import numpy as np
import json
import re
import os
#print (os.getcwd())
os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Accounting')
a.remove('.ipynb_checkpoints')
os.chdir('Accounting')
dic_meta_2 = {}
list_meta_2 = []
a_list_2 = []
year_list_2 = []
merge_meta_2 = {}
id_count_2 = 0
for i in a:
    
    cate = {'category':'Accounting'}
    meta_1_2 = get_metadata2(i)#提取基本metadata
    meta_2_2 = get_edition2(i)#提取匹配metadata
    meta_1_2.update(meta_2_2)
    meta_1_2.update(cate)
    meta_1_2.update({'id':id_count_2})
    #cate = {'category':'Accounting'}
    a_list_2.append(meta_1_2)
    #a_list.append(cate)
    id_count_2+=1
    
#dic_meta.update({'Accounting':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/accounting_meta_2.json","w") as f:
    json.dump(a_list_2,f)

#load index json文件并且上传到firebase里
with open('/Users/yuxinliu/INF551_project/accounting_meta_2.json') as f:
    data = json.load(f)
    


# In[62]:


print(a_list_2)


# In[63]:


######Natural Sciences

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Natural Sciences')
a.remove('.ipynb_checkpoints')
os.chdir('Natural Sciences')
dic_meta_2 = {}
list_meta_2 = []
a_list_2 = []
year_list_2 = []
merge_meta_2 = {}
id_count_2 = 33
for i in a:
    
    cate = {'category':'Natural Sciences'}
    meta_1_2 = get_metadata2(i)#提取基本metadata
    meta_2_2 = get_edition2(i)#提取匹配metadata
    meta_1_2.update(meta_2_2)
    meta_1_2.update(cate)
    #cate = {'category':'Accounting'}
    a_list_2.append(meta_1_2)
    #a_list.append(cate)
    meta_1_2.update({'id':id_count_2})
    id_count_2+=1
    print(id_count_2)
    
    
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/Natural Sciences_meta_2.json","w") as f:
    json.dump(a_list_2,f)



# In[64]:


print(a_list_2)


# In[67]:


######Economics

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Economics')
a.remove('.ipynb_checkpoints')
os.chdir('Economics')
dic_meta_2 = {}
list_meta_2 = []
a_list_2 = []
year_list_2 = []
merge_meta_2 = {}
id_count_2 = 59
for i in a:
    
    cate = {'category':'economics'}
    meta_1_2 = get_metadata2(i)#提取基本metadata
    meta_2_2 = get_edition2(i)#提取匹配metadata
    meta_1_2.update(meta_2_2)
    meta_1_2.update(cate)
    #cate = {'category':'Accounting'}
    a_list_2.append(meta_1_2)
    #a_list.append(cate)
    meta_1_2.update({'id':id_count_2})
    id_count_2+=1
    print(id_count_2)
    
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/Economics_meta_2.json","w") as f:
    json.dump(a_list_2,f)



# In[68]:


print(a_list_2)


# In[69]:


######Engineering

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('Engineering')
a.remove('.ipynb_checkpoints')
os.chdir('Engineering')
dic_meta = {}
list_meta = []
a_list = []
year_list = []
merge_meta = {}
id_count_2 = 92
for i in a:
    
    cate = {'category':'Engineering'}
    meta_1 = get_metadata2(i)#提取基本metadata
    meta_2 = get_edition2(i)#提取匹配metadata
    meta_1.update(meta_2)
    meta_1.update(cate)
    #cate = {'category':'Accounting'}
    a_list.append(meta_1)
    #a_list.append(cate)
    meta_1.update({'id':id_count_2})
    id_count_2+=1
    print(id_count_2)
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/Engineering_meta_2.json","w") as f:
    json.dump(a_list,f)



# In[70]:


print(a_list)


# In[71]:



######IT Management

os.chdir('/Users/yuxinliu/INF551_project/')
a = os.listdir('IT Management')
a.remove('.ipynb_checkpoints')
os.chdir('IT Management')
dic_meta = {}
list_meta = []
a_list = []
year_list = []
merge_meta = {}
id_count_2 = 95
for i in a:
    
    cate = {'category':'it management'}
    meta_1 = get_metadata2(i)#提取基本metadata
    meta_2 = get_edition2(i)#提取匹配metadata
    meta_1.update(meta_2)
    meta_1.update(cate)
    #cate = {'category':'Accounting'}
    a_list.append(meta_1)
    #a_list.append(cate)
    meta_1.update({'id':id_count_2})
    id_count_2+=1
    
#dic_meta.update({'Natural Sciences':a_list})


#将index data 写到.json 文件里
with open("/Users/yuxinliu/INF551_project/IT Management_meta_2.json","w") as f:
    json.dump(a_list,f)


# In[72]:


print(a_list)


# In[73]:


######accounting
with open('/Users/yuxinliu/INF551_project/accounting_meta_2.json') as f:
    data = json.load(f)
id_list = []
for i in range(len(data)):

    id_list.append({data[i]['id']:data[i]})

#####Natural Sciences
with open('/Users/yuxinliu/INF551_project/Natural Sciences_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})
    
#####Economics
with open('/Users/yuxinliu/INF551_project/Economics_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})

#####Engineering
with open('/Users/yuxinliu/INF551_project/Engineering_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})



#####IT Management
with open('/Users/yuxinliu/INF551_project/IT Management_meta_2.json') as f:
    data = json.load(f)
for i in range(len(data)):
    #print(data[i]['ISBN'][4:])
    id_list.append({data[i]['id']:data[i]})




# In[81]:


print(id_list)


# In[74]:


####upload
for i in range(len(id_list)):
    a = id_list[i].keys()
    text = str(a)
    
    #isbn = re.search(r'[\d*-]*\d', text)
    #print(isbn.group())
    string_id = text[11:-2]
    print(string_id)
    meta_id = json.dumps(id_list[i][i])
        #print(meta_isbn)
    i_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/book/%s.json' %string_id ,data = meta_id)


# In[75]:


#load index json文件并且上传到firebase里
with open('/Users/yuxinliu/INF551_project/IT Management_meta.json') as f:
    data = json.load(f)
    
list_accounting_id =[]
for i in range(len(data)):
    #print(data[i]['id'])
#meta_data = json.dumps(data)
    meta_data = data[i]['id']
    list_accounting_id.append(meta_data)
    #list_accounting_id.append(meta_data)
list_accounting_dic = {}
list_accounting_dic.update({'count':len(data)})
list_accounting_dic.update({'id':list_accounting_id})
meta_data = json.dumps(data)
print(list_accounting_dic)
meta_data = json.dumps(list_accounting_dic)
r_uploadjason = requests.put('https://inf551project-c1290.firebaseio.com/category/it_management.json', data = meta_data)

