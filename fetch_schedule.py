import pandas as pd

SHEET_ID = "1jsMeb0MDqyzUjYp_A6jo_vScGJpHpBcJsnMQF2ELCB0"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

def get_next_session() -> pd.Series:
    df = pd.read_csv(URL, parse_dates=["Date"])
    df = df.dropna(subset=["Date", "Speaker", "Speaker email"])

    today = pd.Timestamp.today().normalize()
    next_session = df[df["Date"] > today].iloc[0]
    return next_session