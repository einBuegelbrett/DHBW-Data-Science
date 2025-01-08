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
        <p>{{ initial_dataset }}</p>
    </section>

    <section id="nach-cleaning">
        <h2>Nach Cleaning</h2>
        <p>{{ cleaning }}</p>
    </section>

    <section id="korrelation-kovarianz">
        <h2>Korrelation / Kovarianz</h2>
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_maximaleHerzfrequenz_alter }}</p>
        <p><p>
        
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_ruheblutdruck_cholesterinwert }}</p>
        <p><p>
        
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_blutzucker_cholesterinwert }}</p>
        <p><p>
        
        <h2>Mögliche Zusammenhänge zwischen den unabhängigen Variablen und der Zielvariable, höchsten und niedrigsten Korrelation</h2>
        
        <h3>--- Analyse der Korrelation und Kovarianz (max) ---</h3>
        <p>{{ max_correlation_column }}</p>
        <p><p>
        
        <h3>--- Analyse der Korrelation und Kovarianz (min) ---</h3>
        <p>{{ min_correlation_column }}</p>
        <p><p>
    </section>

    <section id="graphen">
        <h2>Graphen</h2>
        <h3>Untersuchung der Verteilung der numerischen Variablen</h3>
        <img src="images/Alter.png" alt="Histogram of Alter" width="400px" height="400px">
        <img src="images/Geschlecht.png" alt="Histogram of Geschlecht" width="400px" height="400px">
        <img src="images/Brustschmerz-Typ.png" alt="Histogram of Brustschmerz-Typ" width="400px" height="400px">
        <img src="images/Ruheblutdruck.png" alt="Histogram of Ruheblutdruck" width="400px" height="400px">
        <img src="images/Cholesterinwert.png" alt="Histogram of Cholesterinwert" width="400px" height="400px">
        <img src="images/Blutzucker.png" alt="Histogram of Blutzucker" width="400px" height="400px">
        <img src="images/EKG.png" alt="Histogram of EKG" width="400px" height="400px">
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
        <p>{{ ml }}</p>
    </section>

    <section id="hyperparametertuning">
        <h2>Hyperparametertuning</h2>
        <p>{{ hyperparameter_tuning }}</p>
    </section>
</body>
</html>
"""
