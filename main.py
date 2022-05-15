################
# Evan Cazares
# Final
# Driver File
################
import sys
import functions as fn
import pandas as pd

char_format = 25
num_format = 4
def main():
    try:
        if len(sys.argv) != 2:
            print("Did not enter a file")
            sys.exit()
        else:
            all_data = pd.read_csv(sys.argv[1])
    except FileNotFoundError or IndexError:
        print("Incorrect file input")
        sys.exit()
    print("There are", len(fn.unique_hotels(all_data)), "unique hotels in this file.")
    print(len(fn.tennis_star_hotels(all_data, True)), "of those hotels have five stars.")
    print(len(fn.tennis_star_hotels(all_data, False)), "of those hotels have tennis courts.")
    print()
    for key in fn.per_hotel_stats(all_data):
        print(key, "has", end = "")
        char_spaces = char_format - int(len(key))
        for i in range(char_spaces):
            print(" ", end = "")
        print(fn.per_hotel_stats(all_data)[key][1], "rooms, ", end = "")
        num_spaces = num_format - int(len(fn.per_hotel_stats(all_data)[key][1]))
        for i in range(num_spaces):
            print(" ", end ="")
        print(fn.per_hotel_stats(all_data)[key][2],"stars, ", end = "")
        print(fn.per_hotel_stats(all_data)[key][0], "reviews, and an average score of", format(fn.per_hotel_stats(all_data)[key][3], '.4f'))
    print()
    hotel_stats = fn.per_hotel_stats(all_data)
    try:
        print("The hotel with the highest average score is", max(hotel_stats, key=lambda hotel: hotel_stats[hotel][3]), end="")
        print(".")
    except ValueError:
        print("File is bad.")
        sys.exit()


main()