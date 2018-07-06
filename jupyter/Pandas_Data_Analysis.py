
# coding: utf-8

# # Pandas Data Analysis
# 
# ### Here I analyze the dataset again using Pandas

# Importing the pandas and csv file readers and libraries so that I can read in a view my dataset in Python rather than as the file.

# In[1]:

import csv
import pandas as pd


# This code below simply shows me my dataset so that I know it imported correctly.

# In[2]:

faa_data_pandas = pd.read_csv("Pennsylvania_Condensed.csv") # Bringing in the Facebook message data
faa_data_pandas.head()


# Besides just seeing that I could properly display the data, I needed to make sure it imported the whole spreadsheet. By displaying the shape of the data I was able to see that all 6167 lines did in fact get imported. This also shows that all 25 rows did as well. 

# In[3]:

faa_data_pandas.shape


# This is how you pull out just one type. This case pulls out only the instances where the Airport_ID is true for KPHL, then displays just the first few rows. I did this just to test my ability to see just certain subsets of the data. This skill is helpful when analysing the data later in the project.

# In[4]:

# Create a new dataframe for the Airport ID (It does so by testing true/false on date equaling 2018-05-31)
faa_data_phil_pandas = faa_data_pandas[faa_data_pandas['AIRPORT_ID'] == "KPHL"]

print(faa_data_phil_pandas.shape)
faa_data_phil_pandas.head()


# This is the Pandas method for counting the instances of a categorical dataset, such as in this case airport id. This below counts the dataset and each time it finds a new value in the airport field it makes a counter for it, which goes up with each time it passes an occurance. This shows me which airport has more occurances of animal strikes.

# In[5]:

airport_count = faa_data_pandas['AIRPORT'].value_counts()
print(airport_count)


# For ease of importing to my DH project, I then exported this variable into its own spreadsheet so I could then import that into my HTML code.

# In[6]:

airport_count.to_excel('airport_count.xlsx')
print("Done Writing!")


# 

# As before with the airport, I repeated this process with animals. This way I could see which animal was struck more often and then split out the mammals from the birds manually since there were so few.

# In[7]:

species_count = faa_data_pandas['SPECIES'].value_counts()
print(species_count)


# Here I also exported this new variable of the count to an excel spreadsheet so that I could then import this to my html code.

# In[8]:

species_count.to_excel('species_output.xlsx')
print("Done Writing!")


# As with the species of animal and the airport I counted each datapoint of damage.

# In[9]:

damage_count = faa_data_pandas['DAMAGE'].value_counts()
print(damage_count)


# Since the letter code within the dataset does not really tell us much. I then took the output of the damage_count vaiable from just above and ran it through code to export the answers in a more human readable format.

# In[10]:

damage_lookup_dictionary = {"N": "None",
                            "M": "Minor",
                            "M?": "Unknown",
                            "S": "Substantial",
                            "D": "Destroyed",
                            "A": "Over $2,000,000 (Military)",
                            "B": "$500,000 to $2,000,000 (Military)",
                            "C": "$50,000 - $500,000 (Military)",
                            "E": "Less than $50,000 (Military)",
                            "": "No Damage Reported",}


# Here I then run the datase through this dictionary and display the count for each value and show it by the name of the 

# In[11]:

faa_data_pandas["DAMAGE"].value_counts().rename(index=damage_lookup_dictionary)


# Here I used the same methods to count the damage done at each phase of the flight. This way I could see at what point during the flight the planes make contact with the animals. Later I hope to do some more complex analysis of this portion of the data.

# In[12]:

flight_phase = faa_data_pandas['PHASE_OF_FLT'].value_counts()
print(flight_phase)


# For ease of importing to my website, I created a spreadsheet of just this variable counted.

# In[13]:

flight_phase.to_excel('flight_phase.xlsx')
print("Done Writing!")


# Here it counts the time of day. There is a time variable, but counting it would prve to be difficult since it is simply input as an integer. Therefore for now I just analyzed the 'time of day' field. I hope to late use the time field and give a more in depth look at the information.

# In[14]:

time_of_day = faa_data_pandas['TIME_OF_DAY'].value_counts()
print(time_of_day)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# While I have not done anything with this portion of the data analysis for the first draft of my project. I began analysing the data as amount of damage done to the aircraft at each airport. I hope to later normalize the data against flights at each location, then combine it with this analysis to see what airport has the most destructive animals at it. Though I lack current skills to normalize the dataset, so I just did the portion that I could for now.

# In[15]:

# Create a new dataframe for the Airport ID (It does so by testing true/false on date equaling 2018-05-31)
faa_data_minor_damage_pandas = faa_data_pandas[faa_data_pandas['DAMAGE'] == "M"]

print(faa_data_minor_damage_pandas.shape)
faa_data_minor_damage_pandas.head()


# In[16]:

faa_data_minor_damage_pandas['AIRPORT'].value_counts()


# In[17]:

# Create a new dataframe for the Airport ID (It does so by testing true/false on date equaling 2018-05-31)
faa_data_substantial_damage_pandas = faa_data_pandas[faa_data_pandas['DAMAGE'] == "S"]

print(faa_data_substantial_damage_pandas.shape)
faa_data_substantial_damage_pandas.head()


# In[18]:

# Create a new dataframe for the (It does so by testing true/false on date equaling 2018-05-31)
faa_data_destroyed_damage_pandas = faa_data_pandas[faa_data_pandas['DAMAGE'] == "D"]

print(faa_data_destroyed_damage_pandas.shape)
faa_data_destroyed_damage_pandas


# In[ ]:



