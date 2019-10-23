#!/usr/bin/env python
# coding: utf-8

# # Telangana Water level : Pandas analysis

# In[48]:


import pandas as pd 

csv_path="C:\\Python\\Python37\\Project\\ts_wl_data.csv"

wl_df=pd.read_csv(csv_path) #dataframe 

# percentile list 
perc =[.20, .40, .60, .80] 
  
# list of dtypes to include 
include =['object', 'float', 'int'] 

get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# In[7]:


#removing last column and cleaning for Na values 
wl_df_new={}
names=wl_df.keys()

for i in range(0,15):
    wl_df_new[names[i]]=wl_df[names[i]]
wl_df_new=pd.DataFrame(wl_df_new)

wl_df_new.dropna(inplace = True)  


# In[8]:


#COLUMN NAMES
wl_df_new.keys()


# In[5]:


# DESCRIBE ON BASIC DATA FRAME
desc = wl_df_new.describe(percentiles = perc, include = include) 


# In[6]:


desc


# In[27]:


# Main ground water data - PER STATION ssample

STATION_CODE="W17699"

station_data=wl_df_new[wl_df_new["wlcode"]==STATION_CODE]

print(f"Number of rows in the station code {STATION_CODE} is {station_data.shape[0]}")

station_data


# In[41]:


# to get maximum observations on station 

# first get all the station codes
codes=wl_df_new["wlcode"].unique()

codes_list=[]
obs_list=[]

#table code,observations
for code in codes:
    codes_list.append(code)
    obs_list.append(wl_df_new[wl_df_new["wlcode"]==code].shape[0])

# codes_list,obs_list
obs_df = pd.DataFrame({'code': codes_list, 'observations': obs_list})

maxv=obs_df["observations"].max()

max_row=obs_df[obs_df["observations"]==maxv]


    
    




# In[ ]:


#to plot year wise monsoon ground water level 

station_code="W03811"

observation=wl_df_new[wl_df_new["wlcode"]==station_code][]

observation.shape

# total=[]
# for teh in teh_list:
#     total+=observation["monsoon"]



plt.plot(observation["year_obs"],observation["monsoon"])
plt.figure()
plt.plot(observation["year_obs"],observation["premon"])
plt.figure()
plt.plot(observation["year_obs"],observation["pomrb"])
plt.figure()
plt.plot(observation["year_obs"],observation["pomkh"])




# In[ ]:




