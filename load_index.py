
# coding: utf-8

# In[4]:


import requests
import json
import re
import sys

#open stopwords.txt, and store the word in a list
fp = open('stopwords.txt')
arr=[]
for lines in fp.readlines():
    lines=lines.replace("\n","")
    arr.append(lines)
    #print(lines)
fp.close()

#arr is a list that stores the stopwords
#print(arr)
file = sys.argv[1]

with open(file) as f:
    data = json.load(f)

response = requests.put('https://inf551homework1.firebaseio.com/prize.json', json.dumps(data))

url = 'https://inf551homework1.firebaseio.com/prize.json'
response1 = requests.get(url)
data1 = response1.json()

#print(data['prizes'])
key = data1['prizes']
i_list=[]
k_list=[]
dic = {}

content=[]
for i in key:
    #print(i)
    #i_list.append(i)
    #k_list = []
    for k in i['laureates']:
        k_list.append(k)
        #print(k)
        #print(k["id"])
        #print()
        if 'motivation' in k:
            m_content=k['motivation']
            #print(m_content)
            #n1 = re.sub(r"-,'", "",m_content)
            n1 = m_content.strip('""')
            #print(n1)
            n2 = n1.replace(",","")
            n3 = n2.replace("-",'')
            n4 = n3.replace("'",'')
            n5 = n4.replace('&','')
            n6 = n5.replace(';','')
            n7 = n6.replace(':','')
            n8 = n7.replace('.','')
            n9 = n8.replace('+','')
            n10 = n9.replace('/','')
            n11 = n10.replace('(','')
            n12 = n11.replace(')','')
            n13 = n12.replace('<','')
            n14 = n13.replace('>','')
            n = n14.split(' ')
            #m_content.replace(",","")
            #n = m_content.strip('""').split(' ')
            #print(n)
            for j in n:
                if j not in arr:
                    #print (j)
                    key_d = j.lower()
                    key_d_value = k["id"]
                    #print(key_d)
                    if key_d.isalpha():
                        
                        #dic.update(d)
                        if key_d not in dic.keys():
                            d = {key_d:[key_d_value]}
                            dic.update(d)
                            #dic.setdefault("key_d",).append(key_d_value)
                        else:
                            dic[key_d].append(key_d_value)
                            dic[key_d].sort(reverse=True)

                        #print(key_d_value)
                        #dic['key_d']
                        #print(dic)
#print(dic)
response2 = requests.patch('https://inf551homework1.firebaseio.com/index.json', json.dumps(dic))
#print(response2)

