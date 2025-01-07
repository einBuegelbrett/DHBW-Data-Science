import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
import nlp.nlp as nlp
import eda.visualisierungen as vis
from eda.test import t_test_2_sample

def social_media_main(data):
    print(st.relative_haeufigkeit(data["location"]))
    data, dict3 = dv.map_keywords_to_integers(data, "keyword")
    data, dict4 = dv.map_keywords_to_integers(data, "location")

    dv.clean_text(data, "keyword")
    dv.clean_text(data, "text")

    dict1 = st.korrelation_kovarianz(data["keyword"], data["target"])
    dict2 = st.korrelation_kovarianz(data["location"], data["target"])
    # Bei beiden wenig Korrelation, da die Werte sehr nah an 0 sind.
    print(dict1)  # Indicates a small positive relationship between the variables.
    print(dict2)  # Indicates a stronger positive relationship between the variables (but the absolute value depends on the data's scale).

    vis.pie_chart(data, "target", "Anzahl der relevanten und irrelevanten Beiträge")

    print("-" * 80)
    print("Wir merken, dass Wörter wie 'people, time, etc herausstechen. Dies könnte darauf hindeuten, dass die Beiträge allgemein gehalten sind und nicht spezifisch auf Krisen eingehen.")
    vis.word_cloud(data, "text")
    print("Wir wollen jetzt die Wörter die häufig in relevanten Beiträgen vorkommen, visualisieren.")
    vis.word_cloud(data[data['target'] == 1], "text")
    print("Bei Relevanten Beiträgen sind Wörter wie fire, killed, oder australia (wahrscheinlich wegen Waldbrände, etc... häufiger zu finden. Dies könnte darauf hindeuten, dass die Beiträge spezifischer auf Krisen eingehen.")
    print("Wir wollen jetzt die Wörter die häufig in irrelevanten Beiträgen vorkommen, visualisieren.")
    vis.word_cloud(data[data['target'] == 0], "text")
    print("Hier merken wir wie beim Allgemeinen Wordcloud, dass Wörter wie people häufiger vorkommen. Viele Wörter sind gleichgroß was zeigt, dass sich die Beiträge nicht auf ein spezifisches Thema konzentrieren.")
    print("-" * 80)

    # Calculate post lengths
    data['text_length'] = data['text'].apply(len)

    # Split into two groups
    relevant_posts = data[data['target'] == 1]['text_length']
    irrelevant_posts = data[data['target'] == 0]['text_length']

    # Calculate the average post length for each location
    vis.pie_chart(data, "target", "Anzahl der relevanten und irrelevanten Beiträge")

    # 2 sample t-test
    t_test_2_sample(relevant_posts, irrelevant_posts, alternative='two-sided')

    print("Dies bedeutet, dass ein statistisch signifikanter Unterschied zwischen der durchschnittlichen Beitragslänge von relevanten und irrelevanten Beiträgen besteht.")

    print("Wir wollen jetzt schauen, ob das Sentiment des Textes einen Einfluss auf die Relevanz des Beitrags hat.")
    nlp.nlp_social_media(data, "text", 5)