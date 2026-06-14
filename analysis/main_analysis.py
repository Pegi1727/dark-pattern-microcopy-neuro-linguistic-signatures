import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def run_statistical_analysis():
    # 1. Load the enriched dataset
    try:
        data = pd.read_csv('../data/dark_patterns_microcopy_360_enriched.csv')
        print("Dataset loaded successfully.\n")
    except FileNotFoundError:
        print("Error: Dataset not found. Please ensure the CSV is in the /data folder.")
        return

    # 2. Perform One-Way ANOVA (Example: Complexity Index across Pattern Types)
    model = ols('complexity_index ~ C(pattern_type)', data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print("--- ANOVA Results (Complexity Index) ---")
    print(anova_table)
    print("\n")

    # 3. Post-hoc Tukey HSD Test
    tukey = pairwise_tukeyhsd(endog=data['complexity_index'],
                              groups=data['pattern_type'],
                              alpha=0.05)
    print("--- Tukey HSD Post-hoc Results ---")
    print(tukey.summary())
    print("\n")

    # 4. Save results to analysis folder
    anova_table.to_csv('anova_results_summary.csv')
    print("Results have been exported to 'anova_results_summary.csv'.")

if __name__ == "__main__":
    run_statistical_analysis()

