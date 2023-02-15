#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = int(input("enter your marks "))
if marks >=80:
    print("you will be part of A")
elif marks >= 60 and marks < 80:
    print("you will be part of B")
elif marks >= 40 and marks < 60:
    print("you will be part of C")
else :
    print("you will be part of D")


# In[3]:


type(marks)


# In[4]:


price = int(input("enter price "))
if price > 1000:
    print("i will not purchase")
else :
    print("i will purchase")


# In[6]:


price = int(input("enter price "))
if price > 1000:
    print("i will not purchase")


# In[8]:


price = int(input("enter price "))
if price > 1000:
    print("i will not purchase")
    if price >5000:
        print("this is too much")
    elif price  < 2000:
        print("its ok")
elif price < 1000:
    print("i will purchase ")
else :
    print("not intrested")
    


# In[9]:


l = [1,2,3,3,4,5,6,7,8]


# In[11]:


l[0]+1


# In[12]:


l1 = []


# In[13]:


l1.append(l[0]+1)


# In[14]:


l1


# In[15]:


l


# In[16]:


for i in l:
    print(i)


# In[17]:


for i in l:
    print(i+1)


# In[22]:


for i in l:
    print(l)


# In[24]:


l1 = []
for i in l:
    print(i+1)
    l1.append(i+1)
l1


# In[38]:


l = ["ash", "ashu","ashraf","ashrafbhai"]


# In[39]:


l1 = []
for i in l:
    print(i)
    l1.append(i.upper())


# In[28]:


l1 = []
for i in l:
    print(i)
    l1.append(i.upper())


# In[32]:


l = ["ash", "ashu","ashraf"]


# In[33]:


l


# In[34]:


for i in l:
    print(i)


# In[36]:


l1 = []
for i in l:
    print(i)
    l1.append(i.upper())


# In[37]:


l1


# In[40]:


l1


# In[41]:


l = [1,2,3,4,5,4,6,7,"ash","ashu",2.301,"diat"]


# In[43]:


l1_num = []
l2_str = []
for i in l:
    if type(i) == int or type(i) == float :
        l1_num.append(i)     
    else :
        l2_str.append(i)


# In[44]:


l1_num


# In[45]:


l2_str


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




