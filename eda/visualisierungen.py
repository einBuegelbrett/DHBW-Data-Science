

def scatterplot(data, column1, column2):
    plt.figure(figsize=(15, 10))
    data.plot.scatter(x=column1, y =column2)
    plt.show()