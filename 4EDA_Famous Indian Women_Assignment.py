#!/usr/bin/env python
# coding: utf-8

# In[1]:


#We first import the packages that we would need for this case study
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
import math
import datetime
from collections import Counter
from collections import OrderedDict
warnings.filterwarnings('ignore')
sns.set_palette('Set2')
sns.set_style('darkgrid')


# In[2]:


#Reading in data and looking at the number of rows and columns using shape 
data= pd.read_excel('/Users/Apurva/OneDrive/ISB/Final_Dataset.xlsx')
data.shape


# In[3]:


data.head()


# In[4]:


data.head(20)


# In[5]:


data.shape


# In[6]:


data.dtypes


# In[7]:


data.describe()


# In[8]:



timestamp = datetime.datetime.fromtimestamp(1500000000)
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))


# In[9]:


data_NA = pd.DataFrame(data=[data.isna().sum().tolist(), ["{:.2f}".format(i)+'%' for i in (data.isna().sum()/data.shape[0]*100).tolist()]], 
            columns=data.columns, index=['NA Count', 'NA Percent']).transpose()
data_NA.style.background_gradient(cmap="summer", subset=['NA Count'])


# ### Analysis of Missing Data
# From the above table we could analyze that fields including Full name,Description, Job, Country, birth date and birth place have minimum missing value and data lies between 100-70% 

# In[10]:


data_death = data[~data['Death Date'].isna()].reset_index(drop=True)
plt.rcParams['font.size'] = 10
plt.figure(figsize=(10,6))
sns.countplot(x='Death Method', data=data_death, order=data_death['Death Method'].value_counts().index[:4])
plt.ylabel('Women Count', weight='bold', fontsize=16)
plt.xlabel('Method of Death', weight='bold', fontsize=16)
plt.show()


# In[11]:


fig, ax  = plt.subplots(figsize=(16, 8))
fig.suptitle('Death Methods', size = 20, color = "black")
explode = ( 0.05, 0.3, 0.05, 0.05, 0.05)
labels = ["Natural Causes","Sucide","Homicide","Accident","Murdered"]
sizes = data["Death Method"].dropna().value_counts()
ax.pie(sizes, explode=explode, colors=sns.color_palette("Pastel1"), startangle=60, labels=labels,autopct='%1.0f%%', pctdistance=0.9)
ax.add_artist(plt.Circle((0,0),0.4,fc='white'))
plt.show()


# ### Analysis of Death Method
# Based on available data, Natural cause (59%) is the main reason of death followed by suicide (18%), homicide (16%) and accident (6%) 

# In[12]:


sns.set_theme(style="whitegrid")

used_networks = [2,13,14]

df = data.iloc[:,used_networks].value_counts(). rename_axis(['Job','Death Method','Death Reason']).reset_index(name='counts')[:15]


# Draw each cell as a scatter point with varying size and color
g = sns.relplot(
    data=df,
    x="Job", y="counts",
    hue="Death Method", size="Death Reason",
    palette='Pastel1', sizes=(10, 500),alpha=1,height=8,aspect=1
)

plt.xticks(rotation=90)
g.set(ylabel="",title="Connection Between Occupation and Death")
g.despine(left=True, bottom=True);


# ### Analysis on Connection Between Occupation & Death (reason & method)
# In the above analysis the color depicts the death method while size of circle depicts the death reason
# Xaxis is the occupation/job and y axis is count of women died

# In[13]:


plt.rcParams['font.size'] = 12
plt.figure(figsize=(12,10))
sns.countplot(y='Job', data=data, order=data['Job'].value_counts().index[:15])
plt.xlabel('Women Count', weight='bold', fontsize=20)
plt.ylabel('Occupation', weight='bold', fontsize=20)
plt.show()


# ### Analysis of Job/Occupation
# Our dataset includes maximum women from Film Industry followed by Politicians 

# In[14]:


dict_ = Counter(data['Description'].value_counts().to_dict())
dict_ = dict(dict_.most_common(5))

plt.figure(figsize=(7,7))
plt.pie(x=dict_.values(), labels=dict_.keys(), autopct='%1.1f%%', shadow=True, startangle=45)
plt.show()


# ### Analysis on Profession/Description
# Similar to occupation/job, even profession/description depicts the same picture i.e. 55% of dataset is from film industry followed by 23.5% from politics

# In[15]:


plt.rcParams['font.size'] = 10
plt.figure(figsize=(12,10))
sns.countplot(y='Country', data=data, order=data['Country'].value_counts().index[:20])
plt.xlabel('Women Count', weight='bold', fontsize=20)
plt.ylabel('Country', weight='bold', fontsize=20)
plt.xscale('log')
plt.show()


# ### Analysis on Country
# As our domain is Famous Indian Women, we have included maximum details of women who are based at India. Other countries included in dataset are US,UK, Australia, Pakistan, Germany, Switzerland etc.

# In[16]:


Final=data.copy()
Topjobs = ["Actor","Film Actor","Politician","Singer"]
TopDeaths = ["Natural Causes","Suicide","Accident","Homicide"]
Final=Final[Final["Job"].isin(Topjobs)]
Final=Final[Final["Death Method"].isin(TopDeaths)]

