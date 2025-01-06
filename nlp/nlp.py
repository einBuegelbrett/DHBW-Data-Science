import pandas as pd
from transformers import pipeline
from eda.visualisierungen import boxplot, bar_chart

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

    data_subset = data[[column, 'target']].dropna(subset=[column]).head(lines_to_process)
    texts = data_subset[column].tolist()
    relevances = data_subset['target'].tolist()

    # Perform sentiment analysis
    sentiment_results = [classifier(text)[0] for text in texts]

    # Display some sentiment results with relevance
    for text, result, relevance in zip(texts, sentiment_results, relevances):
        print(f"Text: {text}")
        print(f"Sentiment: {result['label']} (Score: {result['score']:.2f})")
        print(f"Relevance to crisis: {'Relevant' if relevance == 1 else 'Irrelevant'}")
        print("-" * 80)

    # Add results to the DataFrame
    data_subset['Sentiment'] = [result['label'] for result in sentiment_results]
    data_subset['Score'] = [result['score'] for result in sentiment_results]

    boxplot(data_subset, 'target', 'Score', 'Sentiment', 'Sentiment Scores by Relevance', 'Relevance (0 = Irrelevant, 1 = Relevant)', 'Sentiment Score')
    bar_chart(data_subset, 'target', 'Sentiment')

