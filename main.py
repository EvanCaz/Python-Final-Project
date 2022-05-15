################
# Evan Cazares
# Final
# Driver File
################
import sys
import functions as fn 
import pandas as pd

def main():

    # Things I have learned: 
    # I am not creative with varibale names and im getting confused with the amount of variables
    # I should plan out what I want to do before I do it, like a story board
    # I think I will lose points on num_rooms for not being effecient and on num_reviews for 
    # being repetitive and def on the length of the output of my code. In hindsight, I should have
    # had a outline and the functions should have returned something that I could print all in the
    # same line, like the x hotel has n reviews, n average score, n rooms, and n stars. Which if I 
    # were to start over I def think I could do.


    all_data = pd.read_csv(sys.argv[1])
    print("There are", len(fn.unique_hotels(all_data)), "unique hotels in this file.")
    print()
    print("There are", len(fn.tennis_star_hotels(all_data, True)), "Hotels with five stars and", len(fn.tennis_star_hotels(all_data, False)), "Hotels with tennis courts.")
    print()
    fn.hotel_average_stars(all_data)
    print()
    fn.num_reviews(all_data) 
    print()
    for key in fn.num_rooms_stars(all_data):
        print(key, "has", fn.num_rooms_stars(all_data)[key][0], "rooms and received", fn.num_rooms_stars(all_data)[key][1],"stars.")
    print()
    #for key in fn.num_stars(all_data):
        #print(key, "received", fn.num_stars(all_data)[key][0], "stars")
    
main()