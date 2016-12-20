
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


# In[ ]:



