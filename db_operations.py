import sqlite3
import pandas as pd

def fetch_data():
    conn = sqlite3.connect("trade_system.db")

    query = """
    SELECT 
        f.TradeID,
        f.Amount AS Amount_front,
        b.Amount AS Amount_back,
        f.Date AS Date_front,
        b.Date AS Date_back,
        f.Status AS Status_front,
        b.Status AS Status_back
    FROM front_office f
    LEFT JOIN back_office b
    ON f.TradeID = b.TradeID
    """

    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
