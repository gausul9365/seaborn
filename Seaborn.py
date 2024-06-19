#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


a = sns.load_dataset("flights")
sns.relplot(x="passengers", y = "month",data=a )


# In[5]:


a = sns.load_dataset("flights")
sns.relplot(x="passengers", y = "month", hue = "year", data=a )


# In[6]:


b=sns.load_dataset("tips")
sns.relplot(x="time", y="tip", data=b, kind="line")


# In[7]:


sns.catplot(x="day", y = "total_bill", data=b)


# In[10]:


sns.catplot(x="day", y = "total_bill", kind="violin", data=b)


# In[11]:


sns.catplot(x="day", y = "total_bill", kind="boxen", data=b)


# In[12]:


from scipy import stats


# In[14]:


c= np.random.normal(loc=5, size=100,scale=2)


# In[16]:


sns.distplot(c)


# In[ ]:





# In[6]:


a= sns.load_dataset("iris")
b= sns.FacetGrid(a, col="species")
b.map(plt.hist, "sepal_length")


# In[ ]:





# In[9]:


a= sns.load_dataset("flights")
b= sns.PairGrid(a)
b.map(plt.scatter)


# In[10]:


sns.set(style="darkgrid")
a= sns.load_dataset("flights")
b= sns.PairGrid(a)
b.map(plt.scatter)


# In[11]:


sns.set(style="dark")
a= sns.load_dataset("flights")
b= sns.PairGrid(a)
b.map(plt.scatter)


# In[16]:


sns.set(style="white",color_codes = True)
a=sns.load_dataset("tips")
sns.boxplot(x="day", y = "total_bill", data=a)
sns.despine(offset=10,trim=True)


# In[18]:


c=sns.color_palette()
sns.palplot(c)


# In[ ]:




