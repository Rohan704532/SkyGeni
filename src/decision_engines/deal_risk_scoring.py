import pandas as pd

def score_deal_risk(df: pd.DataFrame, stage_win_rates: dict) -> pd.DataFrame:
    df = df.copy()

    def compute_risk(row):
        stage = row["deal_stage"]
        win_prob = stage_win_rates.get(stage, 0.45)
        return 1 - win_prob

    df["risk_score"] = df.apply(compute_risk, axis=1)

    return df
