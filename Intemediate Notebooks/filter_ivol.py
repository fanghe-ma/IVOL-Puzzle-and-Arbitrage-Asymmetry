import pandas as pd
import wrds
import numpy as np

# Connect to WRDS
conn = wrds.Connection()

# Load ivol data
ivol_df = pd.read_csv('./ivol_part_1.csv', index_col=0)
ivol_df.index = pd.to_datetime(ivol_df.index)

# Get the latest date and permnos from ivol_df
date = ivol_df.index[-1]  # Get the most recent date
permnos = ivol_df.columns.astype(str).tolist()

# Split permnos into chunks to avoid SQL query length limits
chunk_size = 1000
permno_chunks = [permnos[i:i + chunk_size] for i in range(0, len(permnos), chunk_size)]

# Get prices for each chunk and combine results
prices_list = []
for chunk in permno_chunks:
    chunk_str = ','.join(chunk)
    prices_chunk = conn.raw_sql(
        f"""
        SELECT permno, prc
        FROM crsp.dsf
        WHERE date = '{date.strftime('%Y-%m-%d')}'
        AND permno IN ({chunk_str})
        """
    )
    prices_list.append(prices_chunk)

prices = pd.concat(prices_list).set_index('permno')

# Filter ivol_today for permnos with price >= 5
ivol_today = ivol_df.iloc[-1, :]  # Get the most recent row
valid_permnos = prices[prices['prc'].abs() >= 5].index.astype(str)
ivol_today_filtered = ivol_today[valid_permnos]

print(f"Number of permnos with price >= 5: {len(valid_permnos)}")
print(f"Total number of permnos: {len(ivol_today)}")
print("\nFiltered ivol_today:")
print(ivol_today_filtered)

# Save the filtered data
ivol_today_filtered.to_csv('ivol_today_filtered.csv') 