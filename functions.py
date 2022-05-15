################
# Evan Castars_listares
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
# stars DONE
# number of rewviews DONE
# number of rooms DONE

def unique_hotels(csv_file):
    unique_hotels = list(csv_file["Name"].unique())
    return unique_hotels
    
def tennis_star_hotels(csv_file, FLAG=False):
    if FLAG == True:
        tennis_star = csv_file.query("Stars == '5'")["Name"].unique()
    if FLAG == False:
        tennis_star = csv_file.query("`Tennis court` == 'YES'")["Name"].unique()
    return tennis_star

def hotel_average_stars(csv_file):
    all_hotels = unique_hotels(csv_file)
    score_dict = {}
    for hotel in all_hotels:
        one_hotel = csv_file.query("Name == @hotel")
        scores = one_hotel.query("Score in ['1', '2', '3', '4', '5']")["Score"]
        mean = scores.astype(int).mean()
        score_dict[hotel] = mean
        print("The average score for", hotel, "is", format(mean, '.4f'))
    print()
    print("The hotel with the highest average score is:",max(score_dict, key=score_dict.get, ))
    return 

def per_hotel_stats(csv_file):
    hotel_list =  unique_hotels(csv_file)
    star_rooms_reviews_score = []
    per_hotel = {}
    for hotel in hotel_list:
        one_hotel = csv_file.query("Name == @hotel")
        rooms_list = one_hotel["Rooms"].tolist()
        stars_list = one_hotel['Stars'].tolist()
        scores = one_hotel.query("Score in ['1', '2', '3', '4', '5']")["Score"]
        mean = scores.astype(int).mean()
        for value in stars_list:
            try:
                value = int(value)
            except:
                stars_list.remove(value)
        stars = list(set(stars_list))
        for value in rooms_list:
            try:
                value = int(value)
            except:
                rooms_list.remove(value)
        rooms = list(set(rooms_list))
        star_rooms_reviews_score = [len(one_hotel)] + rooms + stars + [mean]
        per_hotel[hotel] = star_rooms_reviews_score
    return per_hotel
        
    
