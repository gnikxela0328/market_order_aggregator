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
Supply a CSV file to the main.py program. Output will be saved to the book_predictor/data/output folder

```
python3 main.py [INPUT FILE.csv]
```

<hr />

# Modelling

## Predictive Features
- Going rate
- Bid/Ask Spread
- Volume Weighted Average Price
- Orderbook Imbalance
- Volume

## Target (Determined by going rate)
- Bearish
- Bullish


F = [time_n, going rate_n, spread_n, vwap_n, imbalance_n, volume_n, bearish/bullish]