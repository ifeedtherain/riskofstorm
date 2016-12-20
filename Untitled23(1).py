
# coding: utf-8

# In[6]:

n = int(input())
for i range(n):
    print(i * i)


# In[9]:

for i in range(10):
    print(i * i)


# In[8]:

for i in 2, 3, 4:
    print(i * i)


# In[11]:

n = int(input())
for i in range(n):
    print('*'*n)


# In[12]:

n = int(input())
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()


# In[13]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
a <= b, c<=d
for j in (a, b):
    for k in(c, d):
        print((a * c, a *d, b * c, b * d), end = '')
    print()


# In[21]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
a <= b, c<=d
for j in (a, b):
    print(( a, '\n', b)and(c,'\t', d))
    
  
    print()
    


# In[34]:

a,b = (int(i) for i in input().split())
s = 0
if ((a % 2) == 0):
    a += 1
for i in range(a, (b + 1), 2):
    s += i
print(s)
    


# In[38]:

a, b = (int(i) for i in input().split())
s = 0
for i in range(a, b+1):
    if (i % 3 == 0):
        s += i
print(s)
     


# In[46]:

a, b = (int(i) for i in input().split())
s = 0
t = 0
for i in range(a, b+1):
    if i % 3 ==0:
        s += i
        t += 1
        
print(s / t)
     


# In[ ]:



