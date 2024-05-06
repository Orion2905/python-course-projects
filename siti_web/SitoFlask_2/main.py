from flask import Flask
import random

app = Flask(__name__)

lista_fatti = [
    "La maggior parte delle persone che soffrono di dipendenza tecnologica sperimentano un forte stress quando si trovano al di fuori dell'area di copertura della rete o non possono utilizzare i loro dispositivi",
    "Secondo uno studio condotto nel 2018, più del 50% delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone",
    "Lo studio della dipendenza tecnologica è una delle aree più rilevanti della ricerca scientifica moderna",
    "Secondo uno studio del 2019, oltre il 60% delle persone risponde ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro.",
    "Un modo per combattere la dipendenza tecnologica è cercare attività che portino piacere e migliorino l'umore",
    "Elon Musk sostiene che i social network sono progettati per tenerci all'interno della piattaforma, in modo che trascorriamo il maggior tempo possibile a guardare contenuti",
    "Elon Musk è anche favorevole alla regolamentazione dei social network e alla protezione dei dati personali degli utenti. Sostiene che i social network raccolgono un'enorme quantità di informazioni su di noi, che possono essere utilizzate per manipolare i nostri pensieri e comportamenti",
    "I social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme.",
]

@app.route("/")
def index():
    return f'<h1>Ciao! In questa pagina puoi scoprire un paio di fatti interessanti sulle dipendenze tecnologiche!</h1><a href="/fatto_casuale">Vedi un fatto casuale!</a>'

@app.route("/fatto_casuale")
def fatti():
    return f"<p>{random.choice(lista_fatti)}</p>"

app.run(debug=True)