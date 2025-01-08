import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def boxplot(data, x, y, hue, title, x_label, y_label):
    """
    Create a box plot
    :param data: DataFrame containing the data
    :param x: The column name for the x-axis
    :param y: The column name for the y-axis
    :param hue: Optional, the column name to group the data by
    :param title: Title of the plot
    :param x_label: Label for the x-axis
    :param y_label: Label for the y-axis
    :return: None
    """
    plt.figure(figsize=(15, 10))
    sns.boxplot(data=data, x=x, y=y, hue=hue)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def scatterplot(data, column1, column2, imagename):
    """
    Create a scatter plot
    :param data: DataFrame containing the data
    :param column1: The column name for the x-axis
    :param column2: The column name for the y-axis
    :param imagename: Name of the image file to save the plot
    :return: None
    """
    plt.figure(figsize=(15, 10))
    plt.scatter(data[column1], data[column2])
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f"Scatterplot: {column1} vs {column2}")
    plt.savefig(f"images/{imagename}.png")
    plt.show()


def histogram(data, column, title, imagename):
    """
    Create a histogram
    :param data: DataFrame containing the data
    :param column: The column name for the histogram
    :param title: Title of the plot
    :param imagename: Name of the image file to save the plot
    :return: None
    """
    plt.figure(figsize=(15, 10))
    sns.histplot(data[column], kde=False, bins=10)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.savefig(f"images/{imagename}.png")
    plt.show()

def bar_chart(data, x, hue):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x=x, hue=hue, palette='Set2')
    plt.title("Count of Sentiment by Relevance")
    plt.xlabel("Relevance (0 = Irrelevant, 1 = Relevant)")
    plt.ylabel("Count of Posts")
    plt.legend(title="Sentiment")
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


def word_cloud(data, column):
    """
    Creates a word cloud based on a specific column of a DataFrame.

    :param data: DataFrame containing the data.
    :param column: The name of the column in the DataFrame to be used for the word cloud.
                   The column should contain text data.
    :return: None.
    """
    text = ' '.join(data[column].dropna().astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def lineplot(x, y, hue=None, data=None, title=None, x_label=None, y_label=None):
    """
    Create a line plot using Seaborn or Matplotlib.

    :param x: x-axis values (list or DataFrame column)
    :param y: y-axis values (list or DataFrame column)
    :param hue: Optional, grouping variable for multiple lines (default: None)
    :param data: Optional, DataFrame containing the data
    :param title: Title of the plot
    :param x_label: Label for the x-axis
    :param y_label: Label for the y-axis
    :return: None
    """
    plt.figure(figsize=(15, 10))
    if data is not None:
        sns.lineplot(data=data, x=x, y=y, hue=hue)
    else:
        plt.plot(x, y, marker='o', label='Accuracy')
    plt.title(title or "Line Plot")
    plt.xlabel(x_label or "X-axis")
    plt.ylabel(y_label or "Y-axis")
    if hue is None:
        plt.legend()
    plt.show()
