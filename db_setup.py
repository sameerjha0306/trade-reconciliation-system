import sqlite3
import pandas as pd

def setup_database():
    conn = sqlite3.connect("trade_system.db")

    front = pd.read_csv("data/front_office.csv")
    back = pd.read_csv("data/back_office.csv")

    front.to_sql("front_office", conn, if_exists="replace", index=False)
    back.to_sql("back_office", conn, if_exists="replace", index=False)

    conn.close()
    print("Database setup completed.")
