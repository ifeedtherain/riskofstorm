
# coding: utf-8

# In[ ]:

def f(n):
    return n * 10 + 5
print(f(f(f(10))))


# In[ ]:

def min11(n):
    print(n*2)
d = 5
print(min11(d))


# In[2]:

def my_range(start,stop, step =1):
    e = []
    if step > 0:
        x = start
        while x < stop:
            e += [x]
            x += step
    elif x >stop:
        x = start
        while x > stop:
            e +=[x]
            x+= step
    return e
    print(my_range(2,5))


# In[ ]:

print(my_range(2,5))


# In[ ]:



