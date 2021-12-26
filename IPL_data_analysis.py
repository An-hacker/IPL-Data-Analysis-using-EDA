#!/usr/bin/env python
# coding: utf-8

# # **EDA on IPL Dataset**

# **Importing libraries**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# **Importing IPL dataset**

# In[2]:


data=pd.read_csv("matches.csv")
data.head(5)


# In[3]:


data.tail()


# **How big is the dataset? (Rows and columns)**

# In[4]:


data.shape


# In[5]:


data.info


# **Data Pre-processing: Finding out NaN values**

# In[6]:


data.isna().any()


# **Statistical Description of dataset**

# In[7]:


data.describe()


# **How many matches (in total) were played according to the dataset?**

# In[8]:


data['id'].count()


# **How many IPL seasons are we using to analyse?**

# In[9]:


data['Season'].unique()


# **Which IPL team won by scoring the maximum runs?**

# In[10]:


data.iloc[data['win_by_runs'].idxmax()]


# **Which IPL team won by consuming maximum wickets?**
# 

# In[11]:


data.iloc[data['win_by_wickets'].idxmax()]


# **Which IPL team won by taking minimum wickets?**
# 

# In[12]:


data.iloc[data['win_by_wickets'].idxmin()]


# **Which season consisted of the highest number of matches ever played?**

# In[13]:


fig_dims = (20, 4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='Season', ax=ax,data=data)
plt.show()


# **Which is the most successful IPL team with all the data at hand?**

# In[14]:


data1 = data.winner.value_counts()
sns.barplot(y = data1.index, x = data1)


# **What is the probability of winning a match if the toss was won?**

# In[15]:


probability_of_win = data['toss_winner'] == data['winner']

probability_of_win.groupby(probability_of_win).size()


# In[16]:


sns.countplot(probability_of_win)


# **Setting a higher row width**

# In[17]:


pd.set_option('max_rows', 99999)
pd.set_option('max_colwidth', 400)
pd.describe_option('max_colwidth')


# **Highest wins by teams per season**

# In[18]:


data.groupby('Season')['winner'].value_counts()


# In[19]:


data['toss_decision'].value_counts()


# **Man of the match - Highest to lowest (in won matches)**

# In[20]:


data['player_of_match'].value_counts()


# **In which city were the number of matches played?**

# In[21]:


data['city'].value_counts()


# 
# 
# ---
# 
# 
