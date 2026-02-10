import pandas as pd

def load_sales_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Parse dates
    df["created_date"] = pd.to_datetime(df["created_date"])
    df["closed_date"] = pd.to_datetime(df["closed_date"], errors="coerce")

    return df