import sqlite3

conn = sqlite3.connect(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\Data\sales.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC
""")

results = cursor.fetchall()

for row in results:
    print(row)

conn.close()