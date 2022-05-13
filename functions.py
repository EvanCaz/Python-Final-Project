################
# Evan Cazares
# Final
# Functions
################
import sys
import pandas as pd
import numpy as np

# Global Tasks:
# print unique hotels DONE
# hotel with the highest average review DONE
# number of 5 star hotels Done
# number of hotels with a tennis court Done
#
# Per Hotel Tasks:
# average score DONE
# stars
# number of rewviews
# number of rooms

def unique_hotels(csv_file):
    unique_hotels = list(csv_file["Name"].unique())
    return unique_hotels

def best_hotel(csv_file):
    hotel_score = csv_file[["Name", "Score"]]
    print(hotel_score)
    
def tennis_star_hotels(csv_file, FLAG=False):
    if FLAG == True:
        tennis_star = csv_file.query("Stars == '5'")["Name"].unique()
    # query returns all reviews in column stars with value 5, then unique 
    # removes all repeat reviews 
    if FLAG == False:
        tennis_star = csv_file.query("`Tennis court` == 'YES'")["Name"].unique()
    # google says add backticks for columns with spaces
    return tennis_star
    # No error checking for incorrect values in csv file
def hotel_stars(csv_file):
    all_hotels = unique_hotels(csv_file)
    score_dict = {}
    for hotel in all_hotels:
        one_hotel = csv_file.query("Name == @hotel")
        scores = one_hotel.query("Score in ['1', '2', '3', '4', '5']")["Score"]
        mean = scores.astype(int).mean()
        score_dict[hotel] = mean
        print("The average score for", hotel, "is", format(mean, '.4f'))
    print()
    print("The hotel with the highest average score is:",max(score_dict, key=score_dict.get))
    return 
def num_reviews(csv_file):
    a = unique_hotels(csv_file)
    print(type(a))
    b = a[0]
    reviews = csv_file.query("Name == @b")
    print(len(reviews))
    return

