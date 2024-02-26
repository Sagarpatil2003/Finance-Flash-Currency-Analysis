import pandas as pd
import mplfinance as mpf
import pandas_ta as ta

# Load the data
data = pd.read_csv("eur_inr_data.csv", parse_dates=True, index_col=0)

# Ensure that the date exists in the DataFrame's index
desired_date = '2024-02-16'
if desired_date in data.index:
    one_day_data = data.loc[desired_date]

    # Calculate Moving Average
    one_day_data['MA'] = ta.sma(one_day_data['Close'], length=14)

    # Calculate Bollinger Bands
    one_day_data[['upper_band', 'middle_band', 'lower_band']] = ta.bbands(one_day_data['Close'], length=20)

    # Calculate CCI
    one_day_data['CCI'] = ta.cci(one_day_data['High'], one_day_data['Low'], one_day_data['Close'], length=20)

    # Print the calculated metrics
    print("One Day Metrics:")
    print(one_day_data[['MA', 'upper_band', 'middle_band', 'lower_band', 'CCI']])
    
    def make_decision(data):
        if data['Close'] > data['upper_band'] and data['CCI'] > 100:
            return "SELL"
        elif data['Close'] < data['lower_band'] and data['CCI'] < -100:
            return "BUY"
        else:
            return "NEUTRAL"

    # Apply the decision logic
    one_day_data['Decision'] = one_day_data.apply(make_decision, axis=1)

    # Print the trading decisions
    print("\nOne Day Trading Decisions:")
    print(one_day_data[['Close', 'Decision']])
    
    # Calculate one_week_data (assuming you have a similar logic for it)
    one_week_data = data.loc['2024-02-16':'2024-02-23']
    one_week_data['MA'] = ta.sma(one_week_data['Close'], length=14)
    one_week_data[['upper_band', 'middle_band', 'lower_band']] = ta.bbands(one_week_data['Close'], length=20)
    one_week_data['CCI'] = ta.cci(one_week_data['High'], one_week_data['Low'], one_week_data['Close'], length=20)

    # Apply the decision logic for one_week_data
    one_week_data['Decision'] = one_week_data.apply(make_decision, axis=1)

    # Print the trading decisions for one_week_data
    print("\nOne Week Trading Decisions:")
    print(one_week_data[['Close', 'Decision']])
else:
    print(f"Date '{desired_date}' not found in the DataFrame.")
