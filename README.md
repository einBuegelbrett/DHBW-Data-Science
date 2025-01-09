# DHBW Data Science

## Gruppe
- Aziz Carducci (1965015)
- Sven Sendke (8469950)

## Projekt starten
Die Datei `main.py` muss nur ausgeführt werden. Es öffnet sich automatisch ein Fenster, in dem eine Datei ausgewählt werden kann, von der ein Bericht erstellt werden soll.
Die PDF-Datei die dadurch entsteht, heißt "report.pdf" und muss dann Manuell geöffnet werden
### Hinweis bei dem Starten
Auf Windows-basierten Systemen kann es vorkommen, dass das Programm nach dem Start erneut ausgeführt werden muss, damit sich das Dateiauswahlfenster korrekt öffnet.

## pip install
jinja2
pandas
scipy
matplotlib
seaborn
wordcloud
scikit-learn
transformers
xhtml2pdf
torch (https://pytorch.org/)
tk 

## Modularität
Um die Anwendung so modular wie möglich zu gestalten, wurde die Anwendung in verschiedene Klassen unterteilt, die alle unabhängig von ihrem Datensatz wiederverwendet werden können.

## Warnings
Die ML im Gesundheitsdatensatz funktioniert, als wir es getestet haben, schien es nicht zu funktionieren, weil es viele rote Warnungen gab, weil der Datensatz zu klein war. Es hat aber trotzdem funktioniert, man musste nur sehr lange warten, weil es sehr viele Berechnungen mit dem Hyperparameter-Tuning macht. Wir haben eine Fehlerbehandlung für den Fall implementiert, dass es doch nicht funktioniert.
Das Gleiche Problem mit dem Warnings ist auch bei dem Kundendatensatz mit dem K-Means Algorithmus, dieser Funktioniert, wirft aber eine Warning.

## Wichtiger Hinweis
Bei Linux basierten Systemen muss tkinter im voraus installiert werden:
- Ubuntu/Debian: 
```bash 
sudo apt-get install python3-tk
```
- Arch Linux: 
```bash 
sudo pacman -S tk
```
