import pandas as pd

def win_rate_by_stage(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("deal_stage")["is_won"]
        .mean()
        .reset_index()
        .rename(columns={"is_won": "win_rate"})
    )


def overall_win_rate(df: pd.DataFrame) -> float:
    return df["is_won"].mean()
