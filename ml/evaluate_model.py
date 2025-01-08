from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report

def evaluate_model(y_true, y_pred, average='weighted'):
    """
    Evaluates the performance of a classification model.

    :param y_true: True labels
    :param y_pred: Predicted labels
    :return: None
    """
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred, average=average))
    print("Recall:", recall_score(y_true, y_pred, average=average))
    print("F1-Score:", f1_score(y_true, y_pred, average=average))
