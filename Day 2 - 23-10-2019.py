# Telangana State Ground Level Water Analysis using Python

# ---------------------------------------------------------------------------------------------------------------------------------------

# Section 1 - Data Reading 

# The following are the steps involved to read the data from .csv or ,excel 

# Starting a python programm by importing pandas

import pandas as pd

csv_path="C:\\Python\\Python37\\Project\\ts_wl_data.csv"

wl_df=pd.read_csv(csv_path) #dataframe 

# percentile list 

perc =[.20, .40, .60, .80] 
  
# list of dtypes to include - why?

include =['object', 'float', 'int'] 

wl_df

# --------------------------------------------------------------------------------------------------------------------------

# Section 2 - Data Cleaning

# The following are the steps which are involved in data cleaning i.e., cleaning NaN values and deleting unnecessary columns

#removing last column and cleaning for Na values 

wl_df_new={}
names=wl_df.keys()


for i in range(0,15):
    wl_df_new[names[i]]=wl_df[names[i]]

wl_df_new=pd.DataFrame(wl_df_new)


wl_df_new.dropna(inplace = True)  

# --------------------------------------------------------------------------------------------------------------------------

# Section 3 - Main Data Analysis Begins

# To know the column names of a dataframe

wl_df_new.keys() 

# Describing the data frame. It is a predefined function in python

# The below describe function gives us most of the frequency distribution statistics

desc = wl_df_new.describe(percentiles = perc, include = include) 

desc

# The following are the steps which are involved to analyze the data

wl_df_new[wl_df_new["district"]=="Adilabad"]

# .min() is used to find the minimum values of all the columns in a dataframe

wl_df_new[wl_df_new["district"]=="Adilabad"].min()


# finding the minimum value os a particular column in a dataset

wl_df_new[wl_df_new["district"]=="Adilabad"]["monsoon"].min()
 
# finding the exact location of a minimum value in a dataframe 
    
wl_df_new[wl_df_new["district"]=="Adilabad"]["monsoon"][wl_df_new[wl_df_new["district"]=="Adilabad"]["monsoon"]==-0.5]


# To get all the wlcodes of a dataframe and displaying it in a Table Format having count of it 

codes=wl_df_new["wlcode"].unique()
codes

codes_list=[]
obs_list=[]

# table code,observations using for loop

for code in codes:
    codes_list.append(code)
    obs_list.append(wl_df_new[wl_df_new["wlcode"]==code].shape[0])

codes_list,obs_list

# creating a new dictinary i.e., obs_df with code,observation as keys

obs_df = pd.DataFrame({'code': codes_list, 'observations': obs_list})

obs_df

# Finding out the max value of all the observation i.e., count of the wlcodes

maxv=obs_df["observations"].max()

# Displaying all the wlcodes with max. value as there observations
 
max_row=obs_df[obs_df["observations"]==maxv]

max_row

# -----------------------------------------------------------------------------------------------------------------------------

# Section 4 - Data Plotting sample 

# First matplot library to be imported 

get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt

# Steps involved in plotting data of a particular wlcode of a dataframe

station_code="W03811"

# To know the count of rows and columns of a particular wlcode

# select * into observation from wl_df_new where wl_df_new.wlcode = station_code - Corresponding SQL Statement

observation=wl_df_new[wl_df_new["wlcode"]==station_code]

observation.shape

plt.plot(observation["year_obs"],observation["monsoon"])
plt.figure()
plt.plot(observation["year_obs"],observation["premon"])
plt.figure()
plt.plot(observation["year_obs"],observation["pomrb"])
plt.figure()
plt.plot(observation["year_obs"],observation["pomkh"])

# ----------------------------------------------------------------------------------------------------------------------------

# Section 5 - Data Analysis

# printing the list of teh_name of telangana state

teh_name_list=wl_df_new["teh_name"].unique()

print(teh_name_list)

# selecting teh_name for particular station code

teh_name_df=wl_df_new["teh_name"][wl_df_new["wlcode"]==station_code].unique()

print(teh_name_df)

# selecting all the wlcodes for a particular teh_name

teh_name="Asifabad"

wlcodes=wl_df_new["wlcode"][wl_df_new["teh_name"]==teh_name].unique()
for i in wlcodes:
    print (i)

# Calicuating Sum and Average using for loop

for code in wlcodes:
    #To know the No. of observations for a particular wlcode in monsoon season
    wlcode_val=code
    wlcode_count=wl_df_new["monsoon"][wl_df_new["wlcode"]==wlcode_val].unique().shape
    print("No. of Observations :", wlcode_count)


    #To calculate the sum of the observations for a particular wlcode in monsoon season
    stn_sum = wl_df_new["monsoon"][wl_df_new["wlcode"]==wlcode_val].sum()
    print("Sum of the Observation :", stn_sum)


    #To calculate the average of the observations
    stn_avg = stn_sum / wlcode_count
    print("Average of the Observations ", stn_avg)


# average on groupby of wlcode and tehname

data=wl_df_new[["monsoon","premon","pomrb","pomkh","wlcode","year_obs","teh_name"]]

gdata=data.groupby(["teh_name","year_obs"])

# select teh_name,year_obs,count(*),avg(monsoon) from ts_wl_data1 group by teh_name,year_obs; - Corresponding SQL query

# Getting Mean using monsoon column

teh_agg=pd.concat([gdata[["monsoon","premon","pomrb","pomkh"]].mean(),gdata[["monsoon"]].count()],axis=1)

print(teh_agg)



