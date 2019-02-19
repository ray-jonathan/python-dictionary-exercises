from characters import characters
from houses import houses

import requests # makes API requests (this is a third-party module)
# import json # convert the API data into python dictionaries and arrays
import time # module for working with timestamps

# print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}


# print out the key names individually
# for each_dict in characters:
#     for key in each_dict:
#         if key == 'name':
#             print(characters[each_dict][key])



# How many characters names start with "A"?
def a_names_count (characters_dict):
    count = 0
    for person in characters_dict:
        name = person["name"]
        if name[0] == "A":
            count += 1
    return count
print("How many characters names start with \"A\"? %d" % a_names_count(characters))   

# How many characters names start with "Z"?
def z_names_count (characters_dict):
    count = 0
    for person in characters_dict:
        name = person["name"]
        if name[0] == "Z":
            count += 1
    return count
print("How many characters names start with \"Z\"? %d" % z_names_count(characters))  

# How many characters are dead?
def dead_names_count (characters_dict):
    count = 0
    for person in characters_dict:
        name = person["died"]
        if name != "":
            count += 1
    return count
print("How many characters are dead? %d" % dead_names_count(characters))  








# Who has the most titles?
def name_of_titles_count (characters_dict):
    count = 0
    most_names = ""
    for person in characters_dict:
        name = person["titles"]
        if len(name) > count:
            count = len(name)
            most_names = person["name"]
        
    return most_names
print("%s has the most titles." % name_of_titles_count(characters))  

#############################################
# Aquino's Answer: Who has the most titles? #
#############################################
def aquino_name_of_titles_count (characters_dict):
    most_titles = 0
    for person in characters_dict:
        num_titles = len(person["titles"])
        if num_titles > most_titles:
            most_titles = num_titles
            most_names = person["name"]

    # CHECK IF ANYONE ELSE HAS AS MANY TITLES
    other_most_titles = []
    for person in characters_dict:
        num_titles = len(person["titles"])
        if num_titles == most_titles:
            other_most_titles.append(person["name"])

    other_most_titles.append(most_names)
    return other_most_titles
print("%s has the most titles." % aquino_name_of_titles_count(characters))  

####################################################
# Aquino's Answer: Who has the most titles? PART 2 #
####################################################
def aquino_name_of_titles_count_2 (characters_dict):
    other_most_titles = 0
    # # # work in progress
    return other_most_titles
print("%s has the most titles." % aquino_name_of_titles_count_2(characters))  










# How many are Valyrian?
def valyrian_names_count (characters_dict):
    count = 0
    for person in characters_dict:
        name = person["culture"]
        if name == "Valyrian":
            count += 1
    return count
print("How many characters are Valyrian? %d" % valyrian_names_count(characters))  

# What actor plays "Hot Pie" (and don't use IMDB)?
def hot_pie_checker(characters_dict):
    for person in characters_dict:
        name = person["name"]
        if name == "Hot Pie":
            return person["playedBy"][0]
print("Who plays Hot Pie? %s" % hot_pie_checker(characters))  

# How many characters are *not* in the tv show?
def not_tv_names_count(characters_dict):
    count = 0
    for person in characters_dict:
        name = person["tvSeries"]
        if name == [""]:
            count += 1
    return count
print("How many characters are not in the TV series? %d" % not_tv_names_count(characters))  

# Produce a list characters with the last name "Targaryen"
def targaryen_names(characters_dict):
    targs = []
    for person in characters_dict:
        name = person["name"]
        if "Targaryen" in name:
            targs.append(person["name"])
    return targs
print("Who has Targaryen as a last name? %s" % targaryen_names(characters))

# Create a histogram of the houses (it's the "allegiances" key)
def allegiances_count(characters_dict, houses_dict):

    # Makes a list of all the house allegiances
    unabridged_houses_list = []
    for someone in characters_dict:
        someones_allegiance = someone["allegiances"]
        if someones_allegiance != []:
            unabridged_houses_list.append(someone["allegiances"])

    # Makes a dictionary, counting the frequency of each house (storing the count as the value-pair)
    freq = {} 
    for house_1 in unabridged_houses_list: 
        for house in house_1:
            if (house in freq): 
                freq[house] += 1
            else: 
                freq[house] = 1

    # Creates new dictionary with key reassignment from the houses.py dictionary
    new_freq = {}
    for old_key in freq:
        for key in houses:
            if old_key == key:
                new_freq[houses[key]] = freq[old_key]
    return new_freq

print("A histogram of how many people are in each house:")
print(allegiances_count(characters, houses))














###################
# AQUINO'S ANSWER #
###################

# # count the number of people who are part of a house
# def aquino_allegiances_count(characters_dict):
#     histogram = {}

#     # loop through all the people, check "allegiance"
#     for person in characters_dict:
#         allegiances_list = person["allegiances"]
#         for house in allegiances_list:

#     # check if it's already in the histogram, if so increment 1
#             if house in histogram:
#                 histogram[house] += 1
#             else:
#                 histogram[house] = 1

#     return histogram

# def pretty_print_histogram(histogram):
#     for house in histogram:
#         print("%s has %d members." % (house, histogram[house]))

# def translate_URL_to_house_name(URL):
#     house_name = ''
#     # go get the API's info on the house
#     r = requests.get(URL)
#     house_info = r.json() # JSON makes it human_legible
    
#     # filter out just the name
#     house_name = house_info['name']
#     return house_name

# def convert_to_nice_names(histogram):
#     nice_histogram = {}
#     for url_key in histogram:
#         house_name = translate_URL_to_house_name(url_key)
#         nice_histogram[house_name] = histogram[url_key]
#         time.sleep(0.1)
#     return nice_histogram

# ugly_histogram = aquino_allegiances_count(characters)
# pretty_histogram = convert_to_nice_names(ugly_histogram)

# pretty_print_histogram(pretty_histogram)








# Find all the married characters