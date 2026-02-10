import pandas as pd

def win_rate_driver(df: pd.DataFrame, column: str) -> pd.DataFrame:
    baseline = df["is_won"].mean()

    driver = (
        df.groupby(column)["is_won"]
        .mean()
        .reset_index()
        .rename(columns={"is_won": "win_rate"})
    )

    driver["impact_vs_baseline"] = driver["win_rate"] - baseline

    return driver.sort_values("impact_vs_baseline")
