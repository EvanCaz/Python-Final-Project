################
# Evan Cazares
# Final
# Driver File
################
import sys
import functions as fn 
import pandas as pd

def main():
    # .head() reads the first specified rows of data in the file
    # varaible_name.iloc[] retunrs the infromation in a specifed row
    # varaible_name.iloc[1,1] returns information in row index, column index1
    # .tail() reads the last specified date in the file
    # .columns() prints all the columns, they are also specfied in the csv file at the top
    # variabel_name[''] or retunrs the specifc column, usuful for finding out all uniqe hotels in the file
    # variabel_name[['Name', 'other column', 'other column']] will return more than one column, does not have to be in the same order as csv file

    # things I have learned: 
    # I am not creative with varibale names and im getting confused with the amount of variables
    # I do not know how to do this without the Pandas library, i do not get strip() or any of those built in python methods
    # I should plan out what I want to do before I do it, like a story board


    all_data = pd.read_csv(sys.argv[1])
    print("There are", len(fn.unique_hotels(all_data)), "unique hotels in this file.")
    print("These hotels are as follow... " "\n")
    for index in fn.unique_hotels(all_data):
        print(index)
    print()
    print("There are", len(fn.tennis_star_hotels(all_data, True)), "Hotels with five stars.")
    print("There are", len(fn.tennis_star_hotels(all_data, False)), "Hotels with tennis courts.") 
    print()
    fn.hotel_average_stars(all_data)
    print()
    fn.num_reviews(all_data) 
    print()
    fn.num_rooms(all_data)
    
main()