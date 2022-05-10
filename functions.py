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
# number of 5 star hotels
# number of hotels with a tennis court
#
# Per Hotel Tasks:
# average score
# stars
# number of rewviews
# number of rooms

def unique_hotels(csv_file):
    # first created a list of all hotels with repeats
    # that is the first column in the file
    hotel_list = []
    all_hotels = csv_file["Name"]
    for index in all_hotels:
        # print(index)
        hotel_list.append(index)
    # use a set to create a list of free of duplicates
    unique_hotels = list(set(hotel_list))
    return unique_hotels

def best_hotel(csv_file):
    # find out hotels and their scores
    hotel_score = csv_file[["Name", "Score"]]
    print(hotel_score)


