import yfinance as yf
import pandas as pd 

# Define the individual currency tickers
eur_ticker = 'EURUSD=X' # Euro to US Dollar is commonly used as a proxy for Euro
inr_ticker = 'INR=X'  # US Dollar to Indian Rupee

# Define the date range
start_data = "2023-01-01"
end_date = "2024-02-16"

# Download data from Yahoo Finance
eur_data = yf.download(eur_ticker, start=start_data, end=end_date)
inr_data = yf.download(inr_ticker, start=start_data, end=end_date)

# Combine the data into a single DataFrame
data = pd.DataFrame({'EUR_Close':eur_data['Close'], 'INR close':inr_data['Close']})

# Save the data to a CSV file
data.to_csv("eur_inr_data.csv")
