
# coding: utf-8

# In[ ]:

a = int(input())
if (0 <= a <= 1000):
    if ((a == 1) or (a>20 and a%10==1)):
        print(a, 'программист')
    elif ((a % 2 != 0) or (a == 0)or (a %10 == 0) or (a >=100)):
        print(a, 'программистов')        
    else:
        print(a, 'программиста')


# In[ ]:

a = int(input())
if (0 <= a <= 1000):
    if(2<=a<=4):
        print(a, 'программиста')
    elif ((a == 1) or (a>20 and a%10==1)):
        print(a, 'программист')
    elif ((5<=a<=19)or(a % 2 == 0) or (a == 0)or (a %10 == 0) or (a >=100)):
        print(a, 'программистов')        
    else:
        print(a, 'программиста')


# In[ ]:

a = int(input())
if (0 <= a <= 1000):
    if(2<=a<=4):
        print(a, 'программиста')
    elif ((a == 1) or (a>20 and a%10==1)):
        print(a, 'программист')
    elif ((a==0)or(5<=a%10<=19)or(5<=a<=19)):
        print(a, 'программистов')        
    else:
        print(a, 'программиста')


# In[ ]:

a = int(input())
if (0 <= a <= 1000):
    if(2 <=a%10<5):
        print(a, 'программиста')
   
    elif ((a%10==0)or(5<=a%100<=19)or(5<=a%10<=9)):
        print(a, 'программистов')        
    else:
        print(a, 'программист')


# In[ ]:

s = [input()]
s.lower(s)
i = 0
j = 1
cnt = 0
cnt1 = 0
cnt2 = 0
while s[i] == s[j]:
    for nucl in s:
        if nucl == 'a':
            cnt += 1
        if nucl == 'b':
            cnt1 += 1
        if nucl == 'c':
            cnt2 += 1
    i += 1
    j += 1
    if s[i] != s[j]:
        i += 1
        j += 1
        continue
    
print('a',cnt,'b',cnt1,'c', cnt2)


# In[ ]:

b = (input())
b.lower()
i = 0
j = 1
cnt = 0
cnt1 = 0
cnt2 = 0
r = len(b)
for cl in range(r+1):
    while b[i] == b[j]:
        for nucl in b:
            if nucl == 'a':
                cnt += 1
            if nucl == 'b':
                cnt1 += 1
            if nucl == 'c':
                cnt2 += 1
        i += 1
        j += 1
        break
    if b[i] != b[j]:
        i += 1
        j += 1
        continue
   
print('a',cnt,'b',cnt1,'c', cnt2)


# In[ ]:

b = (input())
b.lower()
i = 0
j = 1
cnt = 0
cnt1 = 0
cnt2 = 0
r = len(b)
p= []
for cl in range(r):
    while b[i] == b[j]:
        for nucl in b:
            if nucl == 'a':
                cnt += 1
            if nucl == 'b':
                cnt1 += 1
            if nucl == 'c':
                cnt2 += 1
        i += 1
        j += 1
        break
    else:
        for dl in range(r):
            if b[i] != b[j]:
                p+= nucl, cnt1
                i += 1
                j += 1
                continue
   
print('a',cnt,'b',cnt1,'c', cnt2)


# In[ ]:

b = (input())
b.lower()
i = 0
cnt = 1
for i in range(len(b)):
    if (b[i]==b[i+1]):
        cnt+= 1
        
    elif (b[i]!=b[i+1]):
        
        print(b[i],cnt, end='')
        continue


# In[10]:

b = (input())
b.lower()
cnt = 1
for i in range(len(b)):
    if ((i==(len(b)-1)) or (b[i]!=b[i+1])):
        print(b[i] + str(cnt), end='')
        cnt = 1
    elif (b[i]==b[i+1]):
        cnt+=1
    i+=1


# In[ ]:



