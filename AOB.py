"""
!max market day => 36 trillion microseconds => ten hours
!∴ each input csv is one day

!program should output one whole csv per day of input


class AOB uses three dictionaries to keep track of results ::

a_book : keeps track of all ask orders for a given price index -> price: [(id, quant)]
b_book : keeps track of all bid orders for a given price index -> price: [(id, quant)]
id_book : keeps track of the previous price point for all orders, indexed by id -> id: price


Steps to update book:

    read line from csv

        perform specified action

            add -> add price/side pair to book
            delete -> remove price/side pair from book
            modify -> change price or side on given entry-> add new price/quant pair to given id

        update corresponding order book side, and id_book mapping

        append update to lists
    
    produce order book output
"""

import heapq
import pandas as pd

class AOB():
    def __init__(self):
        ### Setup lists for output to dataframe
        self.timestamps = []
        self.prices = []
        self.sides = []
        
        # Book Depths
        self.bp0 = []
        self.bq0 = []
        
        self.bp1 = []
        self.bq1 = []
        
        self.bp2 = []
        self.bq2 = []
        
        self.bp3 = []
        self.bq3 = []
        
        self.bp4 = []
        self.bq4 = []
        
        self.ap0 = []
        self.aq0 = []
        
        self.ap1 = []
        self.aq1 = []
        
        self.ap2 = []
        self.aq2 = []
        
        self.ap3 = []
        self.aq3 = []
        
        self.ap4 = []
        self.aq4 = []

        # holds all ask orders -> price: [(id, quant)]
        self.a_book = {}

        # holds all bid orders -> price: [(id, quant)]
        self.b_book = {}

        # holds all mappings between id and price -> id: price
        self.id_book = {}


    def add_entry(self, id, quantity, side, price):
        # store order in respective book
        if side == "a":
            if price in self.a_book:
                self.a_book[price].append((id, quantity))
            else:
                self.a_book[price] = [(id, quantity)]
        else:
            if price in self.b_book:
                self.b_book[price].append((id, quantity))
            else:
                self.b_book[price] = [(id, quantity)]

        # map id to original price and quant point
        self.id_book[id] = (price, quantity)
    
    def modify_entry(self, id, quantity, side, price):
        # get last entry from id_book
        latest_entry = self.id_book[id]

        if side == "a":
            # remove old entry
            self.a_book[latest_entry[0]].remove((id, latest_entry[1]))

            # add updated entry
            if price in self.a_book:
                self.a_book[price].append((id, quantity))
            else:
                self.a_book[price] = [(id, quantity)]

        else:
            # remove old entry
            self.b_book[latest_entry[0]].remove((id, latest_entry[1]))

            # add updated entry
            if price in self.b_book:
                self.b_book[price].append((id, quantity))
            else:
                self.b_book[price] = [(id, quantity)]

        # update id_book
        self.id_book[id] = (price, quantity)


    def delete_entry(self, id, quantity, side, price):
        if side == "a":
            # remove old entry
            self.a_book[price].remove((id, quantity))

        else:
            # remove old entry
            self.b_book[price].remove((id, quantity))

        # update id_book
        del self.id_book[id]

    def sum_a_side(self):
        top_prices = heapq.nsmallest(5, self.a_book, key=self.a_book.get)
        a_figures = []

        # sum quantities for each price
        for n in top_prices:
            agg_quantity = 0
            for m in self.a_book[n]:
                agg_quantity+=int(m[1])

            a_figures.append((n, agg_quantity))

        if len(a_figures) >= 1:
            self.ap0.append(a_figures[0][0])
            self.aq0.append(a_figures[0][1])
        else:
            self.ap0.append(0)
            self.aq0.append(0)

        if len(a_figures) >= 2:
            self.ap1.append(a_figures[1][0])
            self.aq1.append(a_figures[1][1])
        else:
            self.ap1.append(0)
            self.aq1.append(0)

        if len(a_figures) >= 3:
            self.ap2.append(a_figures[2][0])
            self.aq2.append(a_figures[2][1])
        else:
            self.ap2.append(0)
            self.aq2.append(0)

        if len(a_figures) >= 4:
            self.ap3.append(a_figures[3][0])
            self.aq3.append(a_figures[3][1])
        else:
            self.ap3.append(0)
            self.aq3.append(0)

        if len(a_figures) >= 5:
            self.ap4.append(a_figures[4][0])
            self.aq4.append(a_figures[4][1])
        else:
            self.ap4.append(0)
            self.aq4.append(0)

    def sum_b_side(self):
        top_prices = heapq.nlargest(5, self.b_book, key=self.b_book.get)
        b_figures = []

        # sum quantities for each price
        for n in top_prices:
            agg_quantity = 0
            for m in self.b_book[n]:
                agg_quantity+=int(m[1])

            b_figures.append((n, agg_quantity))

        if len(b_figures) >= 1:
            self.bp0.append(b_figures[0][0])
            self.bq0.append(b_figures[0][1])
        else:
            self.bp0.append(0)
            self.bq0.append(0)

        if len(b_figures) >= 2:
            self.bp1.append(b_figures[1][0])
            self.bq1.append(b_figures[1][1])
        else:
            self.bp1.append(0)
            self.bq1.append(0)

        if len(b_figures) >= 3:
            self.bp2.append(b_figures[2][0])
            self.bq2.append(b_figures[2][1])
        else:
            self.bp2.append(0)
            self.bq2.append(0)

        if len(b_figures) >= 4:
            self.bp3.append(b_figures[3][0])
            self.bq3.append(b_figures[3][1])
        else:
            self.bp3.append(0)
            self.bq3.append(0)

        if len(b_figures) >= 5:
            self.bp4.append(b_figures[4][0])
            self.bq4.append(b_figures[4][1])
        else:
            self.bp4.append(0)
            self.bq4.append(0)

    def create_csv(self, output_name):
        output_df = pd.DataFrame({
            "timestamp": self.timestamps,
            "price": self.prices,
            "side": self.sides,
            "bp0": self.bp0,
            "bq0": self.bq0,
            "bp1": self.bp1,
            "bq1": self.bq1,
            "bp2": self.bp2,
            "bq2": self.bq2,
            "bp3": self.bp3,
            "bq3": self.bq3,
            "bp4": self.bp4,
            "bq4": self.bq4,
            "ap0": self.ap0,
            "aq0": self.aq0,
            "ap1": self.ap1,
            "aq1": self.aq1,
            "ap2": self.ap2,
            "aq2": self.aq2,
            "ap3": self.ap3,
            "aq3": self.aq3,
            "ap4": self.ap4,
            "aq4": self.aq4,
        })

        output_df.to_csv(output_name, index=False)