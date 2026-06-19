import pandas as pd
import sqlite3

# Load Excel file
df = pd.read_excel(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\data\Superstore Dataset.xlsx",
    sheet_name="Orders"
)

# Create SQLite database
conn = sqlite3.connect(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\data\sales.db"
)

# Export data to SQL table
df.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully!")

conn.close()