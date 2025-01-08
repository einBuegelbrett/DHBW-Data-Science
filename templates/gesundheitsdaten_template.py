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
        
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_location_target }}</p>
        <p><p>
        
        <h3>--- Analyse der Korrelation und Kovarianz ---</h3>
        <p>{{ corr_cov_location_target }}</p>
        <p><p>
    </section>

    <section id="graphen">
        <h2>Graphen</h2>
        <p>{{ graphs }}</p>
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
