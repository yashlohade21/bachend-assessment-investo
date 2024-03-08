import pandas as pd
from sqlalchemy import create_engine

# Assuming you have the data in a CSV file
data = pd.read_csv('your_data.csv')

# Connect to the PostgreSQL database using SQLAlchemy
engine = create_engine('postgresql://your_user:your_password@your_host/your_database')

# Insert data into the table
data.to_sql('stock_data', engine, if_exists='append', index=False)
