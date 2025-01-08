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
        <h2>Vergleich Einkommen und Ausgabeverhalten</h2>
        <h4>Korrelation und Kovarianz</h4>
        <p>{{ correlation_covariance }}</p>
        <p>{{ correlation_covariance_interpretation }}</p>
        <h4>Visualisierung mit Scatterplot</h4>
        <img src="images/income_spending.png" alt="Income Spending Scatterplot" width="400px" height="400px">
        <p>{{ scatterplot_interpretation }}</p>
    </section>

    <section id="graphen">
        <h2>Graphen</h2>
        <p>{{ graphs }}</p>
    </section>

    <section id="tests">
        <h2>Tests</h2>
        <p>{{ tests }}</p>
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
