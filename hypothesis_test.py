import numpy as np
from scipy import stats

# 1. Simulate Data for Task 4
# Control Group: Users on the current layout (Mean session = 3.2 mins)
# Variant Group: Users on the personalized layout (Mean session = 4.1 mins)
np.random.seed(42)
control_group = np.random.normal(loc=3.2, scale=1.0, size=100)
variant_group = np.random.normal(loc=4.1, scale=1.1, size=100)

# 2. Define Hypotheses
# H0 (Null): No difference in session duration.
# Ha (Alternative): Personalized layout increases session duration.

# 3. Perform Independent Two-Sample T-Test
t_stat, p_value = stats.ttest_ind(control_group, variant_group)

# 4. Interpret the Results
alpha = 0.05  # 95% Confidence Level

print("--- Statistical Validation Results ---")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < alpha:
    print("Conclusion: Reject the Null Hypothesis (H0).")
    print("The increase in session duration is Statistically Significant.")
else:
    print("Conclusion: Fail to reject the Null Hypothesis (H0).")
    print("The difference could be due to random chance.")