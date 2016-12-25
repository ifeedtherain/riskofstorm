
# coding: utf-8

# In[1]:

import sys
del sys.argv [0]
for i in sys.argv:
    print(i, end='')


# In[3]:

import sys
del sys.argv [0:0]
for i in sys.argv:
    print(i, end='')


# In[5]:

import sys
argv= readline.input()
del sys.argv [0]
for i in sys.argv:
    print(i, end='',)


# In[6]:

import sys
argv= input()
del sys.argv [0:0]
for i in sys.argv:
    print(*sys.argv[1:])


# In[7]:

import sys
print(*sys.argv[1:])


# In[ ]:



