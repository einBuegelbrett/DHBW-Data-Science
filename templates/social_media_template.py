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
        <p>Hier ist der initiale Datensatz:</p>
        <p>{{ initial_dataset }}</p>
    </section>

    <section id="nach-cleaning">
        <h2>Nach Cleaning</h2>
        <p>Für die Datenvorbereitung wurden die folgenden Schritte durchgeführt:</p>
        <ul>
            <li>Ersetzen von fehlenden Werten</li>
            <li>Entfernen von Duplikaten</li>
            <li>Mapping von Keywords zu Integers</li>
            <li>Textbereinigung (Zum Beispiel Spezialzeichen wie "&amp%" entfernen)</li>
        </ul>
        <p>Der Datensatz nach der Bereinigung sieht wie folgt aus:</p>
        <p>{{ cleaning }}</p>
    </section>

    <section id="korrelation-kovarianz">
        <h2>Korrelation / Kovarianz</h2>
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_keyword_target }}</p>
        <p>Die Kovarianz {corr_cov_keyword_target['covariance']:.2f} indicates a small positive relationship between the variables.<p>
        <p>Die Analyse der Beziehung zwischen den Variablen "Keyword" und "Target" zeigt eine Kovarianz von {corr_cov_keyword_target['covariance']:.2f} und eine Korrelation von {corr_cov_location_target['correlation']:.2f}. Die positive Kovarianz weist auf eine leichte positive Beziehung hin, was bedeutet, dass eine Zunahme der Werte in der einen Variablen tendenziell mit einer leichten Zunahme in der anderen Variablen verbunden ist. Allerdings ist die Korrelation mit {corr_cov_keyword_target['correlation']:.2f} sehr schwach und nahe bei 0, was darauf hindeutet, dass diese lineare Beziehung nicht signifikant ist. In der Praxis bedeutet dies, dass "Keyword" als Variable nur eine sehr geringe Vorhersagekraft für den Zielwert "Target" hat. Die geringe Korrelation zeigt deutlich, dass die Abhängigkeit zwischen diesen Variablen für diese Daten vernachlässigbar ist.</p>
        
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_location_target }}</p>
        <p>Die Kovarianz {corr_cov_location_target['covariance']:.2f} indicates a stronger positive relationship between the variables (but the absolute value depends on the data's scale).<p>
        <p>Für die Beziehung zwischen "Location" und "Target" ergibt sich eine Kovarianz von {corr_cov_location_target['covariance']:.2f} und eine Korrelation von {corr_cov_location_target['correlation']:.2f}. Die negative Kovarianz deutet auf eine gegenläufige Beziehung hin, das heißt, dass höhere Werte in "Location" mit einer Tendenz zu niedrigeren Werten in "Target" verbunden sein könnten. Dennoch ist die Korrelation mit {corr_cov_location_target['correlation']:.2f} so gering, dass praktisch keine lineare Beziehung zwischen diesen beiden Variablen besteht. Die negative Kovarianz allein liefert keinen starken Hinweis auf einen Zusammenhang, da sie stark von der Skalierung der Daten abhängt und durch die geringe Korrelation weiter relativiert wird.</p>
        
        <h3>--- Zusammenfassung ---</h3>
        <p>Zusammenfassend zeigt die Analyse der Korrelation und Kovarianz, dass weder "Keyword" noch "Location" eine signifikante lineare Beziehung zu "Target" aufweisen. Beide Korrelationen sind sehr nah an 0, was darauf hinweist, dass Änderungen in diesen Variablen keinen starken Einfluss auf den Zielwert haben. Die Ergebnisse deuten darauf hin, dass weder "Keyword" noch "Location" entscheidende Faktoren für die Vorhersage von "Target" sind. Darüber hinaus sollte berücksichtigt werden, dass die Kovarianz abhängig von der Skalierung der Daten ist, während die Korrelation eine normierte Maßzahl darstellt, die unabhängig von den Einheiten der Variablen interpretiert werden kann. Daher bestätigen die schwachen Korrelationen letztendlich die mangelnde Relevanz dieser beiden Variablen in Bezug auf den Zielwert.</p>
    </section>

    <section id="graphen">
        <h2>Graphen</h2>
        <p>{{ confidence_intervals }}</p>
        <p>{{ relative_frequency }}</p>
        
        <p>Wir wollen zuerst die Wordcloud für alle Beiträge visualisieren.</p>
        <img src="images/wordcloud_all.png" alt="Income Spending Scatterplot" width="400px" height="400px">
        <p>Beim ersten Blick auf den Graph fällt auf, dass bestimmte Begriffe wie „people“, „time“ und ähnliche häufig vorkommen. Dies könnte darauf hindeuten, dass die Beiträge in ihrer Wortwahl eher allgemein gehalten sind und nicht spezifisch auf Krisen oder dramatische Ereignisse eingehen.</p>
        
        <p>Vielleicht liegt es aber auch daran, dass es mehr irrelevante Beiträge gibt als relevante Beiträge. Dies werden wir jetzt analysieren indem wir die Anzahl der relevanten und irrelevanten Beiträge visualisieren.</p>
        <img src="images/target_pie_chart.png" alt="Target Pie Chart" width="400px" height="400px">
        <Wir merken, dass es mehr irrelevante Beiträge gibt als relevante Beiträge. Dies könnte erklären warum Wörter wie „people“ häufiger vorkommen.>
        
        <p>Wir analysieren also jetzt Wörter analysieren die häufig in irrelevanten Beiträgen vorkommen, um das zu bestätigen, kreieren wir die Wordcloud dazu.<p>
        <img src="images/wordcloud_irrelevant.png" alt="Income Spending Scatterplot" width="400px" height="400px">
        <p>Die Wortwolke der irrelevanten Beiträge zeigt eine ähnliche Verteilung wie die der allgemeinen Beiträge: Wörter wie „people“ erscheinen häufig und es gibt weniger ausgeprägte Unterschiede in der Häufigkeit der Begriffe. Dies könnte darauf hindeuten, dass diese Beiträge nicht auf ein konkretes oder dringendes Thema fokussiert sind.</p>        
    
        <p>Wenn wir uns nun nur die relevanten Beiträge anschauen, zeigt sich ein anderes Bild: Wörter wie „fire“ „killed“ oder „australia“ treten häufiger auf. Das deutet darauf hin, dass diese Beiträge oft spezifisch auf Krisenereignisse, wie etwa Waldbrände in Australien, eingehen und weniger allgemeiner Natur sind.</p>
        <img src="images/wordcloud_relevant.png" alt="Income Spending Scatterplot" width="400px" height="400px">
     </section>

    <section id="tests">
        <h2>Tests</h2>
        <h3>T-Test</h3>
        <p><strong> Nullhypothese (𝐻0): Es gibt keinen signifikanten Unterschied in der durchschnittlichen Textlänge zwischen relevanten und irrelevanten Beiträgen. <br> 
        Alternativhypothese (𝐻𝐴): Es gibt einen signifikanten Unterschied in der durchschnittlichen Textlänge zwischen relevanten und irrelevanten Beiträgen. </strong></p>
        <p>{{ ttest }}</p>
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
