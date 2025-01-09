gesundheitsdaten_template = """
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
            <li>Mapping von allen Spalten zu Integers</li>
        </ul>
        <p>Der Datensatz nach der Bereinigung sieht wie folgt aus:</p>
        <p>{{ cleaning }}</p>
    </section>

    <section id="korrelation-kovarianz">
        <h2>Korrelation / Kovarianz</h2>
        <h3>--- Analyse der Korrelation und Kovarianz zwischen der Maximalen Herzfrequenz und dem Alter ---</h3>
        <p>{{ corr_cov_maximaleHerzfrequenz_alter }}</p>
        <p>Die negative Kovarianz und die Korrelation zeigen eine mäßig starke negative Beziehung zwischen der maximalen Herzfrequenz und dem Alter. 
        Das bedeutet, dass mit zunehmendem Alter die maximale Herzfrequenz tendenziell sinkt. 
        Die Beziehung ist jedoch nicht perfekt, es gibt also auch Ausnahmen von diesem Trend.</p>
        
        <h3>--- Analyse der Korrelation und Kovarianz zwischen dem Ruheblutdruck und Cholesterinwert---</h3>
        <p>{{ corr_cov_ruheblutdruck_cholesterinwert }}</p>
        <p>Die Kovarianz von -203.58 und die Korrelation von -0.22 weisen auf eine schwache negative Beziehung hin. 
        Dies deutet darauf hin, dass ein leichter Trend besteht, wonach Personen mit höherem Cholesterinwert tendenziell einen etwas niedrigeren Ruheblutdruck haben könnten.
        </p>
        
        <h3>--- Analyse der Korrelation und Kovarianz zwischen dem Blutzucker und dem Cholesterinwert---</h3>
        <p>{{ corr_cov_blutzucker_cholesterinwert }}</p>
        <p>Hier ist die Kovarianz mit 1.29 sehr niedrig, und die Korrelation von 0.06 zeigt praktisch keinen Zusammenhang zwischen Blutzucker und Cholesterinwert. 
        Dies deutet darauf hin, dass die beiden Variablen weitgehend unabhängig voneinander sind. 
        Eine Vorhersage des Cholesterinwerts anhand des Blutzuckerspiegels oder umgekehrt wäre somit kaum möglich.
        </p>
        
    </section>

    <section id="graphen">
        <h2>Graphen</h2>
        <h3>Untersuchung der Verteilung der numerischen Variablen</h3>
        <img src="images/Ruheblutdruck.png" alt="Histogram of Ruheblutdruck" width="400px" height="400px">
        <img src="images/Cholesterinwert.png" alt="Histogram of Cholesterinwert" width="400px" height="400px">
        <img src="images/MaximaleHerzfrequenz.png" alt="Histogram of MaximaleHerzfrequenz" width="400px" height="400px">
        <img src="images/Gesundheitszustand.png" alt="Histogram of Gesundheitszustand" width="400px" height="400px">
        
        <h3>Die 3 Spalten mit den größten Ausreißern sind:</h3>
        <ul>
            {{ top_outliers }}
        </ul>
        <img src="images/image_0.png" alt="Boxplot of {{ top_outliers[0].column }}" width="400px" height="400px">
        <img src="images/image_1.png" alt="Boxplot of {{ top_outliers[1].column }}" width="400px" height="400px">
        <img src="images/image_2.png" alt="Boxplot of {{ top_outliers[2].column }}" width="400px" height="400px">
    </section>

    <section id="tests">
        <h2>Tests</h2>
        <h3>Nullhypothese (H₀): Es gibt keinen Unterschied im Gesundheitsrisiko zwischen Männern und Frauen.</h3>
        <p>{{ ttest_Gesundheitszustand_Geschlecht }}</p>
        
        <h3>Nullhypothese (H₀): Es gibt keinen Unterschied im Gesundheitsrisiko zwischen den Altersgruppen.</h3>
        <p>{{ ttest_Gesundheitszustand_Alter }}</p>
        
        <h3>Nullhypothese (H₀): Es gibt keinen Unterschied im Ruheblutdruck zwischen Personen mit Risiko (Gesundheitszustand = 1) und ohne Risiko (Gesundheitszustand = 0).</h3>
        <p>{{ ttest_Ruheblutdruck_Gesundheitszustand }}</p>
        
        <h3>Nullhypothese (H₀): Es gibt keinen Unterschied im Cholesterinwert zwischen Personen mit Risiko (Gesundheitszustand = 1) und ohne Risiko (Gesundheitszustand = 0).</h3>
        <p>{{ ttest_Cholesterinwert_Gesundheitszustand }}</p>
    </section>

    <section id="ml">
        <h2>ml</h2>
        <h3>--- Evaluation: Logistic Regression ---</h3>
        <p>{{ logistic_regression_evaluate_model }}</p>
        
        <h3>--- Evaluation: Random Forest ---</h3>
        <p>{{ random_forest_evaluate_model }}</p>
        
        <h3>--- Evaluation: K-Nearest Neighbors (KNN) ---</h3>
        <p>{{ knn_classifier_evaluate_model }}</p>
    </section>

    <section id="hyperparametertuning">
        <h2>Hyperparametertuning</h2>
        <h3>--- Evaluation: Logistic Regression ---</h3>
        <p>{{ logistic_regression_best_params }}</p>
        
        <h3>--- Evaluation: Random Forest ---</h3>
        <p>{{ random_forest_best_params }}</p>
        
        <h3>--- Evaluation: K-Nearest Neighbors (KNN) ---</h3>
        <p>{{ knn_classifier_best_params }}</p>
    </section>
    
    <section id="zusaetzlicheanalyse">
        <h2>Zusätzliche Analyse</h2>
        <p>{{ mehranalyse }}</p>
    </section>
</body>
</html>
"""
