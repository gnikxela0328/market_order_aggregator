class DataCollection():
    # find bid ask spread for each entry
    def calc_bid_ask_spread(row):
        difference = abs(row['ap0'] - row['bp0'])
        return difference

    # calculate going rate for each entry
    def calc_going_rate(row):
      going_rate = (row['ap0'] + row['bp0']) / 2
      return going_rate

      # calculate volume weighted average price per entry (ASK SIDE)
    def calc_vwap_a(row):
      total_volume = 0
      total_price = 0

      if row['ap0'] != 0:
        total_volume+=row['aq0']
        total_price+= row['ap0'] * row['aq0']

      if row['ap1'] != 0:
        total_volume+=row['aq1']
        total_price+= row['ap1'] * row['aq1']

      if row['ap2'] != 0:
        total_volume+=row['aq2']
        total_price+= row['ap2'] * row['aq2']

      if row['ap3'] != 0:
        total_volume+=row['aq3']
        total_price+= row['ap3'] * row['aq3']

      if row['ap4'] != 0:
        total_volume+=row['aq4']
        total_price+= row['ap4'] * row['aq4']

      return total_price / total_volume if total_volume != 0 else 0

    # calculate volume weighted average price per entry (BID SIDE)
    def calc_vwap_b(row):
      total_volume = 0
      total_price = 0

      if row['bp0'] != 0:
        total_volume+=row['bq0']
        total_price+= row['bp0'] * row['bq0']

      if row['bp1'] != 0:
        total_volume+=row['bq1']
        total_price+= row['bp1'] * row['bq1']

      if row['bp2'] != 0:
        total_volume+=row['bq2']
        total_price+= row['bp2'] * row['bq2']

      if row['bp3'] != 0:
        total_volume+=row['bq3']
        total_price+= row['bp3'] * row['bq3']

      if row['bp4'] != 0:
        total_volume+=row['bq4']
        total_price+= row['bp4'] * row['bq4']

      return total_price / total_volume if total_volume != 0 else 0


    # calculate orderbook imbalance (p > 1 => ask heavy, p < 1 => bid heavy)
    def calc_imbal(row):
      bids = 0
      asks = 0

      if row['ap0'] != 0:
        asks+=1
      if row['ap1'] != 0:
        asks+=1
      if row['ap2'] != 0:
        asks+=1
      if row['ap3'] != 0:
        asks+=1
      if row['ap4'] != 0:
        asks+=1

      if row['bp0'] != 0:
        bids+=1
      if row['bp1'] != 0:
        bids+=1
      if row['bp2'] != 0:
        bids+=1
      if row['bp3'] != 0:
        bids+=1
      if row['bp4'] != 0:
        bids+=1

      return asks / bids

    # calculate volume
    def calc_volume(row):
      volume = 0

      if row['ap0'] != 0:
        volume+=row['bq0']
      if row['ap1'] != 0:
        volume+=row['bq1']
      if row['ap2'] != 0:
        volume+=row['bq2']
      if row['ap3'] != 0:
        volume+=row['bq3']
      if row['ap4'] != 0:
        volume+=row['bq4']

      if row['bp0'] != 0:
        volume+=row['bq0']
      if row['bp1'] != 0:
        volume+=row['bq1']
      if row['bp2'] != 0:
        volume+=row['bq2']
      if row['bp3'] != 0:
        volume+=row['bq3']
      if row['bp4'] != 0:
        volume+=row['bq4']

      return volume


    def calc_target(current_price):
        # calculate target feature, bearish, bullish, or no_change
        # this will be determined by comparing the going rate of the current day to the going rate of the following day

        target = []

        for x in range(len(current_price) - 1):
          if current_price[x] < current_price[x + 1]:
            target.append("bullish")
          elif current_price[x] > current_price[x + 1]:
            target.append("bearish")
          else:
            target.append("no_change")

        target.append("no_change")

        return target