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
        <p>{{ initial_dataset }}</p>
    </section>

    <section id="nach-cleaning">
        <h2>Nach Cleaning</h2>
        <p>{{ cleaning }}</p>
    </section>
    
    <section id="statistiken">
        <h2>Statistiken</h2>
        {{ statistics }}
    </section>
    
    <section id="income_spending">
        <h2>Korrelation und Kovarianz</h2>
        <h4> Korrelation und Kovarianz zwischen Alter und Einkommen</h4>
        <p>{{corr_cov_age_income}}</p>
        <p> Die Kovarianz, zeigt eine leichte gemeinsame Streuung der beiden Variablen,
            was bedeutet, dass sie sich in die gleiche Richtung bewegen.<br>
            Die Stärke und Richtung der Beziehung wird dadurch aber nicht deutlich.<br>
            Die Korrelation, deutet darauf hin dass es keinen linearen Zusammenhang zwischen Alter und Einkommen gibt.
        </p>
            
        <h4> Korrelation und Kovarianz zwischen Alter und Ausgabenverhalten</h4>
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
            
        <h6>Visualisierung mit Scatterplot</h6>
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
        <h2>Boxplot</h2>
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
        <h4> Normalverteilungstest</h4>
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
        
        <h4> Chi-Square Test</h4>
        <p><strong> Nullhypothese (𝐻0): Es gibt keinen signifikanten Zusammenhang zwischen dem Geschlecht und der Ausgabenkategorie (hoch, mittel, niedrig). <br>
                    Alternativhypothese (𝐻𝐴): Es gibt einen signifikanten Zusammenhang zwischen dem Geschlecht und der Ausgabenkategorie. </strong></p>
        <p> {{ chi_square_test }}</p>
        <p> Die Ergebnisse zeigen einen Chi-Quadrat-Wert von 0.656, einen p-Wert von 0.720 und 2 Freiheitsgrade. 
            Da der p-Wert größer als das Signifikanzniveau von 0.05 ist, wird die Nullhypothese, dass kein signifikanter Zusammenhang zwischen den Variablen besteht, beibehalten und dementsprechend abgelehnt wird. 
            Die erwarteten Häufigkeiten zeigen keine auffälligen Abweichungen, sodass kein statistisch signifikanter Einfluss des Geschlechts auf die Ausgabenkategorien nachgewiesen werden kann. 
        </p>
    </section>

    <section id="nlp-ml">
        <h2>nlp / ml</h2>
        <p>{{ nlp_ml }}</p>
    </section>

    <section id="hyperparametertuning">
        <h2>Hyperparametertuning</h2>
        <p>{{ hyperparameter_tuning }}</p>
    </section>
</body>
</html>
"""
