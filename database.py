import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
)

# Create a cursor object
cur = conn.cursor()

# Define a table schema
create_table_query = '''
CREATE TABLE stock_data (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP,
    ticker VARCHAR(10),
    open_price DECIMAL,
    high_price DECIMAL,
    low_price DECIMAL,
    close_price DECIMAL,
    volume INT
);
'''

# Execute the query to create the table
cur.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
