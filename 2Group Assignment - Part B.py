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


url = ("https://en.wikipedia.org/wiki/Category:Indian_women_poets",
      "https://en.wikipedia.org/wiki/List_of_Indian_women_writers",
      "https://en.wikipedia.org/wiki/Category:Indian_women_television_journalists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_radio_presenters",
      "https://en.wikipedia.org/wiki/Category:Indian_women_editors",
      "https://en.wikipedia.org/wiki/Category:Indian_women_critics",
      "https://en.wikipedia.org/wiki/List_of_Indian_women_artists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_fashion_designers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_alpine_skiers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_archers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_athletes",
      "https://en.wikipedia.org/wiki/Category:Indian_female_badminton_players",
      "https://en.wikipedia.org/wiki/Category:Indian_women%27s_basketball_players",
      "https://en.wikipedia.org/wiki/Category:Indian_women_boxers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_chess_players",
      "https://en.wikipedia.org/wiki/Category:Indian_women_cricketers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_cyclists",
      "https://en.wikipedia.org/wiki/Category:Indian_female_divers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_fencers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_field_hockey_players",
      "https://en.wikipedia.org/wiki/Category:Indian_women%27s_footballers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_golfers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_artistic_gymnasts",
      "https://en.wikipedia.org/wiki/Category:Indian_female_handball_players",
      "https://en.wikipedia.org/wiki/Category:Indian_female_judoka",
      "https://en.wikipedia.org/wiki/Category:Indian_female_karateka",
      "https://en.wikipedia.org/wiki/Category:Indian_female_martial_artists",
      "https://en.wikipedia.org/wiki/Category:Indian_female_mountain_climbers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_rowers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_sailors_(sport)",
      "https://en.wikipedia.org/wiki/Category:Indian_female_skiers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_sport_shooters",
      "https://en.wikipedia.org/wiki/Category:Indian_female_sport_wrestlers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_squash_players",
      "https://en.wikipedia.org/wiki/Category:Indian_female_swimmers",
      "https://en.wikipedia.org/wiki/Category:Indian_female_table_tennis_players",
      "https://en.wikipedia.org/wiki/Category:Indian_female_tennis_players",
      "https://en.wikipedia.org/wiki/Category:Indian_women%27s_volleyball_players",
      "https://en.wikipedia.org/wiki/Category:Indian_female_weightlifters",
      "https://en.wikipedia.org/wiki/Category:Women_Indian_independence_activists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_in_war"
      "https://en.wikipedia.org/wiki/Category:Indian_women_activists"
      "https://en.wikipedia.org/wiki/Category:Indian_women%27s_rights_activists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_economists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_philanthropists",
      "https://en.wikipedia.org/wiki/Category:Indian_anthropologists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_academics",
      "https://en.wikipedia.org/wiki/Category:Indian_women_scholars",
      "https://en.wikipedia.org/wiki/Category:Indian_women_educational_theorists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_scholars",
      "https://en.wikipedia.org/wiki/Category:Indian_women_social_scientists",
      "https://en.wikipedia.org/wiki/Category:Indian_women_historians")

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


good_urls[:] = [x for x in good_urls if ":" not in x and "novel" not in x and "%" not in x and "List" not in x and "Main_Page" not in x and "India" not in x and "A_Burning" not in x and "Aalahayude_Penmakkal" not in x]
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


import wptools


# In[16]:


#Only = ['Aaditi_Pohankar','Aahana_Kumra']
Cum_info = []
for x in Only_good_urls:
    Add_data = wptools.page(x).get_parse()
    infobox = Add_data.data["infobox"]
    Cum_info.append(infobox)

print("Appended list is", Cum_info)
    


# In[62]:


len(Cum_info)


# In[63]:


Total_info=[]
for x in Cum_info:
    if x is not None:
        Total_info.append(x)


# In[64]:


len(Total_info)


# In[65]:


Total_info


# In[66]:


