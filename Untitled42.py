
# coding: utf-8

# In[ ]:


lst= [int (g) for g in input().split()]
x = int(input()) 
d = []
while i in range(len(lst)):
    if x == lst[i]:
        d.append(i)
        i += 1
    elif x!= lst[i]:
        i += 1
if len(d)== 0:
    d.append('Отсутствует')
l = ' '.join(str(v) for v in d) 
print(l) 


# In[ ]:

def f(x):
    if (x <= -2):
        f =(1-(x+2)**2)
    elif (-2 <x <=2):
        f =(-(x/2))
    elif (2 < x):
        f = ((x -2)**2)+ 1
    return(f)
        


# In[5]:

import math

s = float(input())
d = 2*(math.pi*s)
print(d)


# In[19]:

import sys
import subprocess
sys.arvg=['python3', 'my_solution.py', 'arg1 arg2 arg1 arg2']
subprocess.call(sys.arvg)


# In[ ]:



