import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    build_df = df.copy()

    # Binary target
    build_df["is_won"] = (build_df["outcome"].str.lower() == "won").astype(int)

    # Time features
    build_df["close_quarter"] = build_df["closed_date"].dt.to_period("Q").astype(str)

    # Deal age
    build_df["deal_age_days"] = (
        build_df["closed_date"] - build_df["created_date"]
    ).dt.days

    return build_df