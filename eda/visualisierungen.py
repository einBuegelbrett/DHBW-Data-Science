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