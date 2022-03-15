#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


x_url = "https://raw.githubusercontent.com/babdelfa/x/main/xdata1.csv"

x = pd.read_csv(x_url)
x.head()


# In[45]:


x.tail()


# In[3]:


x.corr()


# In[9]:


x_America = x[(x["CONTINENT"] == "Americas")]
x_America.corr()


# In[11]:


x_America["LIFE EXPECTANCY_CHANGE"] = x_America["LIFE EXPECTANCY"].diff()


# In[16]:


x_America["LIFE EXPECTANCY_CHANGE"].sum()


# In[26]:


x_US = x[(x["COUNTRY"] == "United States")]
x_US["LIFE EXPECTANCY_CHANGE"] = x_US["LIFE EXPECTANCY"].diff()


# In[27]:


x_US["LIFE EXPECTANCY_CHANGE"].mean()


# In[30]:


x_America["LIFE EXPECTANCY"].mean()


# In[42]:


x_coun1 = x[(x["COUNTRY"] == "United States")&(x.YEAR>1956)&(x.YEAR<2008)]
x_coun1.tail()


# In[44]:


x_coun2 = x[(x["COUNTRY"] == "United Kingdom")&(x.YEAR>1956)&(x.YEAR<2008)]
x_coun2.tail()


# In[40]:


x_coun3 = x[(x["COUNTRY"] == "Canada")&(x.YEAR>1956)&(x.YEAR<2008)]
x_coun3.tail()


# In[ ]:





# In[ ]:





# In[ ]:




