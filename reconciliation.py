def reconcile(df):

    def check(row):
        if row['Amount_back'] is None:
            return "Missing in Back Office"
        elif row['Amount_front'] != row['Amount_back']:
            return "Mismatch"
        else:
            return "Matched"

    df['Reconciliation_Status'] = df.apply(check, axis=1)
    return df
