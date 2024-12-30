import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind, ttest_1samp, chi2_contingency

def normality_test(data: pd.DataFrame) -> int:
    """
    Perform a normality test on the data.

    :param data: A pandas DataFrame containing the data to test.
    :return: None. Results are printed directly.

    """
    # Perform the Shapiro-Wilk test
    stat, p = shapiro(data)

    # Report results
    print(f"Shapiro-Wilk Test for Normality:")
    print(f"Statistic={stat}, P-value={p}")
    if p > 0.05:
        print("Fail to reject the null hypothesis: Data is normally distributed.")
    else:
        print("Reject the null hypothesis: Data is not normally distributed.")

    return p



def t_test_1_sample(data: pd.DataFrame, mu_0: float, alternative: str = 'two-sided') -> None:
    """
    Perform a one-sample t-test on the data.

    :param data: A pandas Series containing the sample data to test.
    :param mu_0: The null hypothesis mean (population mean to compare the sample against).
    :param alternative: The type of test to perform:
                        'two-sided' (default) for testing if the sample mean is different from mu_0,
                        'greater' for testing if the sample mean is greater than mu_0,
                        'less' for testing if the sample mean is less than mu_0.
    :return: None. Results are printed directly.
    """


    # Perform the one-sample t-test
    t_stat, p_value = ttest_1samp(data, mu_0, alternative=alternative)

    # Report results
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

    if alternative == 'two-sided':
        print(f"Test is two-sided: Null hypothesis is {'rejected' if p_value < 0.05 else 'not rejected'}.")
    elif alternative == 'greater':
        print(f"Test is one-sided (greater): Null hypothesis is {'rejected' if p_value < 0.05 else 'not rejected'}.")
    elif alternative == 'less':
        print(f"Test is one-sided (less): Null hypothesis is {'rejected' if p_value < 0.05 else 'not rejected'}.")


def t_test_2_sample(data1: pd.Series, data2: pd.Series, alternative: str = 'two-sided') -> None:
    """
    Perform a two-sample t-test to compare the means of two independent samples.

    :param data1: A pandas Series containing the first sample data.
    :param data2: A pandas Series containing the second sample data.
    :param alternative: The type of test to perform:
                        'two-sided' (default) for testing if the means are different,
                        'greater' for testing if the mean of data1 is greater than data2,
                        'less' for testing if the mean of data1 is less than data2.
    :return: None. Results are printed directly.
    """

    # Levene's test for equality of variances
    stat, p = levene(data1, data2)
    equal_var = p > 0.05  # Assume equal variance if p > 0.05

    print("\nLevene’s Test for Equality of Variances:")
    print(f"Statistic={stat}, P-value={p} ({'Equal variances' if equal_var else 'Unequal variances'})")

    # Perform the two-sample t-test
    t_stat, p_value = ttest_ind(data1, data2, equal_var=equal_var, alternative=alternative)

    # Print the t-test results
    print("\nTwo-Sample T-Test:")
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")

    # Interpret the results based on the alternative hypothesis
    if alternative == 'two-sided':
        print(f"Test is two-sided: Null hypothesis is {'rejected' if p_value < 0.05 else 'not rejected'}.")
    elif alternative == 'greater':
        print(f"Test is one-sided (greater): Null hypothesis is {'rejected' if p_value < 0.05 else 'not rejected'}.")
    elif alternative == 'less':
        print(f"Test is one-sided (less): Null hypothesis is {'rejected' if p_value < 0.05 else 'not rejected'}.")


def chi_square_test(data: pd.DataFrame) -> None:
    """
    Perform a Chi-Square test of independence.

    :param data: A pandas DataFrame containing the contingency table.
    :return: None. Results are printed directly.
    """

    # Perform the Chi-Square test
    chi2, p, dof, expected = chi2_contingency(data)

    # Report results
    print(f"Chi-Square Statistic: {chi2}")
    print(f"P-value: {p}")
    print(f"Degrees of Freedom: {dof}")
    print("Expected Frequencies:")
    print(pd.DataFrame(expected, index=data.index, columns=data.columns))

    # Decision
    alpha = 0.05
    if p < alpha:
        print("Reject the null hypothesis: There is a significant association between the variables.")
    else:
        print("Fail to reject the null hypothesis: There is no significant association between the variables.")

