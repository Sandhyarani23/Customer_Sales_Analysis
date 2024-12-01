import pandas as pd

# Load data
data = pd.read_csv('sales_data.csv')

# Data cleaning
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

# Feature engineering
data['SaleDate'] = pd.to_datetime(data['SaleDate'])
data['DayOfWeek'] = data['SaleDate'].dt.dayofweek
