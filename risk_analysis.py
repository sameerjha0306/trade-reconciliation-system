def risk_flags(df):
    risks = []

    for _, row in df.iterrows():

        if row['Amount_front'] > 25000:
            risks.append(f"High Value Trade: {row['TradeID']}")

        if row['Reconciliation_Status'] != "Matched":
            risks.append(f"Reconciliation Issue: {row['TradeID']}")

    return risks
