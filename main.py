################
# Evan Cazares
# Final
# Driver File
################

import numpy as np
import sys
import functions as fn 
import pandas as pd

def main():

    # these two lines are all you need to run the program, but they do not do error
    # checking to make sure the file exists before calling count_lines() and dispay_file()
    # fix it to do proper error checking as shown in the examples. then erase this comment.

    all_data = pd.read_csv("hotel-reviews.csv")
    print(all_data)

main()