import pandas as pd
from src.config import HIGH_RISK_THRESHOLD

def generate_high_risk_alerts(df: pd.DataFrame) -> pd.DataFrame:
    alerts = df[df["risk_score"] >= HIGH_RISK_THRESHOLD][
        ["deal_id", "deal_stage", "risk_score", "deal_amount"]
    ]

    return alerts