field_names = ['Full Name','Description',"Job","Country","Father","Mother","Spouse","Birth Date","Death Date","Birth Place",
               "Death Place","Death Reason","Known for","Notable Work","Image","Website","Children","Native Name","Signature",
               "Title","Honours","Awards","Education","Birth Name","Nationality","Weight","Height","Eye Color","Hair Color"]
    
to_ignore = [ "Education Place", "Native Language",'image_size', 'imagesize','image size','image_caption',
              'parents','relatives', 'family','relations' ,
               'years_active', 'yearsactive', 'years active', 'label', 'honorific_prefix',
               'caption','works', 
                'othername', 'other_names','other names', 'nickname',
               'alma_mater','alma mater', 'subject', 'pseudonym', 'period','patrons','burial_place', 'honorific_suffix',
               'restingplace','agent','style', 'pre-nominals', 'post-nominals', 
               'signature_alt','domesticpartner','gender', 'alternative spelling', 'related names', 'meaning', 'region','influences','1namedata1', '1blankname1', '1namedata', 'data1', 'blank1', '1blankname',
               'nominator','thesis_year', 'thesis_url','academic_advisors', 'regnal name', 
               'dynasty', 'house','main_interests','signature_size','subterm', 'suboffice3', 'suboffice',
               'subterm3', 'term8', 'subterm1', 'suboffice2', 'subterm2', 'office4', 'suboffice1',
              'honorary-prefix','image_upright','photo','era','pronunciation','credits','movement','Sister', 
               'medaltemplates', 'medal_templates', 'date_of_current_ranking', 'bwf_id', 'current_ranking', 'highest_ranking', 
               'date_of_highest_ranking', 'event','sport', 'peakrating', 'award1', 'yearpro', 'year1', 'status', 'prowins', 'evian', 
               'tour', 'otherwins', 'anainspiration', 'lpga', 'wbritopen', 'letwins', 'wusopen''clubs2', 'caps2', 'nationalteam1', 
               'nationalteam2', 'clubnumber', 'goals1', 'years2', 'nationalgoals1', 'nationalcaps2', 'clubs3', 'college1', 'caps1', 'years1', 
               'nationalyears1', 'years4', 'caps3', 'nationalgoals2', 'clubs1', 'position', 'years3', 'clubs4', 'ntupdate', 'nationalyears2',
               'nationalcaps1', 'currentclub', 'college2', 'goals3', 'club-update', 'goals2','wusopen', 'clubs2', 'handedness',
               'show', 'network','show-medals', 'classes','career_start', 'team','role', 'wctitles', 'team_starts', 
               'wcoveralls', 'totalpodiums', 'seasons', 'individual_starts', 'headercolor','succeeded','bowling', 'catches/stumpings2', 'odidebutyear', 
               'international', 'wickets3', 'bat avg1', 'matches2', 'matches1', 'best bowling3', 'tenfor3', 'testcap', 'lastodiagainst', 
               'batting', '100s/50s3', 'column1', '100s/50s2', '100s/50s1', 'runs1', 'T20Idebutagainst', 'lastodidate', 'deliveries1', 
               'lasttestyear', 'testdebutyear', 'wickets1', 'bowl avg2', 'top score1', 'lastT20Idate', 'lastT20Iagainst', 'column2', 
               'best bowling2', 'columns', 'best bowling1', 'catches/stumpings1', 'top score3', 'female', 'odidebutdate', 'fivefor1', 
               'top score2', 'odidebutagainst', 'testdebutdate', 'column3', 'deliveries2', 'fivefor3', 'runs2', 'runs3', 'catches/stumpings3',
               'bowl avg1', 'year', 'T20Idebutdate', 'T20Icap', 'testdebutagainst', 'bowl avg3', 'wickets2', 'bat avg3', 'fivefor2',
              'tenfor2', 'lastodiyear', 'T20Idebutyear', 'bat avg2', 'deliveries3', 'lasttestagainst', 'odicap', 'matches3', 'tenfor1', 
               'date', 'lastT20Iyear', 'lasttestdate', 'training','onetest','hidedeliveries','turnedpro', 'plays', 'updated','label_name',
              'order','order4', 'office7','career_end','heightinch', 'heightft','nationalteam-update','internationalspan', 'club1', 'T20Idebutfor',
               'lastT20Ifor','highestranking', 'collegeteam', 'universityteam', 'coach','term_start1', 'predecessor1', 'office1', 
               'term_end1', 'successor1', 'employer', 'party','residence','office', 'term_end', 'term_start', 
               'term_start2', 'term_end2', 'office2','constituency', 'predecessor','genre','organization','discipline','otherparty',
              'source','field', 'alt','module', 'philosophy', 'religion','term_start8', 'term_start7', 'term_start5', 'constituency7', 
               'governor4', 'office5', 'constituency8', 'successor4', 'term_end8', 'office8', 'term_end5', 'constituency5', 'constituency6',
               'term_start6', 'term_end6', 'office6', 'term_end4', 'term_start4', 'predecessor4', 'term_end7','language', 
               'origin','rank','singlesrecord', 'careerprizemoney', 'doublestitles', 'doublesrecord', 'highestsinglesranking', 'singlestitles', 
               'highestdoublesranking','playingstyle', 'equipment', 'club','OlympicsDoublesresult', 'WimbledonDoublesresult', 'AustralianOpenDoublesresult', 
               'currentsinglesranking', 'OthertournamentsDoubles', 'WimbledonMixedresult', 'USOpenresult', 'USOpenDoublesresult', 'AustralianOpenresult', 
               'Team', 'Wimbledonresult', 'FedCupresult', 'FrenchOpenDoublesresult', 'currentdoublesranking', 'FrenchOpenresult', 'work_institution',
              'main_discipline', 'notable_ascents','boards', 'Delhi Address', 'chairperson2','home_town','medaltemplates-expand',
              'retired', 'racquet','medals','league', 'number','cast','national_team', 'strokes','natlteam', 'level', 'played', 
               'year2', 'club2','current_ranking_date','nationalyears', 'nationalteam','paralympics','oneT20I','wickets4', 'top score4', 
               'catches/stumpings4', 'runs4', 'best bowling4', 'bat avg4', 'deliveries4', 'matches4', 'bowl avg4', '100s/50s4', 'club3', 
               'fivefor4', 'column4', 'tenfor4', 'year4', 'year3', 'club4','isbn', 'release_date', 'dewey', 'oclc', 'congress', 
               'author', 'publisher','start_discipline','honors','goals4', 'goals5', 'nationalteam3', 'caps5', 'caps4', 'years5', 
               'nationalgoals3', 'clubs5', 'nationalyears3', 'nationalcaps3','ethnicity','oneodi','spouse-type','iso2', 'notice', 
               'fam2', 'imagecaption', 'glotto', 'script', 'mapcaption', 'iso1', 'iso3', 'agency', 'speakers2', 'sign', 'fam5', 'ancestor2',
               'nation', 'fam4', 'fam3', 'ancestor', 'altname', 'dia1', 'familycolor', 'ancestor4', 'glottorefname', 'ancestor3', 'speakers',
               'states', 'map','rating', 'FideID','subjects', 'population', 'region10', 'languages', 'region2', 'region3', 'pop3', 
               'pop12', 'pop6', 'pop11', 'region9', 'pop9', 'region6', 'pop7', 'related', 'pop2', 'pop10', 'region1', 'region11', 'region7', 
               'pop1', 'region8', 'religions', 'region12', 'pop8', 'group','term','notes','recognition','honorific-prefix',
              'doctoral_students', 'doctoral_advisor', 'count', 'boxes','olympic', 'world', 'union','nationalyears4', 'nationalcaps4', 
               'nationalgoals4', 'nationalteam4','odishirt', 'odidebutfor','workplaces','hometown', 'headcoach', 'nationalcaps(goals)1',
              'WorldOpenresult','other_interests', 'life_partner','highschool', 'jersey', 'former_school(s)', 'height_in', 
               'height_ft','sub_discipline', 'lingua', 'ref', 'fam6', 'mapsize','genres','offices_held', 'ordained', 'church',
              'successor', 'appointer','fields','fetchwikidata','notice2', 'minority','place of burial', 'issue','reign-type', 'reign', 
               'succession','T20Ishirt','club5', 'club7', 'year6', 'club6', 'year5', 'year7','show_medals','nationalgoals5', 'nationalteam5',
               'nationalyears5', 'nationalcaps5','primeminister','thesis_title','hrank','honorific suffix','pb','youthclubs1',
              'boxrec', 'total', 'no contests', 'weight class', 'losses', 'KO', 'wins', 'draws', 'secondlady', 'order1', 'primeminister1', 
               'president1', 'term_label1', 'successor2', 'vicepresident2', 'order2', 'term_label2', 'predecessor2','visitor','institution',
              'battles', 'branch', 'allegiance', 'unit', 'commands','finals', 'activity_sector', 'formation', 'related_occupation', 
               'competencies', 'average_salary', 'type', 'employment_field', 'official_names','termend', 'termend2', 'termstart', 'termstart2',
              'Representing','final_ascent','youthyears1','resting_place', 'penname','1namedata2', '1blankname2','consort','best_result', 
               'disability_class', 'disability','literary_works','revived-category','FrenchOpenjuniorresult', 
               'Wimbledonjuniorresult', 'FrenchOpenDoublesjuniorresult', 'USOpenjuniorresult', 'USOpenDoublesjuniorresult', 
               'AustralianOpenDoublesjuniorresult', 'WimbledonDoublesjuniorresult','resides', 'trainer', 'billed', 'debut', 
               'names','title2', 'title1','Alma mater', 'worldchampion','weight_class','school_tradition','FrenchOpenMixedresult',
              'instrument','stance','notable_ideas','olympics','pub_date', 'pages', 'italic title','portaldisp','AustralianOpenjuniorresult',
               'majorascents','net_worth', 'module2','worlds', 'nationals','pcupdate', 'totalcaps', 'totalgoals','clubs6', 'clubs7',
              'congregations','founder','manageryears1', 'managerclubs1','textcolor','pen_name', 'institute', 'students',
              'beatified_by', 'beatified_place', 'honorific-suffix', 'canonized_by', 'feast_day', 'canonized_place', 
               'canonized_date', 'venerated_in', 'beatified_date', 'major_shrine', 'work_institutions','television','royal house','heightm','primeminister3', 'predecessor5', 'term_start3', 'predecessor6', 'primeminister2', 'office3', 
               'successor3', 'predecessor3', 'term_end3', 'successor6', 'width','Mixed','honorary prefix','major_works',
               'manageryears2', 'managerclubs2', 'manageryears3', 'managerclubs3','career_record','formercoach', 'Training Center',
              'constituency1','team1','glottoname', 'glottoname2', 'lc2', 'lc1', 'glotto2', 'ld1', 'ld2', 'glottorefname2',
               'coaching','testdebutfor', 'lastodifor', 'heightcm','subheader', 'verses','constituency3', 'constituency4',
              'pre-type2', 'reign-type2', 'reign2', 'succession2','term1','elected','cover_artist','repec_prefix', 'repec_id',
               'player name','OlympicMixedDoublesresult', 'WTAChampionshipsDoublesresult', 'USOpenMixedresult', 'mixedtitles', 
               'Olympicsresult', 'college', 'AustralianOpenMixedresult', 'Othertournaments', 'country_represented', 
               'OthertournamentsMixedDoubles','Commonwealth Games 2018','alias','term2','commonwealth Championship 2017',
               'media_type', 'native_lang1', 'native_lang1_name1','restingplacecoordinates','award2','termstart4', 
               'termstart3', 'constituency2','headquarters', 'abbreviation', 'location', 'region_served', 
                'competitions', 'guru','dumaurier', 'futwins', 'nabisco', 'extour','landscape', 'resting_place_coordinates',
              'paralympic', 'category', 'mgender','dissertation','years6','Siblings','image caption', 
               'clubnumber1', 'clubnumber2','URL','linglist', 'lingname','turned_pro','followed_by','preceded_by', 'isbn_note',
              'published','mma_loss', 'fighting_out_of', 'mma_subloss', 'sherdog', 'mma_koloss','known_Us','writings', 'partnerships', 
               'start_age','ChiefMinister4', 'Chief Minister2', 'term4', 'term3', 'Chief Minister3','realname','governor',
              'regionals', 'clubnumber3', 'clubnumber4','native_name_lang','nativename','country/region']
