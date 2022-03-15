#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1) total reported COVID-19 cases over time
2) state level geometry shapes
3) county level geometry shapes

*required libraries : pandas, geopandas, matplotlib, and contextily


# In[2]:


#Jiwon Mok G01096224
import os
os.getcwd()


# In[3]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily


# In[1]:


PART1
#""https://github.com/babdelfa/project/blob/main/covid19_project.csv?raw=true""


# In[4]:


url_cases = "https://github.com/babdelfa/project/blob/main/covid19_project.csv?raw=true"
df_cases = pd.read_csv(url_cases)
df_cases.head()


# In[5]:


df_cases_melted = pd.melt(df_cases, id_vars=["FIPS","county","state","lat","long_"],
            var_name='dates',
            value_name="cases") 
df_cases_melted.tail()


# In[18]:





# In[ ]:


#1.What is the total number of reported COVID-19 cases in the USA?


# In[6]:


df_cases_melted['cases'].sum()


# In[ ]:


#2.What is the total number of reported COVID-19 cases for Virginia?


# In[7]:


df_Virginia = df_cases_melted[df_cases_melted.state == 'Virginia'].copy()
df_Virginia['cases'].sum()


# In[ ]:


#3. Provide a bar chart displaying the new reported COVID-19cases in Virginia over the last 10 days.


# In[8]:


df_Virginia.dates = pd.to_datetime(df_Virginia.dates)


# In[9]:


df_VA_last10days = df_cases_melted[(df_cases_melted.state == 'Virginia')&(df_Virginia.dates>"11/6/2021")]
df_VA_last10days


# In[10]:


df_VA_last10days.plot.bar()


# In[11]:


#4. Find the three Virginia counties with the highest reported COVID-19 cases in descending order.
Virginia_cases = df_Virginia[["county","cases"]]
VA_TOP3_counties = Virginia_cases['cases']
Virginia_cases


# In[35]:


subset = Virginia_cases[['county','cases']].groupby(['county']).sum()
TOP3 = subset.sort_values(['cases'],ascending=[0])
print(TOP3)
TOP3.head(3)


# In[13]:


#5. Find when each of the three Virginia counties (from problem 4) reported their highest 
    #number of new COVID-19 cases in a day.
#=> "Fairfax","Prince William", "Virginia Beach"
Fairfax_Cases = df_cases_melted[(df_cases_melted.state == 'Virginia')&(df_Virginia.dates>"11/6/2021")&(df_cases_melted.county == 'Fairfax')]
Fairfax_Cases
Fairfax_max = Fairfax_Cases.max()
print(Fairfax_max)


# In[14]:


Prince_William_Cases = df_cases_melted[(df_cases_melted.state == 'Virginia')&(df_Virginia.dates>"11/6/2021")&(df_cases_melted.county == 'Prince William')]
Prince_William_Cases
Prince_William_max = Prince_William_Cases.max()
print(Prince_William_max)


# In[15]:


Virginia_Beach_Cases = df_cases_melted[(df_cases_melted.state == 'Virginia')&(df_Virginia.dates>"11/6/2021")&(df_cases_melted.county == 'Virginia Beach')]
Virginia_Beach_Cases
Virginia_Beach_max = Virginia_Beach_Cases.max()
print(Virginia_Beach_max)


# In[ ]:


#6. Provide a figure with one subplot that shows three plotted lines - 
#one for each county from #problem 4. Each line represents the county’s total 
#reported COVID-19 cases over time.


# In[16]:


fig, ax = plt.subplots()
ax.plot(df_cases_melted[df_cases_melted.county == "Fairfax"].groupby(["dates"])["cases"].sum())
ax.plot(df_cases_melted[df_cases_melted.county == "Prince William"].groupby(["dates"])["cases"].sum())
ax.plot(df_cases_melted[df_cases_melted.county == "Virginia Beach"].groupby(["dates"])["cases"].sum())


# In[ ]:





# In[ ]:


#7. Find the total and average number of new COVID-19 cases reported in October 2021
#   for Fairfax,Virginia.


# In[17]:


Oct2021 = df_cases_melted[(df_cases_melted.county == 'Fairfax')&(df_Virginia.dates>="10/01/2021")&(df_Virginia.dates<="10/31/2021")]
Sum1 = Oct2021['cases'].sum()
mean = Oct2021['cases'].mean()

print("sum :", Sum1)
print("mean :",mean)


# In[ ]:


part02


# In[18]:


import fsspec
path = "https://github.com/babdelfa/gis/blob/main/counties_geometry.zip?raw=true"
with fsspec.open(path) as file:
    county = gpd.read_file(file)


# In[19]:


import fsspec
path1 = "https://github.com/babdelfa/gis/blob/main/state_geometry.zip?raw=true"
with fsspec.open(path1) as file1:
    state = gpd.read_file(file1)


# In[53]:


Virginia = state[state.STATE_NAME == 'Virginia']
Virginia

Counties = df_cases_melted.groupby(['FIPS','county',"state","lat","long_"])["cases"].max()
Counties = Counties.to_frame()
Counties.reset_index(inplace=True)
Counties = Counties[(Counties.state == 'Virginia')]
Counties = Counties.sort_values(by = 'cases', ascending=False)
Counties = Counties.head(3)
Counties

county = county.to_crs(epsg=4326)


gdf = gpd.GeoDataFrame(Counties,
                      crs="EPSG:4326",
                      geometry = gpd.points_from_xy(Counties.long_, Counties.lat))
df_county = gpd.sjoin(gdf,county)

fig, ax = plt.subplots()
Virginia.plot(ax=ax, color='darkgreen')
df_county.plot(ax=ax, column='cases', cmap='hot_r')#cmap 
contextily.add_basemap(ax, crs = 4326)
contextily.add_basemap(ax, crs=Virginia.crs.to_string())
plt.axis("off")
plt.title("Virginia County Case")


# In[ ]:





# In[ ]:




