#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[15]:


cwd = os.getcwd()
print(cwd)


# In[5]:


get_ipython().system('ls')


# In[6]:


os.chdir('Desktop')


# In[7]:


get_ipython().system('ls')


# In[8]:


os.chdir('Images')


# In[10]:


get_ipython().system('ls')


# In[11]:


direc_list=os.listdir()


# In[13]:


for image in direc_list:
    if "raw" in image:
        print(image)


# In[ ]:




