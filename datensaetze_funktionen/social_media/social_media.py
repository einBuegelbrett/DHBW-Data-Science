import pandas as pd
from datenvorverarbeitung.datenbereinigung import map_keywords_to_integers, clean_text
from eda.konfidenzintervalle import konfidenzintervall
from eda.statistiken import korrelation_kovarianz, relative_haeufigkeit
from eda.test import t_test_2_sample
from eda.visualisierungen import pie_chart, word_cloud
from nlp.nlp_social_media import nlp_social_media

def social_media_main(df: pd.DataFrame) -> dict[str, str]:
    """
    Main function to perform analysis on the social media dataset.

    :param df: Input DataFrame containing social media data
    :return: Data Input for output generation
    """
    data = {}
    data["initial_dataset"] = df.head().to_html(classes="table")

    # Data Cleaning
    df, dict3 = map_keywords_to_integers(df, "keyword")
    df, dict4 = map_keywords_to_integers(df, "location")
    clean_text(df, "keyword")
    clean_text(df, "text")
    df['text_length'] = df['text'].apply(len)  # Calculate post lengths
    data["cleaning"] = df.head().to_html(classes="table")

    # Correlation and covariance
    corr_cov_keyword_target = korrelation_kovarianz(df["text_length"], df["target"])
    corr_cov_location_target = korrelation_kovarianz(df["location"], df["target"])
    data["corr_cov_keyword_target"] = f"Covariance: {corr_cov_keyword_target['covariance']:.2f}, Correlation: {corr_cov_keyword_target['correlation']:.2f}"
    data["corr_cov_location_target"] = f"Covariance: {corr_cov_location_target['covariance']:.2f}, Correlation: {corr_cov_location_target['correlation']:.2f}"

    # Graphs
    pie_chart(df, "target", "Anzahl der relevanten und irrelevanten Beiträge", "target_pie_chart")
    word_cloud(df, "text", "Word Cloud for relevant and irrelevant posts", "wordcloud_all")
    word_cloud(df[df['target'] == 1], "text", "Word Cloud for relevant posts", "wordcloud_relevant")
    word_cloud(df[df['target'] == 0], "text", "Word Cloud for irrelevant posts", "wordcloud_irrelevant")
    data["relative_frequency"] = relative_haeufigkeit(df["location"])

    # Konfidenzintervalle
    relevant_posts = df[df['target'] == 1]['text_length'] # Split into first groups
    irrelevant_posts = df[df['target'] == 0]['text_length'] # Split into second groups
    ci_relevant = konfidenzintervall(relevant_posts.values, confidence_level=0.95)
    ci_irrelevant = konfidenzintervall(irrelevant_posts.values, confidence_level=0.95)
    data["confidence_intervals"] = (
        f"Relevante Beiträge (95% KI): ({ci_relevant[0]:.2f}, {ci_relevant[1]:.2f}), "
        f"Irrelevante Beiträge (95% KI): ({ci_irrelevant[0]:.2f}, {ci_irrelevant[1]:.2f})"
    )

    # Tests
    data["ttest"] = t_test_2_sample(relevant_posts, irrelevant_posts, alternative='two-sided')

    # NLP
    data["nlp"] = nlp_social_media(df, "text", 5)

    # Return data for output generation
    return data