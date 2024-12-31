import datenvorverarbeitung.datenvorverarbeitung as dv
import eda.statistiken as st
#import nlp.nlp as nlp
import eda.visualisierungen as vis
from eda.test import t_test_2_sample

def social_media_main(data):
    print(st.relative_haeufigkeit(data["location"]))
    data, dict3 = dv.map_keywords_to_integers(data, "keyword")
    data, dict4 = dv.map_keywords_to_integers(data, "location")

    dict1 = st.korrelation_kovarianz(data["keyword"], data["target"])
    dict2 = st.korrelation_kovarianz(data["location"], data["target"])
    # Bei beiden wenig Korrelation, da die Werte sehr nah an 0 sind.
    print(dict1)  # Indicates a small positive relationship between the variables.
    print(dict2)  # Indicates a stronger positive relationship between the variables (but the absolute value depends on the data's scale).
    # nlp.nlp_social_media(data)
    vis.pie_chart(data, "target", "Anzahl der relevanten und irrelevanten Beiträge")
    vis.word_cloud(data, "text")

    # 2 sample t-test
    # Calculate post lengths
    data['text_length'] = data['text'].apply(len)

    # Split into two groups
    relevant_posts = data[data['target'] == 1]['text_length']
    irrelevant_posts = data[data['target'] == 0]['text_length']

    t_test_2_sample(relevant_posts, irrelevant_posts, alternative='two-sided')

    print("This means there is a statistically significant difference between the average post lengths of relevant and irrelevant posts.")