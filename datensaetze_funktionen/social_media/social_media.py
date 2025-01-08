import datenvorverarbeitung.datenvorverarbeitung as dv
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

    df, dict3 = dv.map_keywords_to_integers(df, "keyword")
    df, dict4 = dv.map_keywords_to_integers(df, "location")
    dv.clean_text(df, "keyword")
    dv.clean_text(df, "text")

    data["cleaning"] = df.head().to_html(classes="table")

    corr_cov_keyword_target = st.korrelation_kovarianz(df["keyword"], df["target"])
    corr_cov_location_target = st.korrelation_kovarianz(df["location"], df["target"])

    data["correlation_covariance"] = f"Covariance: {corr_cov_keyword_target['covariance']:.2f}, Correlation: {corr_cov_keyword_target['correlation']:.2f}"
    data["correlation_covariance_interpretation"] = (f"--- Analyse der Korrelation und Kovarianz ---<br>"
                                                     f"Die Kovarianz {corr_cov_keyword_target['covariance']:.2f} indicates a small positive relationship between the variables.<br>")

    data["correlation_covariance"] = f"Covariance: {corr_cov_location_target['covariance']:.2f}, Correlation: {corr_cov_location_target['correlation']:.2f}"
    data["correlation_covariance_interpretation"] = (f"--- Analyse der Korrelation und Kovarianz ---<br>"
                                                     f"Die Kovarianz {corr_cov_location_target['covariance']:.2f} indicates a stronger positive relationship between the variables (but the absolute value depends on the data's scale).<br>")

    print("Bei beiden wenig Korrelation, da die Werte sehr nah an 0 sind.")

    vis.pie_chart(df, "target", "Anzahl der relevanten und irrelevanten Beiträge")
    print("-" * 80)
    print("Wir merken, dass Wörter wie 'people, time, etc herausstechen. Dies könnte darauf hindeuten, dass die Beiträge allgemein gehalten sind und nicht spezifisch auf Krisen eingehen.")
    vis.word_cloud(df, "text")
    print("Wir wollen jetzt die Wörter die häufig in relevanten Beiträgen vorkommen, visualisieren.")
    vis.word_cloud(df[df['target'] == 1], "text")
    print("Bei Relevanten Beiträgen sind Wörter wie fire, killed, oder australia (wahrscheinlich wegen Waldbrände, etc... häufiger zu finden. Dies könnte darauf hindeuten, dass die Beiträge spezifischer auf Krisen eingehen.")
    print("Wir wollen jetzt die Wörter die häufig in irrelevanten Beiträgen vorkommen, visualisieren.")
    vis.word_cloud(df[df['target'] == 0], "text")
    print("Hier merken wir wie beim Allgemeinen Wordcloud, dass Wörter wie people häufiger vorkommen. Viele Wörter sind gleichgroß was zeigt, dass sich die Beiträge nicht auf ein spezifisches Thema konzentrieren.")
    print("-" * 80)

    print(st.relative_haeufigkeit(df["location"]))

    # Calculate post lengths
    df['text_length'] = df['text'].apply(len)

    # Split into two groups
    relevant_posts = df[df['target'] == 1]['text_length']
    irrelevant_posts = df[df['target'] == 0]['text_length']

    # Calculate the average post length for each location
    print("Wir wollen jetzt schauen, ob die Länge des Textes einen Einfluss auf die Relevanz des Beitrags hat.")
    vis.pie_chart(df, "target", "Anzahl der relevanten und irrelevanten Beiträge")

    # 2 sample t-test
    t_test_2_sample(relevant_posts, irrelevant_posts, alternative='two-sided')

    print("Dies bedeutet, dass ein statistisch signifikanter Unterschied zwischen der durchschnittlichen Beitragslänge von relevanten und irrelevanten Beiträgen besteht.")

    print("Wir wollen jetzt schauen, ob das Sentiment des Textes einen Einfluss auf die Relevanz des Beitrags hat.")
    nlp.nlp_social_media(df, "text", 5)

    print("Wir merken, dass oft ein Negatives Sentiment auch ein Indikator für relevante Beiträge ist und umgekehrt. Wir können daraus schließen, dass relevante Beiträge für Katastrophe oft negativ sind. Das war zu erwarten wie man es schon mit der Wortwolke gesehen hat.")

    # Return data for output generation
    return data