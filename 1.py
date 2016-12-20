
# coding: utf-8

# In[10]:

d= input()
if (d == 'прямоугольник'):
    a= float(input())
    b= float(input())
    print (a * b)
elif (d == 'треугольник'):
    a= float(input())
    b= float(input())
    c = float(input())
    p= ((a + b + c)/2)
    print((p *(p - a)*(p - b)*(p - c))**0.5)
elif (d == 'круг'):
    a= float(input())
    print(3.14 * (a**2))


# In[14]:

a= int(input())
b= int(input())
c= int(input())

print (max(a, b, c))
print (min(a, b, c))
print(max a, b, c (max(b, c)))


# In[17]:

a= int(input())
b= int(input())
c= int(input())

list.sort (a, b, c)


# In[20]:

a = [int(input()), int(input()),int(input())]
 
list.sort (a)
list.reverce(a)


# In[24]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if ((a + b + c)==(d + e + f)):
    print ('Счастливый')
else:
    print('Обычный')


# In[ ]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if ((a + b + c)!=(d + e + f)):
    print ('Обычный')
else:
    print('Счастливый')

