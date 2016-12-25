
# coding: utf-8

# In[ ]:

l = [int(i) for i in input().split()]
d =[]
if len(l)<= 1:
    print(*l)
elif len(l)>1:
    for i in range(len(l)):
        if i == 0 :
            d.append(l[+1]+ l[-1])
        elif i == len(l)-1 :
            d.append(l[0]+l[-2])
        elif i != 0 and i != len(l)-1 :
            d.append(l[(i)-1] + l[(i)+1])                 

d = ' '.join(str(v) for v in d)
print(d)


# In[ ]:

l = [int(i) for i in input().split()]
print(*list({x for x in l if l.count(x) > 1}))


# In[ ]:

l = int(input())
d=[]
i= 1
j= 1
if l == 1:
    print(l)
for i in range(l):
    for j in range(i):
        d.append(i)
        if l ==len(d):
            print(*d, end = '')
      
        
        
    


# In[ ]:




# In[ ]:



