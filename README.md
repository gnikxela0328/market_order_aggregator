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

## Target (Determined by going rate)
- Bearish
- Bullish


### Model One feature vector

F = [timestamp,	going_rate,	b/a_spread,	ask_vol_weight_avg_price 	bid_vol_weight_avg_price, order_imbalance, volume, target]

timestamp : Corresponds with agg orderbook entries
going_rate : Calculated by taking the midpoint between the best ask and bid prices
b/a_spread : Calculated by taking the difference between the best ask and bid prices
ask_vol_weight_avg_price : Weighted average of ask prices for all order depths
bid_vol_weight_avg_price : Weighted average of bid prices for all order depths
order_imbalance : Denotes imbalance between number of orderbook entries
volume : Volume of shares for all order depths
target : Does the current going price increase or decrease at the next timestamp?



