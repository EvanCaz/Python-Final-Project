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

    all_data = pd.read_csv(sys.argv[1])
    print("There are", len(fn.unique_hotels(all_data)), "unique hotels in this file.")
    print("These hotels are as follow... " "\n")
    for index in fn.unique_hotels(all_data):
        print(index)
    print()
    # print(fn.best_hotel(all_data))
    # skipping until I am sure what quetsion means
    # print(all_data.head(10))
    print("There are",fn.five_star_hotels(all_data, True), "five star hotels.")
    print("There are",fn.five_star_hotels(all_data, False), "hotels with a tennis court.")


main()