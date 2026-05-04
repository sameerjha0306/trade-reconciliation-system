from database.db_setup import setup_database
from src.db_operations import fetch_data
from src.reconciliation import reconcile
from src.risk_analysis import risk_flags
from src.report_generator import generate_report

# Step 1: Setup database
setup_database()

# Step 2: Fetch data using SQL
df = fetch_data()

# Step 3: Reconciliation
result = reconcile(df)
result.to_csv("output/reconciliation_output.csv", index=False)

# Step 4: Risk analysis
risks = risk_flags(result)

# Step 5: Generate report
generate_report(risks, "output/risk_report.txt")

print("Process Completed Successfully with SQL Integration!")
