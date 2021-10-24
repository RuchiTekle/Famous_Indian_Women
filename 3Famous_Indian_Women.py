#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd

cwd = os.path.abspath('')
files = os.listdir(cwd)


# In[3]:


# Reading the csv file
Add_Data_1 = pd.read_csv('Additional_data_1.csv')
  
# saving xlsx file
AD1 = pd.ExcelWriter('Add_data_1.xlsx')
Add_Data_1.to_excel(AD1, index = False)
AD1.save()

# Reading the csv file
Add_Data_2 = pd.read_csv('Additional_data_2.csv')
  
# saving xlsx file
AD2 = pd.ExcelWriter('Add_data_2.xlsx')
Add_Data_2.to_excel(AD2, index = False)
AD2.save()


# In[4]:


AD = pd.DataFrame()

AD = AD.append(pd.read_excel(AD1), ignore_index=True) 
AD = AD.append(pd.read_excel(AD2), ignore_index=True) 

AD.head()
AD


# In[5]:


AD = AD.replace('\"',"",regex=True)
AD = AD.replace('\'',"",regex=True)
AD = AD.replace('\[',",",regex=True)
AD = AD.replace('\]',"",regex=True)
AD = AD.replace('\{',"",regex=True)
AD = AD.replace('\}',"",regex=True)
AD = AD.replace('\(',"",regex=True)
AD = AD.replace('\)',"",regex=True)
AD = AD.replace('Marriage|',"",regex=True)
AD = AD.replace('marriage|',"",regex=True)
AD = AD.replace('hlist|,,',"",regex=True)
AD = AD.replace('\|',",",regex=True)
AD = AD.replace('birth date and age|df|=|yes|',"",regex=True)
AD = AD.replace('Birth-date and age',"",regex=True)
AD = AD.replace('Birth date and age|',"",regex=True)
AD = AD.replace('death date and age',"",regex=True)


# In[6]:


AD


# In[8]:


AD.to_excel('Add_Data.xlsx', index=False)


# In[9]:


# reading the files
File1 = pd.read_excel("Famous Indian Women - Start Dataset.xlsx")


# In[10]:


File1


# In[11]:


# merging additional data with seed files
Merge_File = File1[["Full Name","Description","Job","Education Place","Native Language","Country","Father","Mother","Spouse",
               "Birth Date","Death Date","Birth Place","Death Place","Death Method",
               "Death Reason"]].merge(AD[["Full Name","Known for","Notable Work","Image","Website","Children","Native Name",
                                             "Signature","Title","Honours","Awards","Education","Birth Name","Nationality",
                                             "Weight","Height","Eye Color","Hair Color"]], on = "Full Name", how = "left")


# In[12]:


Merge_File


# In[13]:


Merge_File.to_excel("Add_plus_Original.xlsx", index = False)


# In[21]:


file_list=['Add_plus_Original.xlsx','Add_Row.xlsx']
  
main_dataframe = pd.DataFrame(pd.read_excel(file_list[0]))
  
for i in range(1,len(file_list)):
    data = pd.read_excel(file_list[i])
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe,df],axis=0)


# In[22]:


main_dataframe


# In[23]:


main_dataframe.to_excel("Final_Dataset.xlsx", index = False)

