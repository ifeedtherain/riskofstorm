
# coding: utf-8

# In[6]:

genome = input()
c = 0
for j in genome:
    if j == 'C':
        c += 1
print(c)


# In[7]:

genome = input()
print(genome.count('C'))


# In[8]:

s = 'agTtcAGtc'
s.upper().count('g'.upper())
s.upper().count('c'.upper())
print('G=', g,'C=', c)


# In[9]:

s = 'acggtgttat'
s.upper().count('gt'.upper())


# In[11]:

s = 'acggtgttat'
g = s.upper().count('g'.upper())
c = s.upper().count('c'.upper())
print('G=', g,'C=', c)


# In[16]:

s = 'acggtgttat'
print(len(s))


# In[18]:

s = input()
g = s.upper().count('g'.upper())
c = s.upper().count('c'.upper())

print(((g + c)/ len(s)*100))


# In[46]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = 0
print('\t', c,'\t', d,'\n')
for k in range(a, b+1):
    print(k, end='\t')
    for j in (c, d):
        print(k * j, end='\t')
        s += 1 
        if (s % 2==0):
            print('\n')


# In[ ]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = 0

for g in range(c,d+1):
    print ('\t', g,end='')
for k in range(a, b+1):
    print()
    print('\t', k, end='')
    for j in range(c, d+1):
        print('\t', k * j, end='')
    


# In[ ]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('\n',end='\t')
for l in range(c,d+1):
    print(l, end='\t')
print('')
for i in range(a,b+1):
    print(i, end='\t')
    for j in range(c,d+1):
        print(j*i, end='\t')
    print(j*i)


# In[100]:

a = int (input())
b = int (input())
c = int (input())
d = int (input())
j = 0
m = 0

for j in range (c,d+1):
        print ('\t',j,end = '')    

for r in range (a,b+1):
        print()
        print (r, end = "")
        for j in range (c,d+1):
            m = j * r
            print ("\t",m,end ="")


# In[ ]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = 0

for g in range(c,d+1):
    print ('\t', g,end='')
for k in range(a, b+1):
    print()
    print('\t', k, end='')
    for j in range(c, d+1):
        print('\t', k * j, end='')


# In[ ]:



