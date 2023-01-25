"""
DRIVER CODE

Input files must be provided in the form of a csv

The code is designed to ignore the first line of input (in our case, this is the line of the csv file
that lists the column headers)

Output csv files are stored in the book_predictor/data/output folder


To see how the Aggregate Order Book is structured, refer to AOB.py
"""
import os
import sys
from AOB import AOB

ROOT_DIR = os.path.realpath(os.path.dirname(__file__))

# supply name of daily input csv to program using command line
input_name = sys.argv[1]
output_name = ROOT_DIR + "/data/output/" + input_name.split("/")[2] + "_aggregate_output.csv"

# open input file
f = open(input_name)

# ditch first line of csv
next(f)

# Create new Aggregate Order Book
OrderBook = AOB()

for x in f:
    # values
    line = x.split(',')
    timestamp = line[0]
    side = line[1]
    action = line[2]
    id = line[3]
    price = int(line[4])
    quantity = line[5].strip()

    # record timestamp, price, and side of each entry line
    OrderBook.timestamps.append(timestamp)
    OrderBook.prices.append(price)
    OrderBook.sides.append(side)

    ### determine action

    # add an entry
    if action == "a":
        # store order in respective book
        OrderBook.add_entry(id=id, side=side, quantity=quantity, price=price)
    
    # modify an entry
    elif action == "m":
        OrderBook.modify_entry(id=id, side=side, quantity=quantity, price=price)
        
    # delete an entry
    else:
        OrderBook.delete_entry(id=id, side=side, quantity=quantity, price=price)
        

    ### Add output to aggregate book

    # a side
    OrderBook.sum_a_side()
    
    # b side
    OrderBook.sum_b_side()

OrderBook.create_csv(output_name=output_name)