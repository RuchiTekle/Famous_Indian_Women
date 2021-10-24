#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
import html5lib
import re
from bs4 import BeautifulSoup


# In[2]:


url = ("https://en.wikipedia.org/wiki/List_of_Indian_film_actresses",
      "https://en.wikipedia.org/wiki/Category:Indian_women_film_directors",
      "https://en.wikipedia.org/wiki/List_of_Indian_women_in_dance",
      "https://en.wikipedia.org/wiki/Category:Indian_women_classical_musicians",
      "https://en.wikipedia.org/wiki/Category:Indian_women_biologists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_academics")
cum_urls = []
for x in url:
    text = requests.get(x).text
    soup = BeautifulSoup(text, "html5lib")

    all_urls = [a["href"]
            for a in soup("a") if a.has_attr("href")]
    cum_urls.extend(all_urls)
    print(len(all_urls))
    print(len(cum_urls))


# In[3]:


cum_urls


# In[4]:


regex = r"^/wiki/.*"


# In[5]:


good_urls = [url for url in cum_urls if re.match(regex,url)]


# In[6]:


print(len(good_urls))


# In[7]:


good_urls


# In[8]:


good_urls[:] = [x for x in good_urls if ":" not in x and "%" not in x and "inema" not in x and "File" not in x and "List" not in x]
print(len(good_urls))
good_urls


# In[9]:


good_urls = list(set(good_urls))
print(len(good_urls))


# In[10]:


good_urls.sort()


# In[11]:


good_urls


# In[12]:


Only_good_urls = []
Only_good_urls = [x.replace("/wiki/", "") for x in good_urls]


# In[13]:


print(len(Only_good_urls))


# In[14]:


Only_good_urls


# In[15]:


pip install wptools


# In[16]:


import wptools


# In[17]:


Cum_info = []
for x in Only_good_urls:
    Add_data = wptools.page(x).get_parse()
    infobox = Add_data.data["infobox"]
    Cum_info.append(infobox)

print("Appended list is", Cum_info)
    


# In[18]:


len(Cum_info)


# In[19]:


Total_info=[]
for x in Cum_info:
    if x is not None:
        Total_info.append(x)


# In[20]:


len(Total_info)


# In[21]:


Total_info


# In[22]:


field_names = ['Full Name','Description',"Job","Country","Father","Mother","Spouse","Birth Date","Death Date","Birth Place",
               "Death Place","Death Reason","Known for","Notable Work","Image","Website","Children","Native Name","Signature",
               "Title","Honours","Awards","Education","Birth Name","Nationality","Weight","Height","Eye Color","Hair Color"]
    
    
to_ignore = ['image_size','imagesize','image size','image_caption','parents','partner','relatives','family','relations',
             'years_active','yearsactive','years active','honorific_prefix','caption','birth_name','birthname','citizenship',
             'othername','other_names','other names','alma_mater','alma mater','source','party','successor','constituency',
             'residence','competitions','alt','native_name_lang','module','budget','director','cinematography','gross',
             'producer','starring','screenplay','distributor','runtime','editing','writer','language','music','released',
             'studio','landscape','origin','genre','instrument','fields','predecessor','term_start','workplaces','office',
             'governor','chancellor','field','work_institutions','work_institution','notes','distributors','box_office_year',
             'produced_year','produced_total','profession','term_end','footnotes','primeminister','fetchwikidata','president',
             'office2','president1','term_start2','predecessor1','office1','term_end2','president2','successor2','predecessor2',
             'term_start1','agency','restingplacecoordinates','measurements','constituency2','otherparty','predecessor3',
             'term_end3','term_start3','successor3','constituency3','digits','number','check_digit','acronym','organization',
             'organisation','example','start_date','drives_on','population_density_km2','GDP_PPP','population_estimate_rank',
             'Gini_year','leader_name4','population_density_rank','lower_house','symbol_width','leader_name5','symbol_type',
             'national_motto','membership','calling_code','HDI','national_languages','other_symbol','government_type',
             'regional_languages','established_date2','leader_title5','iso3166code','established_event2','leader_title2',
             'englishmotto','sovereignty_note','area_rank','other_symbol_type','currency_code','HDI_year','image_map',
             'DST_note','area_sq_mi','population_density_sq_mi','religion','leader_title1','population_census_rank',
             'date_format','time_zone','conventional_long_name','leader_name2','HDI_rank','official_languages','cctld',
             'alt_map','population_census','largest_city','GDP_nominal_per_capita_rank','GDP_PPP_rank','map_caption',
             'GDP_nominal_rank','languages','HDI_change','map_width','population_estimate','GDP_PPP_per_capita_rank',
             'population_census_year','leader_title3','Gini','GDP_nominal','Gini_rank','image_coat','GDP_nominal_per_capita',
             'sovereignty_type','common_name','leader_name1','demonym','capital','upper_house','national_anthem','legislature',
             'utc_offset','GDP_PPP_year','population_estimate_year','established_date1','percent_water','coordinates',
             'currency','electricity','alt_coat','GDP_PPP_per_capita','languages_type','leader_name3','alt_flag','area_km2',
             'area_footnote','leader_title4','image_flag','GDP_nominal_year','religion_year','established_event1',
             'constituency1','predecessor7','constituency9','predecessor13','1blankname9','successor12','term_end1','term_end7',
             'predecessor12','1blankname11','successor4','predecessor4','governor4','term_start4','constituency12','1namedata5',
             'term_end14','constituency5','constituency7','term_end13','predecessor10','successor7','1blankname12','governor1',
             'successor13','term_start5','1namedata11','successor11','successor8','term_end6','1blankname10','office5',
             'successor10','1namedata8','governor3','term_start6','1blankname13','1blankname5','term_end11','term_start11',
             'office8','successor9','predecessor5','constituency6','1namedata10','1namedata7','1blankname14','1blankname6',
             'term_end10','1namedata14','governor2','1namedata6','term_end8','resting_place','term_start9','term_start13',
             'successor6','successor1','term_end4','successor5','predecessor6','term_end5','predecessor8','constituency11',
             'term_end12','office13','office6','term_end9','1namedata12','predecessor9','predecessor11','term_start10',
             '1namedata13','2blankname14','1blankname8','1namedata9','constituency10','term_start7','term_start8','2namedata14',
             'constituency4','term_start14','constituency8','term_start12','1blankname7','office14','thesis_title','termstart',
             'office3','television','doctoral_advisor','institution','alias','net_worth','background','philosophy',
             'literary_works','majority','homepage','employer','discipline','school_tradition','current_group','dances',
             'subject','pseudonym','period','patrons','burial_place','honorific_suffix','restingplace','agent','style',
             'pre-nominals','post-nominals','signature_alt','domesticpartner','gender','alternative spelling','related names',
             'meaning','region','influences','1namedata1','1blankname1','1namedata','data1','blank1','1blankname','nominator',
             'thesis_year','thesis_url','academic_advisors','regnal name','dynasty','house','main_interests','signature_size',
             'subterm','suboffice3','suboffice','subterm3','term8','subterm1','suboffice2','subterm2','office4','suboffice1',
             'honorary-prefix','image_upright','photo','era','pronunciation','credits','movement','Sister','label','nickname']

