from src.ingestion.load_data import load_sales_data
from src.features.build_features import build_features
from src.metrics.win_rate_metrics import win_rate_by_stage
from src.decision_engines.deal_risk_scoring import score_deal_risk
from src.decision_engines.revenue_forecast import forecast_revenue
from src.alerts.alert_engine import generate_high_risk_alerts
from src.decision_engines.win_rate_drivers import win_rate_driver

DATA_PATH = "Data/raw/skygeni_sales_data.csv"

def main():
    df = load_sales_data(DATA_PATH)
    df = build_features(df)

    stage_rates_df = win_rate_by_stage(df)
    stage_win_rates = dict(
        zip(stage_rates_df["deal_stage"], stage_rates_df["win_rate"])
    )
    df = score_deal_risk(df, stage_win_rates)
    revenue = forecast_revenue(df, stage_win_rates)
    alerts = generate_high_risk_alerts(df)

    lead_source_drivers = win_rate_driver(df, "lead_source")
    industry_drivers = win_rate_driver(df, "industry")
    rep_drivers = win_rate_driver(df, "sales_rep_id")

    print("\nTop Win Rate Drivers (Lead Source):")
    print(lead_source_drivers.head())

    print("\nTop Win Rate Drivers (Industry):")
    print(industry_drivers.head())

    print("\nTop Win Rate Drivers (Sales Rep):")
    print(rep_drivers.head())

    print("\nExpected Revenue:", revenue)
    print("\nHigh Risk Deals:")

    if alerts.empty:
        print("✅ No high-risk deals detected at this time.")
    else:
        print(alerts.head())

if __name__ == "__main__":
    main()
