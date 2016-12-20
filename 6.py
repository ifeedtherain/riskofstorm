
# coding: utf-8

# In[17]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = 0
if (a<=b) and (c <= d) and (a, b, c, d <= 10):
    for g in range(c,d+1):
        print ('\t', g,end='')
    for k in range(a, b+1):
        print()
        print(k, end='')
        for j in range(c, d+1):
            print('\t', k * j, end='')
elif(a >b) and (c > d) and (a, b, c, d > 10):
    print(a, b, c ,d)


# In[ ]:



