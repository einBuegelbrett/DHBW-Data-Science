import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def confusion_matrix_plot(x: pd.Series, y: pd.Series, label) -> None:
    # Confusion Matrix
    cm = confusion_matrix(x, y)

    # Confusion Matrix visualization
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=label.classes_, yticklabels=label.classes_)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Categories')
    plt.ylabel('Actual Categories')
    plt.savefig('images/knn_confusion_matrix.png')
    plt.show()