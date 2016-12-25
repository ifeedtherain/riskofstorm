
# coding: utf-8

# In[43]:

import requests
file = requests.get('https://stepic.org/media/attachments/course67/3.6.2/580.txt')
file= file.text
s = file.splitlines()
print(len(s))




# In[34]:

import requests

url= input()
r = requests.get(url)
r= r.text #is the answer!


# In[39]:

import requests
file=requests.get('https://stepic.org/media/attachments/course67/3.6.2/580.txt')
file=file.text
k=len(file.splitlines())
print(k)


# In[ ]:



