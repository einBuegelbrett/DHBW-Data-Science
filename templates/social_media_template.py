social_media_template = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datenanalyse-Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; }
        h1, h2, h3 { color: #333; }
        section { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Datenanalyse-Report</h1>

    <section id="initial-dataset">
        <h2>Initialer Datensatz</h2>
        <p>{{ initial_dataset }}</p>
    </section>

    <section id="nach-cleaning">
        <h2>Nach Cleaning</h2>
        <p>{{ cleaning }}</p>
    </section>

    <section id="korrelation-kovarianz">
        <h2>Korrelation / Kovarianz</h2>
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_keyword_target }}</p>
        <p>Die Kovarianz {corr_cov_keyword_target['covariance']:.2f} indicates a small positive relationship between the variables.<p>
        
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_location_target }}</p>
        <p>Die Kovarianz {corr_cov_location_target['covariance']:.2f} indicates a stronger positive relationship between the variables (but the absolute value depends on the data's scale).<p>
        
        <h3>--- Interpretation ---</h3>
        <p>Bei beiden wenig Korrelation, da die Werte sehr nah an 0 sind.</p>
    </section>

    <section id="graphen">
        <h2>Graphen</h2>
        <p>{{ relative_frequency }}</p>
        <img src="images/target_pie_chart.png" alt="Target Pie Chart" width="400px" height="400px">
        <p>Wir merken, dass Wörter wie 'people, time, etc herausstechen. Dies könnte darauf hindeuten, dass die Beiträge allgemein gehalten sind und nicht spezifisch auf Krisen eingehen.</p>
        <img src="images/wordcloud_all.png" alt="Income Spending Scatterplot" width="400px" height="400px">
        <p>Wir wollen jetzt die Wörter die häufig in relevanten Beiträgen vorkommen, visualisieren.</p>
        <img src="images/wordcloud_relevant.png" alt="Income Spending Scatterplot" width="400px" height="400px">
        <p>Bei Relevanten Beiträgen sind Wörter wie fire, killed, oder australia (wahrscheinlich wegen Waldbrände, etc... häufiger zu finden. Dies könnte darauf hindeuten, dass die Beiträge spezifischer auf Krisen eingehen."</p>
        <p>Wir wollen jetzt die Wörter die häufig in irrelevanten Beiträgen vorkommen, visualisieren.<p>
        <img src="images/wordcloud_irrelevant.png" alt="Income Spending Scatterplot" width="400px" height="400px">
        <p>Hier merken wir wie beim Allgemeinen Wordcloud, dass Wörter wie people häufiger vorkommen. Viele Wörter sind gleichgroß was zeigt, dass sich die Beiträge nicht auf ein spezifisches Thema konzentrieren.</p>
        
        <p>Wir wollen jetzt schauen, ob die Länge des Textes einen Einfluss auf die Relevanz des Beitrags hat.</p>
        <img src="images/number_of_posts_pie_chart.png" alt="Number of Posts Pie Chart" width="400px" height="400px">
    </section>

    <section id="tests">
        <h2>Tests</h2>
        <p>{{ tests }}</p>
        <p>Dies bedeutet, dass ein statistisch signifikanter Unterschied zwischen der durchschnittlichen Beitragslänge von relevanten und irrelevanten Beiträgen besteht.</p>
    </section>

    <section id="nlp">
        <h2>nlp</h2>
        <p>Wir wollen jetzt schauen, ob das Sentiment des Textes einen Einfluss auf die Relevanz des Beitrags hat.</p>
        <p>{{ nlp }}</p>
        <img src="images/sentiment_scores_boxplot.png" alt="Sentiment Scores Boxplot" width="400px" height="400px">
        <img src="images/sentiment_bar_chart.png" alt="Sentiment Bar Chart" width="400px" height="400px">
        <p>Wir merken, dass oft ein Negatives Sentiment auch ein Indikator für relevante Beiträge ist und umgekehrt. Wir können daraus schließen, dass relevante Beiträge für Katastrophe oft negativ sind. Das war zu erwarten wie man es schon mit der Wortwolke gesehen hat.</p>
    </section>
</body>
</html>
"""
