################
# Evan Cazares
# Final
# Functions
################
import sys
import pandas as pd

# Global Tasks:
# print unique hotels DONE
# hotel with the highest average review
# number of 5 star hotels DONE
# number of hotels with a tennis court DONE
#
# Per Hotel Tasks:
# average score
# stars
# number of rewviews
# number of rooms

def unique_hotels(csv_file):

    unique_hotels = csv_file["Name"].unique()
    return unique_hotels

def best_hotel(csv_file):
    # find out hotels and their scores
    hotel_score = csv_file[["Name", "Score"]]
    print(hotel_score)
    #skiiping as i am not sure specifcally what i am supposed to do
    
def tennis_star_hotels(csv_file, FLAG=False):
    if FLAG == True:
        determinate = "5"
        lists = list(csv_file["Stars"])
    else:   
        lists = list(csv_file["Tennis court"])
        determinate = "YES" 
    counter = 0
    for index in lists:
        if index == determinate:
            counter += 1
    return counter
def hotel_stars(csv_file):
    hotels_stars = csv_file.iloc[1, 1]
    return hotels_stars


