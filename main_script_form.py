"""
max market day => 36 trillion microseconds => ten hours
∴ each input csv is one day

program should output one whole csv per day of input

Steps to update book

read line in csv

perform specified action

    add -> add price/side pair to book
    delete -> remove price/side pair from book
    modify -> change price or side on given entry-> add new price/quant pair to given id


- needs to allow updates to price
- needs to sum all quantities of a given price
"""

import os
import sys
import heapq
import pandas as pd

ROOT_DIR = os.path.realpath(os.path.dirname(__file__))

# supply name of daily input csv to program using command line
input_name = sys.argv[1]
output_name = ROOT_DIR + "/data/" + input_name.split("/")[2] + "_aggregate_output.csv"

# open input file
f = open(input_name)

# setup lists for output dataframe
timestamps = []
prices = []
sides = []

bp0 = []
bq0 = []

bp1 = []
bq1 = []

bp2 = []
bq2 = []

bp3 = []
bq3 = []

bp4 = []
bq4 = []

ap0 = []
aq0 = []

ap1 = []
aq1 = []

ap2 = []
aq2 = []

ap3 = []
aq3 = []

ap4 = []
aq4 = []
###


# holds all ask orders -> price: [(id, quant)]
a_book = {}

# holds all bid orders -> price: [(id, quant)]
b_book = {}

# holds all mappings between id and price -> id: price
id_book = {}

# ditch first line of csv
next(f)


for x in f:
    # values
    line = x.split(',')
    timestamp = line[0]
    side = line[1]
    action = line[2]
    id = line[3]
    price = line[4]
    quantity = line[5].strip()

    # record timestamp, price, and side of each entry line
    timestamps.append(timestamp)
    prices.append(price)
    sides.append(side)


    ### determine action

    # add an entry
    if action == "a":
        # store order in respective book
        if side == "a":
            if price in a_book:
                a_book[price].append((id, quantity))
            else:
                a_book[price] = [(id, quantity)]
        else:
            if price in b_book:
                b_book[price].append((id, quantity))
            else:
                b_book[price] = [(id, quantity)]

        # map id to original price and quant point
        id_book[id] = (price, quantity)

    
    elif action == "m":

        # get last entry from id_book
        latest_entry = id_book[id]

        if side == "a":

            # remove old entry
            a_book[latest_entry[0]].remove((id, latest_entry[1]))

            # add updated entry
            if price in a_book:
                a_book[price].append((id, quantity))
            else:
                a_book[price] = [(id, quantity)]


        else:

            # remove old entry
            b_book[latest_entry[0]].remove((id, latest_entry[1]))

            # add updated entry
            if price in b_book:
                b_book[price].append((id, quantity))
            else:
                b_book[price] = [(id, quantity)]

        # update id_book
        id_book[id] = (price, quantity)
    
    else:
        if side == "a":
            # remove old entry
            a_book[price].remove((id, quantity))

        else:
            # remove old entry
            b_book[price].remove((id, quantity))

        # update id_book
        del id_book[id]


    ### Add output to aggregate book

    # a side
    top_prices = heapq.nsmallest(5, a_book, key=a_book.get)
    a_figures = []

    # sum quantities for each price
    for n in top_prices:
        agg_quantity = 0
        for m in a_book[n]:
            agg_quantity+=int(m[1])
        
        a_figures.append((n, agg_quantity))
    
    if len(a_figures) >= 1:
        ap0.append(a_figures[0][0])
        aq0.append(a_figures[0][1])
    else:
        ap0.append(0)
        aq0.append(0)
    
    if len(a_figures) >= 2:
        ap1.append(a_figures[1][0])
        aq1.append(a_figures[1][1])
    else:
        ap1.append(0)
        aq1.append(0)

    if len(a_figures) >= 3:
        ap2.append(a_figures[2][0])
        aq2.append(a_figures[2][1])
    else:
        ap2.append(0)
        aq2.append(0)
    
    if len(a_figures) >= 4:
        ap3.append(a_figures[3][0])
        aq3.append(a_figures[3][1])
    else:
        ap3.append(0)
        aq3.append(0)

    if len(a_figures) >= 5:
        ap4.append(a_figures[4][0])
        aq4.append(a_figures[4][1])
    else:
        ap4.append(0)
        aq4.append(0)
    

    # b side
    top_prices = heapq.nlargest(5, b_book, key=b_book.get)
    b_figures = []

    # sum quantities for each price
    for n in top_prices:
        agg_quantity = 0
        for m in b_book[n]:
            agg_quantity+=int(m[1])
        
        b_figures.append((n, agg_quantity))

    
    if len(b_figures) >= 1:
        bp0.append(b_figures[0][0])
        bq0.append(b_figures[0][1])
    else:
        bp0.append(0)
        bq0.append(0)
    
    if len(b_figures) >= 2:
        bp1.append(b_figures[1][0])
        bq1.append(b_figures[1][1])
    else:
        bp1.append(0)
        bq1.append(0)

    if len(b_figures) >= 3:
        bp2.append(b_figures[2][0])
        bq2.append(b_figures[2][1])
    else:
        bp2.append(0)
        bq2.append(0)
    
    if len(b_figures) >= 4:
        bp3.append(b_figures[3][0])
        bq3.append(b_figures[3][1])
    else:
        bp3.append(0)
        bq3.append(0)

    if len(b_figures) >= 5:
        bp4.append(b_figures[4][0])
        bq4.append(b_figures[4][1])
    else:
        bp4.append(0)
        bq4.append(0)


output_df = pd.DataFrame({
    "timestamp": timestamps,
    "price": prices,
    "side": sides,
    "bp0": bp0,
    "bq0": bq0,
    "bp1": bp1,
    "bq1": bq1,
    "bp2": bp2,
    "bq2": bq2,
    "bp3": bp3,
    "bq3": bq3,
    "bp4": bp4,
    "bq4": bq4,
    "ap0": ap0,
    "aq0": aq0,
    "ap1": ap1,
    "aq1": aq1,
    "ap2": ap2,
    "aq2": aq2,
    "ap3": ap3,
    "aq3": aq3,
    "ap4": ap4,
    "aq4": aq4,
})


output_df.to_csv(output_name, index=False)
        

            
        

            

    

            
    

   
