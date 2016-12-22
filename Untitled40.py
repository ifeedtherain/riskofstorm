
# coding: utf-8

# In[ ]:

# put your python code here
s =[int(i) for i in input().split()]
d=[]

for i in range(len(s)):
    i = 1
    while len(s)> 1: 
        f =s[i]+s[i+1]
        i+= 1 
        d+='f'
    print(d)
else:
    print(s[0])


# In[ ]:

s =[int(i) for i in input().split()]
d=[]
i= 0
for i in s:
    for i in range(len(s)):
        if s[i]== s[0]:
            print (i + s[i(len(s)-1)], end='')
        elif s[i]==s[len(s)-1]:
            
            print(i(0) + i(s[i(len(s)-2)]), end='')
        
        else:
        print(s[i-1]+s[i+1],end=" ")
        


# In[ ]:




# In[ ]:

s =[int(i) for i in input().split()]
d=[]
for i in range(len(s)):
    while i <= len(s):
        if s[i]== s[0]:
            d.append(s[i] + s[(len(s)-1)])
        elif s[i]==s[(len(s)-1)]:
             d.append(s[0] + s[-2])
        elif s[i]== s[0]:
             d.append(s[i - 1] + s[i + 1])
        
    else:
        break 


# In[2]:

s =[int(i) for i in input().split()]
d=[]
i= 0
for i in range(len(s)):
        while s[0]!=i and s[-1]!=i:
            d.append(s[-1] + s[+2])
            i += 1
        if s[i]== s[0]:
            d.append(s[i] + s[-1])
        else: 
            s[-1]== s[+ 1]:
            d.append(s[-1] + s[+1])
print(d)
        


# In[ ]:

s[-1]== s[+ 1]:
            d.append(s[-1] + s[+1])

