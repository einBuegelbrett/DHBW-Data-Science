kunden_template = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datenanalyse-Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; }
        h1, h2 { color: #333; }
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
            <li>Mapping von Gender zu Integers</li>
        </ul>
        <p>Der Datensatz nach der Bereinigung sieht wie folgt aus:</p>
        <p>{{ cleaning }}</p>
    </section>
    
    <section id="statistiken">
        <h2>Statistiken</h2>
        {{ statistics }}
    </section>
    
    <section id="income_spending">
        <h2>Korrelation und Kovarianz</h2>
        <h3> Korrelation und Kovarianz zwischen Alter und Einkommen</h3>
        <p>{{corr_cov_age_income}}</p>
        <p> Die Kovarianz, zeigt eine leichte gemeinsame Streuung der beiden Variablen,
            was bedeutet, dass sie sich in die gleiche Richtung bewegen.<br>
            Die Stärke und Richtung der Beziehung wird dadurch aber nicht deutlich.<br>
            Die Korrelation, deutet darauf hin dass es keinen linearen Zusammenhang zwischen Alter und Einkommen gibt.
        </p>
            
        <h3> Korrelation und Kovarianz zwischen Alter und Ausgabenverhalten</h3>
        <p>{{corr_cov_age_spending}}</p>
        <p> Mit zunehmendem Alter scheint das Einkommen kaum beeinflusst zu werden, 
            da der Zusammenhang äußerst schwach ist. <br>
            Alter und Einkommen weitgehend unabhängig voneinander sind.
            Die Kovarianz, zeigt eine leichte gemeinsame Streuung der beiden Variablen,
            was bedeutet, dass sie sich in die gleiche Richtung bewegen.<br>
            Die Stärke und Richtung der Beziehung wird dadurch aber nicht deutlich.<br>
            Die Korrelation, deutet darauf hin dass es keinen linearen Zusammenhang zwischen Alter und Ausgabenverhalten gibt.
        </p>
            
        <h4> Korrelation und Kovarianz zwischen Einkommen und Ausgabenverhalten</h4>    
        <p>{{ correlation_covariance }}</p>
        <p> Mit zunehmendem Alter geben Menschen tendenziell weniger aus, 
            aber diese Beziehung ist nicht sehr stark. <br>
            Es gibt wahrscheinlich noch andere Faktoren, die das Ausgabenverhalten beeinflussen.
        </p>
            
        <img src="images/income_spending.png" alt="Income Spending Scatterplot" width="400px" height="400px">
        <p> Der Scatterplot zeigt deutlich unterschiedliche Cluster in den Daten: <br>
            Ein großes, zentrales Cluster, das viele Datenpunkte im Bereich von mittlerem Einkommen (40-60 k$) 
            und mittlerem Spending Score (40-60) umfasst.<br>
            Vier kleinere Cluster, in den jeweiligen Ecken verteilt sind: 
            Die Verteilung zeigt deutlich segmentiertes Verhalten, was auf verschiedene Kundengruppen oder 
            Marktsegmente hinweist. 
        </p>
        <br>
        <p> Zusammenfassend lässt sich sagen, dass die numerischen Ergebnisse von Korrelation und Kovarianz mit dem Scatterplot übereinstimmen:<br>
            Es gibt keinen linearen Zusammenhang zwischen Einkommen und Ausgabeverhalten, welcher aussagekräftig genug ist, um eine klare Beziehung zu erkennen.<br>
            Die Cluster im Scatterplot zeigen jedoch eine segmentierte Population, die sich in fünf Gruppen unterteilen lässt.
            Dies deutet darauf hin, dass andere Faktoren das Ausgabeverhalten beeinflussen. 
        </p>
    </section>


    <section id="boxplot">
        <h2>--- Evaluation: Boxplot ---</h2>
        <img src="images/Boxplot_Income_Gender.png" alt="Income_Gender_Boxplot" width="400px" height="400px">
        <p> Der Boxplot zeigt die Verteilung des Einkommens nach Geschlecht. <br>
            Es ist zu erkennen, dass die Verteilung des Einkommens bei Männern und Frauen sehr ähnlich ist,
            was auf ein vergleichbares mittleres Einkommen hinweist.
            Wobei Frauen tendenziell ein niedrigeres mittleres Einkommen haben als Männer, um rund 2k$. 
            Auch der Interquartilsabstand (IQR) ist in beiden Gruppen ähnlich und zeigt eine ähnliche Streuung. 
            Abgesehen davon zeigen die Whiskers, die die minimalen und maximalen Werte der Daten ohne Ausreißer darstellen, für beide Gruppen gleiche Spannweiten.
            Ein Ausreißer oberhalb des oberen Whiskers ist nur in der Gruppe für das "Männliche" Geschlecht zu sehen, was auf ein besonders hohen Einkommen hinweist.
            Insgesamt ist die Verteilung des Einkommens bei Männern und Frauen relativ ähnlich. 
        </p> 
    </section>

    <section id="tests">
        <h2>Tests</h2>
        <h3>--- Evaluation: Normalverteilungstest ---</h3>
        <p>{{ normality_test }}</p>
        <p> Die Normalitätstests für alle drei Variablen (Alter, jährliches Einkommen und Ausgabeverhalten) zeigen, 
            dass sie nicht normalverteilt sind. Beim Alter, dem Einkommen und dem Ausgabeverhalten weisen die Tests jeweils darauf hin, 
            dass diese Variablen von einer normalen Verteilung abweichen. Das bedeutet, dass die Verteilungen in den Daten entweder asymmetrisch oder schief sind 
            oder andere Merkmale aufweisen, die eine normale Verteilung nicht widerspiegeln. 
            Dies hat Auswirkungen auf die Auswahl der statistischen Methoden, die für die weitere Analyse verwendet werden sollten, da viele Verfahren die Annahme der Normalverteilung voraussetzen.
        </p>
        
        <h4> Entscheidung für Chi-Square Test</h4>
        <p> Basierend auf den Ergebnissen der Normalitätstests zeigte sich, dass keine der betrachteten Variablen (Alter, Jahreseinkommen und Ausgabenscore) normalverteilt ist, wie die extrem niedrigen p-Werte der Shapiro-Wilk-Tests nahelegen. 
            Da der T-Test die Voraussetzung der Normalverteilung nicht erfüllt und ebenso eine Fehlermeldung durch zu kleine Stichproben wirft, wurde sich für den Chi-Quadrat-Test entschieden. 
            Dieser Test setzt keine Normalverteilung der Daten voraus und ist daher besser geeignet, um die Abhängigkeiten zwischen kategorialen Variablen zu untersuchen.
        </p>
        
        <h3>--- Evaluation: Chi-Square-Test ---</h3>
        <p><strong> Nullhypothese (H0): Es gibt keinen signifikanten Zusammenhang zwischen dem Geschlecht und der Ausgabenkategorie (hoch, mittel, niedrig). <br>
                    Alternativhypothese (HA): Es gibt einen signifikanten Zusammenhang zwischen dem Geschlecht und der Ausgabenkategorie. </strong></p>
        <p> {{ chi_square_test }}</p>
        <p> Die Ergebnisse zeigen einen Chi-Quadrat-Wert von 0.656, einen p-Wert von 0.720 und 2 Freiheitsgrade. 
            Da der p-Wert größer als das Signifikanzniveau von 0.05 ist, wird die Nullhypothese, dass kein signifikanter Zusammenhang zwischen den Variablen besteht, beibehalten und dementsprechend abgelehnt wird. 
            Die erwarteten Häufigkeiten zeigen keine auffälligen Abweichungen, sodass kein statistisch signifikanter Einfluss des Geschlechts auf die Ausgabenkategorien nachgewiesen werden kann. 
        </p>
    </section>

    <section id="ml">
        <h2>--- Evaluation: K-Nearest Neighbors (KNN) ---</h2>
        <p>{{ knn_classifier_evaluate_model }}</p>
        <p>Der KNN-Classifier zeigt eine herausragende Leistung bei der Klassifikation der Daten mit einer Genauigkeit von 95%. 
            Neben der hohen Genauigkeit sind auch die weiteren Metriken – Precision, Recall und F1-Score – jeweils mit 95% auf einem sehr hohen Niveau. 
            Dies deutet darauf hin, dass das Modell sowohl zuverlässig bei der Erkennung der tatsächlichen Klassen (Recall) als auch präzise bei der Vorhersage der Klassen (Precision) ist. 
            Der harmonische Mittelwert dieser beiden Metriken, der F1-Score, bestätigt eine ausgewogene Modellleistung.
        </p>
    </section>

    <section id="hyperparametertuning">
        <h4>Hyperparametertuning</h4>
        <p>{{ hyperparameter_tuning }}</p>
        <p> Das Hyperparameter-Tuning hat die besten möglichkeiten für das Modell gefunden. Die besten Parameter beinhalten die Verwendung der euklidischen Distanz als Maßzahl zur Berechnung der Abstände,
        die Betrachtung der 5 nächsten Nachbarn und gleichmäßige Gewichtung dieser Nachbarn. Dieses gezielte Hyperparameter-Tuning hat wesentlich dazu beigetragen, die Leistung des Modells zu maximieren.
        </p>
    </section>
    
    <img src="images/knn_confusion_matrix.png" alt="KNN Confusion Matrix" width="600px" height="600px">
    <p> Die Confusion-Matrix liefert eine detaillierte Analyse der Modellvorhersagen und zeigt, dass die meisten Datenpunkte korrekt klassifiziert wurden.
        Es treten nur Fehler zwischen den Klassen „Low“ und „Medium“ auf, was darauf hindeutet, dass diese beiden Kategorien in den Daten möglicherweise Ähnlichkeiten aufweisen, die die Unterscheidung erschweren könnten.
    </p>
    
    <p> Zusammenfassend lässt sich sagen, dass der KNN-Classifier optimal auf die vorliegenden Daten abgestimmt ist und nur sehr wenige Fehler macht. 
    Dies spricht für eine gelungene Datenaufbereitung sowie eine effektive Modellanpassung. 
    Die Ergebnisse bestätigen, dass der KNN-Algorithmus in diesem Fall eine geeignete Wahl für die Klassifikationsaufgabe ist.
    </p>
</body>
</html>
"""
