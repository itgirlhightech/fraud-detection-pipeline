import pandas as pd
import sqlite3 as sql

def load(df):
    conn = sql.connect('data/fraud_detection.db')
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    print(f"Quantidade de linhas salvas no banco: {len(df)}")
    conn.close()

