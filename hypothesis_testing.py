import pandas as pd
from scipy.stats import ttest_ind

# Load Excel dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Print column names (to verify)
print("Columns in Dataset:")
print(df.columns.tolist())

# Check required columns
if "Gender" not in df.columns or "Total_Sales" not in df.columns:
    print("\nError: 'Gender' or 'Total_Sales' column not found.")
    print("Please check your Excel column names.")
    exit()

# Separate sales by gender
male_sales = df[df["Gender"] == "Male"]["Total_Sales"]
female_sales = df[df["Gender"] == "Female"]["Total_Sales"]

# Perform Independent Sample T-Test
t_stat, p_value = ttest_ind(male_sales, female_sales, equal_var=False)

print("\n===== Hypothesis Testing =====")
print(f"T-Statistic : {t_stat:.4f}")
print(f"P-Value     : {p_value:.4f}")

if p_value < 0.05:
    print("\nResult: Reject the Null Hypothesis")
    print("There is a significant difference in Total Sales between Male and Female customers.")
else:
    print("\nResult: Fail to Reject the Null Hypothesis")
    print("There is no significant difference in Total Sales between Male and Female customers.")