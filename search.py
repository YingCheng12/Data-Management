
# coding: utf-8

# In[2]:


import requests
import json
import sys

url1 = 'https://inf551homework1.firebaseio.com/index.json'
response3 = requests.get(url1)
m = response3.json()

file = sys.argv[1]

#str = raw_input('please enter the words you want to search:')
#str = input('please enter the words you want to search:')
str = file
str_lower = str.lower()
#type(str)
#key_word_list = []
key_word_list = str_lower.split(' ')
#print(key_word_list)

for i in key_word_list:
    print(i)
    print(m[i])
    #print(i)

