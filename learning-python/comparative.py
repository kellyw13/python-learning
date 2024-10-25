import pandas as pd
import math

# Import dataset from excel
data_a = pd.read_excel("grupp7.xlsx", sheet_name="DataA")
data_b = pd.read_excel("grupp7.xlsx", sheet_name="DataB")

# Calculate the number of measurement and proportion of defects for both processes

# Process A
n1 = len(data_a)  # number of measurement
p1_hat = data_a.mean()[0]  # proportion of defects

# Process B
n2 = len(data_b)  # number of measurement
p2_hat = data_b.mean()[0]  # proportion of defects

# Confidence interval for both process

# z-score for 95% confidence interval
z = 1.96

# Confidence interval for process A
lower_ci_a = p1_hat - z * math.sqrt(p1_hat * (1 - p1_hat) / n1)
upper_ci_a = p1_hat + z * math.sqrt(p1_hat * (1 - p1_hat) / n1)

# Confidence interval for process B
lower_ci_b = p2_hat - z * math.sqrt(p2_hat * (1 - p2_hat) / n2)
upper_ci_b = p2_hat + z * math.sqrt(p2_hat * (1 - p2_hat) / n2)

print(
    f"95% Confidence interval for Process A: ({lower_ci_a:.4f}, {upper_ci_a:.4f})")
print(
    f"95% Confidence interval for Process B: ({lower_ci_b:.4f}, {upper_ci_b:.4f})")

# Summary Table

summary_table = pd.DataFrame({
    'Process': ['A', 'B'],
    'Number of measurements': [n1, n2],
    'Estimated proportions of defects': [p1_hat, p2_hat],
    '95% CI lower bound': [lower_ci_a, lower_ci_b],
    '95% CI upper bound': [upper_ci_a, upper_ci_b]
})

print(summary_table)
