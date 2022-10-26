#!/usr/bin/env python
# coding: utf-8

# In[2]:


import xarray as xr
import numpy as np 
import pandas as pd


# In[3]:


#load water eden water depth data 2021 q3
ds = xr.open_dataset ("C:/Users/ihasan2020/Desktop/2011_q3_depth_v3.nc")
da =ds ["depth"]
da


# In[4]:


#variables are in our dataset
ds.data_vars


# In[5]:


#monthly_data = ds.resample (freq = 'm', dim = 'time', how = 'mean')


# In[6]:


#look at the NetCDF representation 
ds.info()


# In[7]:


#slelect one variable and pick the first entry along the first axis (time)
ds.depth [0]


# In[8]:


#plot depth of one date 
ds.depth [0].plot()


# In[10]:


#dataset dimensions
ds.dims


# In[11]:


#dataset coordinates
ds.coords


# In[12]:


#The actual (numpy) arrray
ds.depth.data


# In[13]:


#Looking at the attribute 
ds.attrs


# In[24]:


#demonstrating customised time-seris data  
ds.sel(time= slice("2021-07-01","2021-08-30"))
       


# In[25]:


#performing arithmetic operation on the data set (+)
da + 1.5


# In[26]:


da_mean =da.mean(dim="time")
da_mean


# In[27]:


#Calculating standard deviation of water depth and ploting across time 

da.std (dim =["y","x"]).plot()


# In[31]:


#compute monthly mean depth
m_mean = ds.groupby("time.month").mean()
m_mean


# In[29]:


#Calculating median vlaue of water depth and ploting across time 
da.median (dim =["y","x"]).plot()


# In[34]:


#Resample to 5days mean (experimental)
ds.depth.resample (time ="5D").mean()


# In[47]:


#resample to tri_monthly mean uisng data form 2021-07-01 to 2021-09-30
F_mean = ds.depth.resample (time ="3MS").mean().plot()
F_mean


# In[48]:


#for exportable file 
F_mean = ds.depth.resample (time ="3MS").mean()
F_mean


# In[50]:


#Exporting final mean of water deapth data as.nc format to import in ArcMap
F_mean.to_netcdf("C:/Users/ihasan2020/Desktop/watrDpt_mean.nc")


# In[ ]:




