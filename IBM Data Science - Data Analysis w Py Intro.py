#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)


# In[2]:


# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)


# In[3]:


df.head(10)


# In[4]:


# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
df.head(10)


# In[6]:


import numpy as np
df1=df.replace('?',np.NaN)


# In[7]:


df=df1.dropna(subset=["price"], axis=0)
df1.head(20)


# In[10]:


print(df.columns)


# In[11]:


df.to_csv("automobile.csv", index=False)


# <h2>Read/Save Other Data Formats</h2>
# 
# | Data Formate |        Read       |            Save |
# | ------------ | :---------------: | --------------: |
# | csv          |  `pd.read_csv()`  |   `df.to_csv()` |
# | json         |  `pd.read_json()` |  `df.to_json()` |
# | excel        | `pd.read_excel()` | `df.to_excel()` |
# | hdf          |  `pd.read_hdf()`  |   `df.to_hdf()` |
# | sql          |  `pd.read_sql()`  |   `df.to_sql()` |
# | ...          |        ...        |             ... |

# In[14]:


print(df.dtypes)


# In[16]:


df.describe()


# In[17]:


# describe all the columns in "df" 
df.describe(include = "all")


# In[22]:


temp = df[['length','compression-ratio']]
temp.describe()


# In[23]:


df.info()


# In[ ]:




