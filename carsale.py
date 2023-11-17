#!/usr/bin/env python
# coding: utf-8

# Car Sales Analysis using Python

# In[1]:


#import the necessary libraries

import pandas as pd
import numpy as ns
import matplotlib.pyplot as plt
import seaborn as sns

import  warnings
warnings.filterwarnings('ignore')


# In[61]:


# import the dataset

data = pd.read_csv("C:/Users/MAYOWA/Downloads/archive (25)/Car_sales.csv")


# In[5]:


# check the head of data

data.head()


# In[7]:


#check the info of the data

data.info()


# In[8]:


#check for duplication

data.nunique()


# In[9]:


# check for missing value

data.isnull().sum()


# In[10]:


# cal the percentage of the missing value

(data.isnull().sum()/(len(data)))*100


# In[15]:


# fill in the missing value
data['__year_resale_value'].fillna(data['__year_resale_value'].median(), inplace = True)

data['Price_in_thousands'].fillna(data['Price_in_thousands'].mean(), inplace = True)
data['Curb_weight'].fillna(data['Curb_weight'].mean(), inplace = True)
data['Fuel_efficiency'].fillna(data['Fuel_efficiency'].mean(), inplace = True)
data['Power_perf_factor'].fillna(data['Power_perf_factor'].mean(), inplace = True)


# In[16]:


data.info()


# In[17]:


# How many manufacturers 

data['Manufacturer'].value_counts()


# In[28]:


#Total Sale Distribution by manufacturer

sale = data.groupby('Manufacturer')['Sales_in_thousands'].sum().reset_index()

sales_data = sale.sort_values(by='Sales_in_thousands', ascending = False)

plt.figure(figsize = (12,8))

sns.barplot(x ='Sales_in_thousands', y = 'Manufacturer' , data = sales_data)
plt.title('Sales of car by manufacturer')
plt.xlabel('Sales in thousand')


# In[49]:


# distribution of car sales
prices = data['Sales_in_thousands']

plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Car Prices')
plt.xlabel('Sales in thousand')
plt.ylabel('Frequency')
plt.show()


# In[62]:


#What is the distribution of the horsepower

data_py = data['Horsepower']

plt.figure(figsize=(10,6))
# sns.barplot(x='Horsepower', y='count', data=data_py)
plt.hist(data_py, bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Horsepower");
plt.xlabel('Horsepower')
plt.ylabel('Count')
plt.show()


# In[78]:


#relationship btw horsepower and model

# Create a box plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Engine_size', y='Vehicle_type', data=data)
plt.xlabel('Engine_size')
plt.ylabel('Vehicle_type')
plt.title('Relationship between Horsepower and Model')
plt.show()


# In[63]:


# Fuel Capacity by Vehicle type

plt.figure(figsize=(10, 6))
sns.boxplot(x='Vehicle_type', y='Fuel_capacity', data=data[['Vehicle_type', 'Fuel_capacity', 'Fuel_efficiency']
                                                          ])
plt.title('Fuel Capacity by Vehicle Type')
plt.xlabel('Vehicle Type')
plt.ylabel('Fuel Capacity')
plt.show()

