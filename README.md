# Aggregate Order Book + Price Predictor

## Installation
Create a virtual environment
```
python3 -m venv .env
```

Activate the virtual environment
```
source .env/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt
```

## Usage
Supply a CSV file to the main.py program. Output will be saved to the market_order_aggregator/data/output folder

```
python3 market_order_aggregator/processing/main.py [INPUT FILE.csv]
```

<hr />

# Modeling

## Predictive Features
- Going rate
- Bid/Ask Spread
- Volume Weighted Average Price
- Orderbook Imbalance
- Volume

## Target (Determined by going rate of next timestamp)
- Bearish
- Bullish


### Model One feature vector

Models can be found in market_order_aggregator/modeling

```
F = [timestamp,	going_rate,	b/a_spread,	ask_vol_weight_avg_price, bid_vol_weight_avg_price, order_imbalance, volume, target]
```

timestamp : Corresponds with agg orderbook entries <br />
going_rate : Calculated by taking the midpoint between the best ask and bid prices<br />
b/a_spread : Calculated by taking the difference between the best ask and bid prices<br />
ask_vol_weight_avg_price : Weighted average of ask prices for all order depths<br />
bid_vol_weight_avg_price : Weighted average of bid prices for all order depths<br />
order_imbalance : Denotes imbalance between number of orderbook entries<br />
volume : Volume of shares for all order depths<br />
target : Does the current going price increase or decrease at the next timestamp?<br />


#### References
- [Investigating Limit Order Book Characteristics for Short Term Price Prediction: a Machine Learning Approach](https://deliverypdf.ssrn.com/delivery.php?ID=379066111124123007021017094116093070033020028081008086064087120091099074030094115093126032033060045039030116126086030097066018111006059059074126025092072069031097093000035015103096005114074075101092070007020124075124115105020100095021014099117067064082&EXT=pdf&INDEX=TRUE)

- [Forecasting Quoted Depth With the Limit Order Book](https://www.frontiersin.org/articles/10.3389/frai.2021.667780/full)



