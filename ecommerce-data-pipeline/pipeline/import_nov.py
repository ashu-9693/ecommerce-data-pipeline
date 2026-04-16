import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ASHU",
    database="ecommerce"
)

cursor = conn.cursor()

file_path = file_path = r"C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\2019-Nov.csv"

sql = """
INSERT INTO events
(event_time, event_type, product_id, category_id, category_code, brand, price, user_id, user_session)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

total_rows = 0

for chunk in pd.read_csv(file_path, chunksize=20000, keep_default_na=True):
    chunk = chunk.astype(object)
    chunk = chunk.where(pd.notna(chunk), None)

    data = []
    for row in chunk.itertuples(index=False, name=None):
        cleaned_row = tuple(None if str(value).lower() == "nan" else value for value in row)
        data.append(cleaned_row)

    cursor.executemany(sql, data)
    conn.commit()

    total_rows += len(data)
    print(f"Inserted total rows: {total_rows}")

cursor.close()
conn.close()

print("2019-Oct.csv imported successfully!")