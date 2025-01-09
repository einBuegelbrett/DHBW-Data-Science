import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind, ttest_1samp, chi2_contingency

def normality_test(data: pd.DataFrame, columns: list) -> str:
    """
    Perform normality tests for multiple numerical columns.

    :param data: pandas DataFrame containing the data
    :param columns: List of column names to test for normality
    """

    output = ""

    for column in columns:
        output += f" <br> Normality Test for {column}:\n <br>"
        stat, p = shapiro(data[column].dropna())  # Drop NaN values for the test
        output += f"Statistic={stat}, P-value={p}\n <br>"
        if p > 0.05:
            output += f"{column} is normally distributed.\n <br>"
        else:
            output += f"{column} is not normally distributed.\n <br>"

    return output

def t_test_1_sample(data: pd.DataFrame, mu_0: float, alternative: str = 'two-sided') -> str:
    """
    Perform a one-sample t-test on the data.

    :param data: A pandas Series containing the sample data to test.
    :param mu_0: The null hypothesis mean (population mean to compare the sample against).
    :param alternative: The type of test to perform:
                        'two-sided' (default) for testing if the sample mean is different from mu_0,
                        'greater' for testing if the sample mean is greater than mu_0,
                        'less' for testing if the sample mean is less than mu_0.
    :return: A string containing the formatted test results.
    """
    # Initialize an empty string to hold the output
    output = ""

    # Perform the one-sample t-test
    t_stat, p_value = ttest_1samp(data, mu_0, alternative=alternative)

    # Report results
    output += f"T-statistic: {t_stat}\n"
    output += f"P-value: {p_value}\n"

    if alternative == 'two-sided':
        decision = "rejected" if p_value < 0.05 else "not rejected"
        output += f"Test is two-sided: Null hypothesis is {decision}.\n"
    elif alternative == 'greater':
        decision = "rejected" if p_value < 0.05 else "not rejected"
        output += f"Test is one-sided (greater): Null hypothesis is {decision}.\n"
    elif alternative == 'less':
        decision = "rejected" if p_value < 0.05 else "not rejected"
        output += f"Test is one-sided (less): Null hypothesis is {decision}.\n"
    else:
        output += "Invalid alternative hypothesis.\n"

    return output


def t_test_2_sample(data1: pd.Series, data2: pd.Series, alternative: str = 'two-sided') -> str:
    """
    Perform a two-sample t-test to compare the means of two independent samples.

    :param data1: A pandas Series containing the first sample data.
    :param data2: A pandas Series containing the second sample data.
    :param alternative: The type of test to perform:
                        'two-sided' (default) for testing if the means are different,
                        'greater' for testing if the mean of data1 is greater than data2,
                        'less' for testing if the mean of data1 is less than data2.
    :return: A string containing the formatted test results.
    """
    # Initialize an empty string to hold the output
    output = ""

    # Levene's test for equality of variances
    stat, p = levene(data1, data2)
    equal_var = p > 0.05  # Assume equal variance if p > 0.05

    output += "\nLevene’s Test for Equality of Variances:\n"
    output += f"Statistic={stat}, P-value={p} ({'Equal variances' if equal_var else 'Unequal variances'})\n"

    # Perform the two-sample t-test
    t_stat, p_value = ttest_ind(data1, data2, equal_var=equal_var, alternative=alternative)

    # Print the t-test results
    output += "\nTwo-Sample T-Test:\n"
    output += f"T-statistic: {t_stat}\n"
    output += f"P-value: {p_value}\n"

    # Interpret the results based on the alternative hypothesis
    if alternative == 'two-sided':
        result = "rejected" if p_value < 0.05 else "not rejected"
        output += f"Test is two-sided: Null hypothesis is {result}.\n"
    elif alternative == 'greater':
        result = "rejected" if p_value < 0.05 else "not rejected"
        output += f"Test is one-sided (greater): Null hypothesis is {result}.\n"
    elif alternative == 'less':
        result = "rejected" if p_value < 0.05 else "not rejected"
        output += f"Test is one-sided (less): Null hypothesis is {result}.\n"
    else:
        return "Invalid alternative hypothesis."

    return output


def chi_square_test(data: pd.DataFrame) -> str:
    """
    Perform a Chi-Square test of independence.

    :param data: A pandas DataFrame containing the contingency table.
    :return: A string containing the formatted test results.
    """
    # Initialize an empty string to hold the output
    output = ""

    # Perform the Chi-Square test
    chi2, p, dof, expected = chi2_contingency(data)

    # Report results
    output += f"Chi-Square Statistic: {chi2}\n"
    output += f"P-value: {p}\n"
    output += f"Degrees of Freedom: {dof}\n"
    output += "Expected Frequencies:\n"
    output += pd.DataFrame(expected, index=data.index, columns=data.columns).to_string() + "\n"

    # Decision
    alpha = 0.05
    if p < alpha:
        output += "Reject the null hypothesis: There is a significant association between the variables.\n"
    else:
        output += "Fail to reject the null hypothesis: There is no significant association between the variables.\n"

    return output

