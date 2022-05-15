################
# Evan Cazares
# Final
# Driver File
################
import sys
import functions as fn
import pandas as pd

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
        print(key, "has", fn.per_hotel_stats(all_data)[key][1], "rooms,", fn.per_hotel_stats(all_data)[key][2],"stars, ", end="")
        print(fn.per_hotel_stats(all_data)[key][0], "reviews, and an average score of", format(fn.per_hotel_stats(all_data)[key][3], '.4f'))
    print()
    hotel_stats = fn.per_hotel_stats(all_data)
    print("The hotel with the highest average score is", max(hotel_stats, key=lambda hotel: hotel_stats[hotel][3]), end="")
    print(".")

main()