import pandas as pd
from transformers import pipeline
from eda.visualisierungen import boxplot, bar_chart

def nlp_social_media(data: pd.DataFrame, column: str, lines_to_process: int) -> str:
    """
    Analyze the sentiment of social media posts and correlate with relevance to crises.

    :param data: A pandas DataFrame containing the data.
    :param column: The column name containing the text data for analysis.
    :param lines_to_process: Number of lines to process from the data.
    :return: A string containing the formatted analysis results.
    """
    # Initialize an empty string to hold the output
    output = ""

    # Sentiment-Analyse Pipeline laden
    classifier = pipeline('sentiment-analysis', model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')

    data_subset = data[[column, 'target']].dropna(subset=[column]).head(lines_to_process)
    texts = data_subset[column].tolist()
    relevances = data_subset['target'].tolist()

    # Perform sentiment analysis
    sentiment_results = [classifier(text)[0] for text in texts]

    output += "<table id=\"sentiment-table\" class=\"table\"><thead><tr><th>Text</th><th>Sentiment</th><th>Relevance to Crisis</th></tr></thead><tbody>"

    # Display some sentiment results with relevance
    for text, result, relevance in zip(texts, sentiment_results, relevances):
        output += f"<tr><td>Text: {text}</td>"
        output += f"<td>Sentiment: {result['label']} (Score: {result['score']:.2f})</td>"
        output += f"<td>Relevance to crisis: {'Relevant' if relevance == 1 else 'Irrelevant'}</td></tr>"

    output += "</tbody></table>"

    # Add results to the DataFrame
    data_subset['Sentiment'] = [result['label'] for result in sentiment_results]
    data_subset['Score'] = [result['score'] for result in sentiment_results]

    boxplot(data_subset, 'target', 'Score', 'Sentiment', 'Sentiment Scores by Relevance', 'Relevance (0 = Irrelevant, 1 = Relevant)', 'Sentiment Score', 'sentiment_scores_boxplot')
    bar_chart(data_subset, 'target', 'Sentiment', 'sentiment_bar_chart')

    return output
