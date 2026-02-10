import pandas as pd

def forecast_revenue(df: pd.DataFrame, stage_win_rates: dict) -> float:
    expected_revenue = 0.0

    for _, row in df.iterrows():
        win_prob = stage_win_rates.get(row["deal_stage"], 0.45)
        expected_revenue += row["deal_amount"] * win_prob

    return expected_revenue
