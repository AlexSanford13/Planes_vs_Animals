
# coding: utf-8

# # FAA Data Analysis: Take 1
# ### This is a test analysis from the Hack Day
# 

# These first two cells import the file using the CSV loader. This is a much simpler way to load it and parse the data using a tool to understand the CSV file. If I were to manually import this data, I would not as easily be able to parse through this. Using these methods I will be using a tool that much more readily can read the CSV file and show me the outputs I am looking for.

# In[1]:

import csv # Load up the CSV module


with open('Pennsylvania_Condensed.csv') as file_handler:
    reader = csv.DictReader(file_handler)     # Load the file into the CSV module
    animal_strike_dict = [row for row in reader] # Read all the data into a variable as a list

animal_strike_dict[0:1]


# ## Counting the species hit by plane as a dictionary
# 
# The folllowing Cell counts through each Species in the Species column of the CSV File. This will count and add the count to my created dictionary for each new value found. It will be unordered (shows up how it counts it in as it is found within the file). I imported this from the Dictionary import, rather than the list import since I can access the column by name within the header. THis allows me to not have to count the column, but rather name it.

# In[2]:

# Create a dictionary to store the animals struck
species_counter = dict()


for row in animal_strike_dict:
    animal = row['SPECIES']
    if animal not in species_counter:
        species_counter[animal] = 1
    else:
        species_counter[animal] += 1

print(species_counter)


# In[4]:

species_csv = open('species_csv.csv', 'w')
with species_csv:
    writer = csv.writer(species_csv)
    writer.writerows(species_counter)

print("Write Complete")


# Below is more cells creating dictionaries for a variety of the columns in the CSV file. It is being read as the list within the dictionary.

# In[5]:

# Create a dictionary to store the part of the flight in which the animal was struck
flight_phase = dict()


for row in animal_strike_dict:
    phase = row['PHASE_OF_FLT']
    if phase not in flight_phase:
        flight_phase[phase] = 1
    else:
        flight_phase[phase] += 1

print(flight_phase)


# In[6]:

# Create a dictionary to store the airport where the strike happened
airport_count = dict()


for row in animal_strike_dict:
    airport = row['AIRPORT']
    if airport not in airport_count:  # makes the rule that creates the new value if it doesn't exist
        airport_count[airport] = 1
    else: # counts up if the value already exists
        airport_count[airport] += 1

print(airport_count)


# Below, I created a dictionary that would import the amount of damage done. This loops over the dataset and adds up the total amount of reported data on each type. 

# In[7]:

damage_counter_dictionary = dict()

for row in animal_strike_dict: # Chooses the Damage Cell
    damage = row['DAMAGE']
    if damage not in damage_counter_dictionary:
        damage_counter_dictionary[damage] = 1
    else:
        damage_counter_dictionary[damage] += 1

print(damage_counter_dictionary)


# Next, I imported and then created a counter that would count using that method. This was for the same output, but would in the end create a more interesting way to analyze the data

# In[8]:

from collections import Counter

damage_counter = Counter() # Empty counter for damage

for row in animal_strike_dict:
    damage_counter.update(row['DAMAGE'])
    
damage_counter


# Here I took the key of damage done within the dataset, here I mapped it to the letter in the key. This way I can then show the data by how much damage was done in terms that would be understandable by people

# In[9]:

#Creating the Data Dictionary from the Key on the FAA Website
damage_lookup_dictionary = {"N": "not any",
                            "M": "minor",
                            "M?": "unknown",
                            "S": "substantial",
                            "D": "destroyed",
                            "A": "over $2,000,000 (Military)",
                            "B": "$500,000 to $2,000,000 (Military)",
                            "C": "$50,000 - $500,000 (Military)",
                            "E": "less than $50,000 (Military)",
                            "?": "an unreported amount",}


# Finally, I took the key and displayed each output in a sentence form. I took the counter and the keys created int he cells above and created strings as outputs. These strings would take the vaiables of each information to show them in a sentence so that we could easily read and understand it.

# In[10]:

