from flask import Flask, render_template, request, jsonify
from collections import Counter
import requests
import numpy as np
import json
import re

# print(name)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Book.html') 

@app.route('/get_metadata',methods=['POST'])
def get_metadata():
    link = 'https://inf551project-c1290.firebaseio.com/book.json'
    r_download = requests.get(link)


    author_sum_list = []
    year_sum_list = []
    cat_sum_list = []
    new_author_sum_list = []
    new_year_sum_list = []
    new_cat_sum_list = []
    count = 0
    id_sum_list = []
    input_list = []
    list_pdf=[]


    keyword = request.form.get('keyword')
    adata = request.form.get('adata')
    cdata = request.form.get('cdata')
    ydata = request.form.get('ydata')

    list_input_adata = []
    list_input_cdata = []
    list_input_ydata = []
    result_pdf=[]
    # return_pdf=[]
    resp_a_all= []
    #____________checkbox 输入读取____________
    if adata!=None and adata !='[]':
        count0 = 1
        str_a  = adata[1:-1]
        str_adata = str_a.split(',')
        for i in str_adata:
            b = i[1:-1]
            list_input_adata.append(b)
            # print('********list_input_adata*********')
            # print(list_input_adata)
        for i in list_input_adata:
            aurl = link[:-9]+'Author_Upper/'+ i +'.json'
            resp_a = requests.get(aurl).json()
            resp_a_all.append(resp_a)
        # print('***********resp_a_all************')
        # print(resp_a_all)

    else:
        count0 = 0

    resp_c_all = []
    if cdata!=None and cdata !='[]':
        count1 = 1
        str_c  = cdata[1:-1]
        str_cdata = str_c.split(',')
        for i in str_cdata:
            b = i[1:-1]
            list_input_cdata.append(b)
        for i in list_input_cdata:
            i = i.lower()
            i = i.replace(' ','_')
            curl = link[:-9]+'category/'+ i +'.json'
            resp_c = requests.get(curl).json()
            resp_c_all.append(resp_c)

    else:
        count1 = 0
    
    resp_y_all=[]
    if ydata!=None and ydata !='[]':
        count2 = 1
        str_y  = ydata[1:-1]
        str_ydata = str_y.split(',')
        for i in str_ydata:
            b = i[1:-1]
            list_input_ydata.append(b)
        for i in list_input_ydata:
            yurl = link[:-9]+'year/'+ i +'.json'
            resp_y = requests.get(yurl).json()
            resp_y_all.append(resp_y)
    else:
        count2=0
    

    if keyword != None and keyword!='':
        count3 =1
        keyword_input = keyword.lower()
        keyword_input_split = keyword_input.split(' ')
        # print(keyword_input_split)
        mov_keysli = keyword_input.replace('-','')
        count_split_keyword = len(keyword_input_split)
        # print(count_split_keyword)
        idlist_split_keyword = []
        for i in keyword_input_split:
            caturl = link[:-9]+'category/'+ i +'.json'
            titleurl = link[:-9]+'Title/'+ i+'.json'
            authorurl = link[:-9]+'Author/'+ i + '.json'
            yearurl = link[:-9]+'year/'+i + '.json'
            ISBNurl = link[:-9]+'ISBN/'+mov_keysli + '.json'

            #___________idlist
            idlist = []
            # list_pdf=[]
       
            resp = requests.get(caturl).json()
            
            if resp is not None:
                for a in resp['id']:
                    # print(a)
                    idlist.append(a)
                
            resp1 = requests.get(titleurl).json()   

            if resp1 is not None:
                for b in resp1['id']:
                    # print(b)
                    idlist.append(b)
            # print(idlist)

            resp2 = requests.get(authorurl).json()   
            if resp2 is not None:
                for c in resp2['id']:
                    # print("*******")
                    # print(c)
                    idlist.append(c)
            # print(idlist)

            resp3 = requests.get(yearurl).json()   
            if resp3 is not None:
                for d in resp3['id']:
                    # print(d)
                    idlist.append(d)
            # print(idlist)

            resp4 = requests.get(ISBNurl).json()   
            if resp4 is not None:
                # print(resp4)
                idlist.append(resp4['id'])

            idlist_rm_si = set(idlist)
            idlist_split_keyword += list(idlist_rm_si)
        # print('*******idist*******')
        # print(idlist)
        counter_split = Counter(idlist_split_keyword)
        counter_split_common = counter_split.most_common()
        
        
        # print(counter_split_common)
        #print(b)
        split_list = []
        for i in counter_split_common:
            if i[1]==count_split_keyword:
                split_list.append(i[0])
        # print('*******split_ids_list********')
        # print(split_list)


        return_list = []
        counter_all_list = []
        for j in resp_y_all:
            list_ids= j['id']
            counter_all_list+=list_ids
        # print(counter_all_list)
        for j in resp_c_all:
            list_ids= j['id']
            counter_all_list+=list_ids
        # print(counter_all_list)    
        
        # print('*********resp_a_all******')
        # print(type(resp_a_all))
        # print(resp_a_all)
        
        for j in resp_a_all:
            list_ids= j['id']
            counter_all_list+=list_ids
        
        
        counter_all_list += split_list
        # print('*********here is counter_all_list*************')
        # print(counter_all_list)

        
        # counter_yl_sum = counter_all_list + list(return_list)
        # print(counter_yl_sum)
        c = Counter(counter_all_list)
        b = c.most_common()
        count_123 = count0+count1+count2+count3
        for i in b:
            if i[1]==count_123:
                return_list.append(i[0])
        # print('*************return list*********')
        # print(return_list)

        for i in return_list:
            resulturl = link[:-5]+'/'+str(i)+'.json'
            temp1 = requests.get(resulturl).json()
            result_pdf.append(temp1)
        # print('*********result_pdf*********')
        # print(result_pdf)
            # list_pdf.append(temp1)
            # print(list_pdf)
        # print(result_pdf)

        
    # print('rp:',result_pdf)
    # #————————new checkbox的生成————————

    new_author_name_list  = []
    new_author_count = {}
    new_year_list  = []
    new_year_count = {}

    new_cat_list  = []
    new_cat_count = {}
       
    for i in range(len(result_pdf)):
        new_author = result_pdf[i]['Author']
        new_year = result_pdf[i]['Creation_Year']
        new_cat = result_pdf[i]['category']
    #######author
        if new_author not in new_author_name_list:
            new_author_name_list.append(new_author)
            new_author_count.update({new_author:[1]})
        else:
            new_author_count[new_author].append(1)
    
    #######year
        if new_year not in new_year_list:
            new_year_list.append(new_year)
            new_year_count.update({new_year:[1]})
        else:
            new_year_count[new_year].append(1)
    ######cat
        if new_cat not in new_cat_list:
            new_cat_list.append(new_cat)
            new_cat_count.update({new_cat:[1]})
        else:
            new_cat_count[new_cat].append(1)

    ######author
    new_count_sum_author = []
    for i in new_author_name_list:
        new_count_list = new_author_count[i]
        new_count = len(new_count_list)
        new_count_sum_author.append(new_count)
    #######year
    new_count_sum_year = []
    for i in new_year_list:
        new_count_list = new_year_count[i]
        new_count = len(new_count_list)
        new_count_sum_year.append(new_count)
