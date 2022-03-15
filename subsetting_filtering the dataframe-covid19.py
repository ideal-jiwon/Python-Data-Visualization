#!/usr/bin/env python
# coding: utf-8

# Instructions: Use Jupyter Notebook to complete the steps below. 
# Submit your completed Jupyter Notebook and PDF files to Blackboard.

# In[209]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# Use the url to load the data using pandas: 
# https://raw.githubusercontent.com
# /CSSEGISandData/COVID-19/master/csse_covi
# d_19_data/csse_covid_19_time_series/time_se
# ries_covid19_confirmed_US.csv

# In[210]:


url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
df = pd.read_csv(url)


# In[211]:


df.head()


# Melt the data to include dates and cases columns.

# In[212]:


df.drop(columns=["code3","UID","iso2","iso3","FIPS","Country_Region","Lat","Long_"],
        inplace=True)
df.head()


# In[213]:


list = ["Admin2","Province_State","Combined_Key"]


# In[214]:


df = pd.melt(df, id_vars = list,
        var_name = 'dates',
        value_name = 'cases')


# Change dates to a datetime data type.

# In[215]:


df.dtypes


# In[216]:


df.dates = pd.to_datetime(df.dates)


# Subset/filter the dataframe to include data only related to
# Arlington, Virginia as well as Fairfax, Virginia between
# January 1, 2021 and September 30, 2021. Use multi-condition
# syntax when filtering the data (i.e., ‘&’ symbol).  

# In[244]:


df_va = df[(df["Province_State"] == "Virginia")&(df.dates>"2021-01-01")&(df.dates<"2021-09-30")].copy()
df_va_counties = df_va[df_va['Combined_Key'].isin(["Arlington, Virginia, US","Fairfax, Virginia, US"])]
df_va_counties.head()


# In[245]:


Rename three columns as shown below from the subset 
dataframe and use inplace=True:
Admin2 to County
dates  to Date
cases to Number of Cases


# In[246]:


df_va_counties.columns
df_va_counties.rename(columns={"Admin2":"County","dates" : "Date" , "cases" : "Number of Cases"}, inplace=True)
df_va_counties.columns


# In[237]:


Create a FacetGrid using seaborn’s relplot function to create
line charts that display the cumulative cases for Arlington and 
Fairfax. Set the col to County when using the relplot function. 
Format the chart as needed (set axis rotation to 30).


# In[259]:


g1 = sns.relplot(
    data=df_va_counties,
    x="Date", y= "Number of Cases",
    col = "County", kind="line")