for damage_key in damage_counter:
    damage_count = damage_counter[damage_key] # Creates Vaiable for the count
    damage_name = damage_lookup_dictionary[damage_key] # Creats variable for the key
    print("There was {} damage done to {} aircraft".format(damage_name, damage_count))


# Here I take the same method of creating a dictionary of the count of each animal that was struck by a plane. THis is in dictionary form, so it isn't as mutable,.

# In[11]:

species_counter_dictionary = dict()

for row in animal_strike_dict: # Chooses the Damage Cell
    species = row['SPECIES']
    if species not in species_counter_dictionary:
        species_counter_dictionary[species] = 1
    else:
        species_counter_dictionary[species] += 1

print(species_counter_dictionary)


# Here I attempted to count the number of each animal that was hit by the plane. This was difficult. My first error is displayed here.
# 
# 
# ````
# ValueError                                Traceback (most recent call last)
# <ipython-input-66-c51fc6875d37> in <module>()
#       4 
#       5 for row in animal_strike_dict:
# ----> 6     species_counter.update(row['SPECIES'])
#       7 
#       8 species_counter.most_common() # Displays the counter
# 
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
# ````
# 
# After some troubleshooting I found that the error was misnaming the species_counter counter in the beginning of the for loop. This returned an error telling me that it was problematic
# 
# 
# Below, I fixed the issue but it was counting by letter, not by value.

# In[12]:

from collections import Counter # Imports the counter 

species_counter = Counter() # Empty counter creator

for row in animal_strike_dict:
    species_counter.update(row['SPECIES'])
    
species_counter # Displays the counter


# I took this code and both the dictionary and the list version and put them in a new notebook, and got the same issues.
# 
# After discssing it and some troubleshooting, then seeing the issues it was a problem of mixing the more Pythonig and less Pythonic is the issue. In the previous iterations it was looking at each string as a new list and then computing the numbers one letter at a time. This next block of code is used to actually read through the strings as a whole and then count each as a string not as a letter.

# In[13]:

from collections import Counter # Imports the counter 

species_counter = Counter([row['SPECIES'] for row in animal_strike_dict]) # Empty counter creator

    
species_counter.most_common() # Displays the counter


# In[14]:

species_csv = open('species_csv.csv', 'w')
with species_csv:
    writer = csv.writer(species_csv)
    writer.writerows(species_counter)

print("Write Complete")


# The below code is for counting the months. I attempted to use the same methods as above, so continuing to just practice this using counters and different variables to see how things change. This is dont using both just a counter and displaying them in order of month. This will give a picture of the chronological timeline of the strikes by month.

# In[15]:

from collections import Counter

month_counter = Counter() # Empty counter for damage

for row in animal_strike_dict:
    month_counter.update(row['INCIDENT_MONTH'])
    
month_counter


# In[16]:

#Creating the Data Dictionary from the Key on the FAA Website
month_lookup_dictionary = {"1": "January",
                            "2": "February",
                            "3": "March",
                            "4": "April",
                            "5": "May",
                            "6": "June",
                            "7": "July",
                            "8": "August",
                            "9": "September",
                            "10": "October",
                            "11": "November",
                            "12": "December",
                            "0": "Not Known"}


# Below is taking the code dictionary and counter displayed abot to see the data and then output sentences to more easily read. These are displayed in order they were added to the list, so there is not a real order. I am hoping to find a way to order these sentences so I can see them in order of either time within the year, or to organize by number of strikes per month.

# In[17]:

for month_key in month_counter:
    month_count = month_counter[month_key] # Creates Vaiable for the count
    month_name = month_lookup_dictionary[month_key] # Creats variable for the key
    print("In {} there were {} animal strikes".format(month_name, month_count))


# I hope to use these tools and eventualy expand it to see per month over time. So maybe see if certain years are more frequent and if the pattern is generally seen throught this framework. I hope to maybe graph these points and see over the three decades within the data set to see the change over time.

# Below is a counter that imports the infomration from month an then counts each incident by month. It then sorts these by most to least frequent months.

# In[18]:

from collections import Counter # Imports the counter 

month_counter = Counter([row['INCIDENT_MONTH'] for row in animal_strike_dict]) # Empty counter creator

    
month_counter.most_common() # Displays the counter

