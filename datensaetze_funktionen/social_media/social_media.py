import datenvorverarbeitung.data_cleaning as dv
import eda.statistiken as st
import nlp.nlp as nlp
import eda.visualisierungen as vis
from eda.test import t_test_2_sample

def social_media_main(df):
    """
    Main function to perform analysis on the social media dataset.

    :param df: Input DataFrame containing social media data
    :return: Data Input for output generation
    """
    data = {}
    data["initial_dataset"] = df.head().to_html(classes="table")

    # Data Cleaning
    df, dict3 = dv.map_keywords_to_integers(df, "keyword")
    df, dict4 = dv.map_keywords_to_integers(df, "location")
    dv.clean_text(df, "keyword")
    dv.clean_text(df, "text")
    df['text_length'] = df['text'].apply(len)  # Calculate post lengths
    data["cleaning"] = df.head().to_html(classes="table")

    # Correlation and covariance
    corr_cov_keyword_target = st.korrelation_kovarianz(df["text_length"], df["target"])
    corr_cov_location_target = st.korrelation_kovarianz(df["location"], df["target"])
    data["corr_cov_keyword_target"] = f"Covariance: {corr_cov_keyword_target['covariance']:.2f}, Correlation: {corr_cov_keyword_target['correlation']:.2f}"
    data["corr_cov_location_target"] = f"Covariance: {corr_cov_location_target['covariance']:.2f}, Correlation: {corr_cov_location_target['correlation']:.2f}"

    # Graphs
    vis.pie_chart(df, "target", "Anzahl der relevanten und irrelevanten Beiträge", "target_pie_chart")
    vis.word_cloud(df, "text", "Word Cloud for relevant and irrelevant posts", "wordcloud_all")
    vis.word_cloud(df[df['target'] == 1], "text", "Word Cloud for relevant posts", "wordcloud_relevant")
    vis.word_cloud(df[df['target'] == 0], "text", "Word Cloud for irrelevant posts", "wordcloud_irrelevant")
    data["relative_frequency"] = st.relative_haeufigkeit(df["location"])
    relevant_posts = df[df['target'] == 1]['text_length'] # Split into first groups
    irrelevant_posts = df[df['target'] == 0]['text_length'] # Split into second groups
    vis.pie_chart(df, "target", "Anzahl der relevanten und irrelevanten Beiträge", "number_of_posts_pie_chart") # Calculate the average post length for each location

    # Tests
    data["tests"] = t_test_2_sample(relevant_posts, irrelevant_posts, alternative='two-sided')

    # NLP
    data["nlp"] = nlp.nlp_social_media(df, "text", 5)

    # Return data for output generation
    return data