################
# Evan Cazares
# Final
# Functions
################
import pandas as pd

def unique_hotels(csv_file):
    unique_hotels = list(csv_file["Name"].unique())
    return unique_hotels
    
def tennis_star_hotels(csv_file, FLAG=False):
    if FLAG == True:
        tennis_star = csv_file.query("Stars == '5'")["Name"].unique()
    if FLAG == False:
        tennis_star = csv_file.query("`Tennis court` == 'YES'")["Name"].unique()
    return tennis_star

def per_hotel_stats(csv_file):
    hotel_list =  unique_hotels(csv_file)
    star_rooms_reviews_score = []
    per_hotel = {}
    for hotel in hotel_list:
        one_hotel = csv_file.query("Name == @hotel")
        scores = one_hotel.query("Score in ['1', '2', '3', '4', '5']")["Score"]
        mean = scores.astype(int).mean()
        rooms_list = one_hotel["Rooms"].tolist()
        stars_list = one_hotel['Stars'].tolist()
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