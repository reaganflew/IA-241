
# coding: utf-8

# # lab 1

# In[5]:


print ("hello world")
1+2

a=3


# In[6]:


print (a)


# ## demo

# 1. item 1
# 2. item 2
# 
# JMU [website](https://www.jmu.edu/)

# In[7]:


5+4


# In[8]:


a=4
b=3
print (a+b)


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()

