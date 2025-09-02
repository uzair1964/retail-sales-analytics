import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

# Ensure DB folder exists
Path("database").mkdir(parents=True, exist_ok=True)

# Read CSV
df = pd.read_csv("data/raw/transactions.csv", parse_dates=["order_datetime"])

# Create SQLite DB and load table
engine = create_engine("sqlite:///database/sales.db", echo=False)

with engine.begin() as conn:
    # Run DDL
    ddl_sql = Path("sql/ddl.sql").read_text()
    for stmt in ddl_sql.split(";"):
        s = stmt.strip()
        if s:
            conn.execute(text(s))

    # Load data
    df.to_sql("transactions", conn, if_exists="append", index=False)
    print("Loaded", len(df), "rows into database/sales.db")