filtered_list = []

for x in Total_info:
    y = {key: value for (key, value) in x.items() if key not in to_ignore}
    filtered_list.append(y)


# In[23]:


len(filtered_list)


# In[24]:


filtered_list


# In[25]:


def rename_keys(filtered_list, keys):
    return dict([(keys.get(k), v) for k, v in filtered_list.items()])


# In[26]:


Correct_Keys = {'Full Name':'Full Name','full name':'Full Name','name':'Full Name','Description':'Description',"Job":"Job",
                'occupation':'Job','Occupation':'Job','profession':'Job',"Country":'Country',"country":"Country","Father":"Father",
                "father":'Father',"Mother":"Mother","mother":'Mother',"Spouse":"Spouse","spouse":'Spouse',"spouses":'Spouse',
                "spouse(s)":"Spouse","partner":"Spouse",'partner(s)':"Spouse","Birth Date":"Birth Date",
                'birth_date':"Birth Date",'born':"Birth Date","Death Date":"Death Date",'death_date':"Death Date",
                "Birth Place":"Birth Place",'birth_place':"Birth Place","Death Place":"Death Place",'death_place':"Death Place",
                "Death Reason":"Death Reason",'death_cause':"Death Reason","Known for":"Known for",'known_for':"Known for",
                'known for':"Known for","Notable Work":"Notable Work",'notable works':"Notable Work",
                'notable_works':"Notable Work",'notableworks':"Notable Work",'works':"Notable Work","Image":"Image",
                'image':"Image","Website":"Website","website":'Website',"Children":"Children","children":'Children',
                'native_name':"Native Name","Signature":"Signature",'signature':"Signature","Title":"Title",'title':"Title",
                'designation':"Title","Honours":"Honours",'honours':"Honours",'honors':"Honours","Awards":"Awards",
                'awards':"Awards",'prizes':"Awards","Education":"Education",'education':"Education","Birth Name":"Birth Name",
                'birth_name':"Birth Name",'birthname':"Birth Name","Nationality":"Nationality",'nationality':"Nationality",
                'citizenship':"Nationality","Weight":"Weight",'weight':"Weight","Height":"Height",'height':"Height",
                'height_cm':"Height",'height_m':"Height","Eye Color":"Eye Color",'eye_color':"Eye Color",
                'eye_colour':"Eye Color",'eyecolor':"Eye Color","Hair Color":"Hair Color",'hair_color':"Hair Color",
                'haircolor':"Hair Color",'hair_colour':"Hair Color",'haircolor':"Hair Color"}

Final_dataset = []

for a in filtered_list:
    
    Final_dataset.append(rename_keys(a,Correct_Keys))
 


# In[27]:


Final_dataset


# In[28]:


import csv

field_names = ['Full Name','Description',"Job","Country","Father","Mother","Spouse","Birth Date","Death Date","Birth Place",
               "Death Place","Death Reason","Known for","Notable Work","Image","Website","Children","Native Name","Signature",
               "Title","Honours","Awards","Education","Birth Name","Nationality","Weight","Height","Eye Color","Hair Color"]

with open('Additional_data_1.csv', 'w',encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(Final_dataset)


# In[29]:


import pandas as pd
df = pd.read_csv("Additional_data_1.csv")
df.to_csv("Additional_data_1.csv", index = False)