filtered_list = []

for x in Total_info:
    y = {key: value for (key, value) in x.items() if key not in to_ignore}
    filtered_list.append(y)


# In[67]:


len(filtered_list)


# In[68]:


filtered_list


# In[69]:


def rename_keys(filtered_list, keys):
    return dict([(keys.get(k), v) for k, v in filtered_list.items()])


# In[70]:


Correct_Keys = {'Full Name':'Full Name','fullname':'Full Name','full_name':'Full Name','full name':'Full Name','name':'Full Name','Description':'Description',"Job":"Job",
                'occupation':'Job','Occupation':'Job','profession':'Job',"Country":'Country',"country":"Country","Father":"Father",
                "father":'Father',"Mother":"Mother","mother":'Mother',"Spouse":"Spouse","spouse":'Spouse',"spouses":'Spouse',
                "spouse(s)":"Spouse","partner":"Spouse",'partner(s)':"Spouse","Birth Date":"Birth Date",'birthdate':"Birth Date",
                'birth_date':"Birth Date",'Birth Date':"Birth Date",'born':"Birth Date","Death Date":"Death Date",'death_date':"Death Date",
                "Birth Place":"Birth Place",'birth_place':"Birth Place","Death Place":"Death Place",'death_place':"Death Place",
                "Death Method":"Death Method", "Death Reason":"Death Reason",'death_cause':"Death Reason","Known for":"Known for",'known_for':"Known for",
                'known for':"Known for",'knownfor':"Known for","Notable Work":"Notable Work",'notablework':"Notable Work",'notable works':"Notable Work",
                'notable_works':"Notable Work",'notableworks':"Notable Work",'works':"Notable Work","Image":"Image",
                'image':"Image","Website":"Website","website":'Website',"Children":"Children","children":'Children',
                'native_name':"Native Name", 'nativename':"Native Name","Signature":"Signature",'signature':"Signature","Title":"Title",'title':"Title",'titles':"Title",
                'designation':"Title","Honours":"Honours",'honours':"Honours",'honors':"Honours","Awards":"Awards",
                'awards':"Awards",'prizes':"Awards","Education":"Education",'education':"Education","Birth Name":"Birth Name",
                'birth_name':"Birth Name",'birthname':"Birth Name","Nationality":"Nationality",'nationality':"Nationality",
                'citizenship':"Nationality","Weight":"Weight",'weight':"Weight",'weight_kg':"Weight","Height":"Height",'height':"Height",
                'height_cm':"Height",'height_m':"Height","Eye Color":"Eye Color",'eye_color':"Eye Color",
                'eye_colour':"Eye Color",'eyecolor':"Eye Color","Hair Color":"Hair Color",'hair_color':"Hair Color",
                'haircolor':"Hair Color",'hair_colour':"Hair Color",'haircolor':"Hair Color"}

Final_dataset = []

for a in filtered_list:
    
    Final_dataset.append(rename_keys(a,Correct_Keys))
 


# In[71]:


Final_dataset


# In[72]:


import csv

field_names = ["Full Name","Description","Job","Country","Father","Mother","Spouse","Birth Date","Death Date","Birth Place",
               "Death Place","Death Reason","Known for","Notable Work","Image","Website","Children","Native Name","Signature",
               "Title","Honours","Awards","Education","Birth Name","Nationality","Weight","Height","Eye Color","Hair Color"]

with open('Additional_data_2.csv', 'w',encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(Final_dataset)


# In[73]:


import pandas as pd
df = pd.read_csv("Additional_data_2.csv")
df.to_csv("Additional_data_2.csv", index = False)

