import pandas as pd

# Assuming you have already connected to the database and fetched the data into a DataFrame
# engine = create_engine('postgresql://your_user:your_password@your_host/your_database')
# data = pd.read_sql('SELECT * FROM stock_data', engine)

# Calculate the short-term (fast) and long-term (slow) moving averages
data['short_ma'] = data['close_price'].rolling(window=10).mean()
data['long_ma'] = data['close_price'].rolling(window=50).mean()

# Create signals based on the moving average crossover strategy
data['signal'] = 0  # 0 represents no signal
data['signal'][data['short_ma'] > data['long_ma']] = 1  # 1 represents buy signal
data['signal'][data['short_ma'] < data['long_ma']] = -1  # -1 represents sell signal

# Output the DataFrame with signals
print(data[['datetime', 'close_price', 'short_ma', 'long_ma', 'signal']])
