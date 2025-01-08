from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report

def evaluate_model(y_true, y_pred, average='weighted') -> str:
    """
    Evaluates the performance of a classification model.

    :param y_true: True labels
    :param y_pred: Predicted labels
    :return: None
    """
    # Initialize an empty string to hold the output
    output = ""

    output += f"Accuracy: {accuracy_score(y_true, y_pred)} <br>"
    output += f"Precision: {precision_score(y_true, y_pred, average=average)} <br>"
    output += f"Recall: {recall_score(y_true, y_pred, average=average)} <br>"
    output += f"F1-Score: {f1_score(y_true, y_pred, average=average)}"

    return output
