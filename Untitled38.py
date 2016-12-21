
# coding: utf-8

# In[ ]:

def point(xs):
    xs.append(0)
    xs=[100]
a = []
point(a)
print (a)


# In[ ]:

x= float(input())
def f(x):
        if (x <= -2):
            f =(1-((x-2)**2))
        elif (-2 <x <=2):
            f =(-(x/2))
        elif (2 < x):
            f = ((x -2)**2)+ 1
    return(f)


# In[ ]:

def f(x):
    if (x <= -2):
        f =(1-(x+2)**2)
    elif (-2 <x <=2):
        f =(-(x/2))
    elif (2 < x):
        f = ((x -2)**2)+ 1
    return(f)


# In[ ]:

x= float(input())
print(f(x))


# In[17]:

l=[]
def modify_list(l):
    l=[int for i in input().split()]
    i = 0
    while[i//2 for i in l if i % 2 == 0]:
        l+= i
    while(l[i] % 3 == 0):
        l.remove(i)
        i += 1
        return(l)
modify_list(l)
print(l)        



# In[34]:


def modify_list(l):
    r=[int for x in input().split()]
    r=[i//2 for i in l if i%2==0]
    return(l)
modify_list(l)    
print(modify_list(l))


# In[28]:

a=[1,2,3,4,6,8,9,10]
[x//2 for x in a if x%2==0]


# In[ ]:




# In[ ]:

[i//2 for i in l if i % 2 == 0]

