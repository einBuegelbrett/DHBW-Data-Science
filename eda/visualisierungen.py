import matplotlib.pyplot as plt
import seaborn as sns

def boxplot(data, x, y, hue, title, x_label, y_label, save_path):
    plt.figure(figsize=(15, 10))
    sns.boxplot(data=data, x=x, y=y, hue=hue)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(save_path)
    plt.show()


def scatterplot(data, column1, column2):
    plt.figure(figsize=(15, 10))
    data.plot.scatter(x=column1, y =column2)
    plt.show()


def pie_chart(data, column, title):
    """
    Creates a pie chart based on a specific column of a DataFrame.

    :param data: DataFrame containing the data.
    :param column: The name of the column in the DataFrame to be used for the chart.
                   The column should contain categorical data or data that can be grouped into categories.
    :param title: The title of the pie chart, displayed at the top of the chart.
    :return: None.
    """
    plt.figure(figsize=(15, 10))
    data[column].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title(title)
    plt.show()