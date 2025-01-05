import pandas as pd
from transformers import pipeline

def nlp_social_media(data: pd.DataFrame, column: str, lines_to_process: int) -> None:
    """
    Analyze the sentiment of social media posts and correlate with relevance to crises.

    :param data:
    :param column:
    :param lines_to_process:
    :return:
    """
    # Sentiment-Analyse Pipeline laden
    classifier = pipeline('sentiment-analysis')

    data_subset = data[[column, 'Zielvariable']].dropna(subset=[column]).head(lines_to_process)
    texts = data_subset[column].tolist()
    relevances = data_subset['Zielvariable'].tolist()

    # Perform sentiment analysis
    results = [classifier(text)[0] for text in texts]

    # Display results with relevance
    for text, result, relevance in zip(texts, results, relevances):
        print(f"Text: {text}")
        print(f"Sentiment: {result['label']} (Score: {result['score']:.2f})")
        print(f"Relevance to crisis: {'Relevant' if relevance == 1 else 'Irrelevant'}")
        print("-" * 80)