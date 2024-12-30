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
    plt.scatter(data[column1], data[column2])
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f"Scatterplot: {column1} vs {column2}")
    plt.show()


def histogram(data, column, title):
    plt.figure(figsize=(15, 10))
    sns.histplot(data[column], kde=False, bins=10)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()