#######cat
    new_count_sum_cat = []
    for i in new_cat_list:
        new_count_list = new_cat_count[i]
        new_count = len(new_count_list)
        new_count_sum_cat.append(new_count)
########author
    new_index_author = sorted(range(len(new_count_sum_author)), key=lambda x: new_count_sum_author[x],reverse=True)[:3]
    
    for i in new_index_author:
        new_author_sum_list.append([new_author_name_list[i],new_count_sum_author[i]])
        #author_sum_list.update({author_name_list[i]:count_sum_author[i]})
########year
    new_index_year = sorted(range(len(new_count_sum_year)), key=lambda x: new_count_sum_year[x],reverse=True)[:3]
    
    for i in new_index_year:
        new_year_sum_list.append([new_year_list[i],new_count_sum_year[i]])
    #########cat
    new_index_cat = sorted(range(len(new_count_sum_cat)), key=lambda x: new_count_sum_cat[x],reverse=True)[:3]
    
    for i in new_index_cat:
        new_cat_sum_list.append([new_cat_list[i],new_count_sum_cat[i]])
    
    # print(new_author_sum_list)
    # print(new_cat_sum_list)
    # print(new_year_sum_list)

        

    #_______keyword_result___________
    if keyword != None and keyword!='':
        keyword_input = keyword.lower()
        keyword_input_split = keyword_input.split(' ')
        mov_keysli = keyword_input.replace('-','')
        count_split_keyword = len(keyword_input_split)
        idlist_split_keyword = []
        for i in keyword_input_split:
            caturl = link[:-9]+'category/'+ i +'.json'
            titleurl = link[:-9]+'Title/'+ i+'.json'
            authorurl = link[:-9]+'Author/'+ i + '.json'
            yearurl = link[:-9]+'year/'+i + '.json'
            ISBNurl = link[:-9]+'ISBN/'+mov_keysli + '.json'
            idlist = []
       
            resp = requests.get(caturl).json()
            if resp is not None:
                for a in resp['id']:
                    idlist.append(a)
                
            resp1 = requests.get(titleurl).json()   

            if resp1 is not None:
                for b in resp1['id']:
                    idlist.append(b)

            resp2 = requests.get(authorurl).json()   
            if resp2 is not None:
                for c in resp2['id']:
                    idlist.append(c)

            resp3 = requests.get(yearurl).json()   
            if resp3 is not None:
                for d in resp3['id']:
                    idlist.append(d)

            resp4 = requests.get(ISBNurl).json()   
            if resp4 is not None:
                idlist.append(resp4['id'])


            idlist_rm_si = set(idlist)
            idlist_split_keyword += list(idlist_rm_si)

        counter_split = Counter(idlist_split_keyword)
        counter_split_common = counter_split.most_common()
        # print(counter_split_common)
        #print(b)
        split_list = []
        for i in counter_split_common:
            if i[1]==count_split_keyword:
                split_list.append(i[0])
        # print(split_list)
       
        
        for i in split_list:
            list_link = link[:-5]+'/'+ str(i) +'.json'
            temp = requests.get(list_link).json()
            list_pdf.append(temp)

        #_________chechbox的生成_________ 
        author_name_list  = []
        author_count = {}
        year_list  = []
        year_count = {}

        cat_list  = []
        cat_count = {}
       
        for i in range(len(list_pdf)):
            author = list_pdf[i]['Author']
            year = list_pdf[i]['Creation_Year']
            cat = list_pdf[i]['category']
        #######author
            if author not in author_name_list:
                author_name_list.append(author)
                author_count.update({author:[1]})
            else:
                author_count[author].append(1)
        
        #######year
            if year not in year_list:
                year_list.append(year)
                year_count.update({year:[1]})
            else:
                year_count[year].append(1)
        ######cat
            if cat not in cat_list:
                cat_list.append(cat)
                cat_count.update({cat:[1]})
            else:
                cat_count[cat].append(1)

        ######author
        count_sum_author = []
        for i in author_name_list:
            count_list = author_count[i]
            count = len(count_list)
            count_sum_author.append(count)
        #######year
        count_sum_year = []
        for i in year_list:
            count_list = year_count[i]
            count = len(count_list)
            count_sum_year.append(count)
    #######cat
        count_sum_cat = []
        for i in cat_list:
            count_list = cat_count[i]
            count = len(count_list)
            count_sum_cat.append(count)
    ########author
        index_author = sorted(range(len(count_sum_author)), key=lambda x: count_sum_author[x],reverse=True)[:3]
        
        for i in index_author:
            author_sum_list.append([author_name_list[i],count_sum_author[i]])
            #author_sum_list.update({author_name_list[i]:count_sum_author[i]})
    ########year
        index_year = sorted(range(len(count_sum_year)), key=lambda x: count_sum_year[x],reverse=True)[:3]
        
        for i in index_year:
            year_sum_list.append([year_list[i],count_sum_year[i]])
        #########cat
        index_cat = sorted(range(len(count_sum_cat)), key=lambda x: count_sum_cat[x],reverse=True)[:3]
       
        for i in index_cat:
            cat_sum_list.append([cat_list[i],count_sum_cat[i]])
        

        a = len(return_list)
        b = len(split_list)
        if a < b:
            resultcounter = a
            # print('结果个数a')
            # print(resultcounter)
        else:
            resultcounter = b
            # print('结果个数b')
            # print(resultcounter)


    else:
        list_pdf = r_download.json()
        resultcounter = '101'
        # print(resultcounter)

    return jsonify({"result":list_pdf,"author_sum_list":author_sum_list,"new_author_sum_list":new_author_sum_list,"year_sum_list": year_sum_list,"new_year_sum_list": new_year_sum_list,"cat_sum_list":cat_sum_list,"new_cat_sum_list":new_cat_sum_list,"result_pdf":result_pdf,"resultcounter":resultcounter,"success":200})



if __name__ == "__main__":
    app.debug = True
    app.run()
