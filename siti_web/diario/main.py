#Importare le librerie
from flask import Flask, render_template,request, redirect
#Collegare la libreria del database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Connettere SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#creare il db
db = SQLAlchemy(app)
#Creare una tabella

#Consegna #1. Creare un db
class Card(db.Model):
    #Creazione di campi colonna
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Titolo
    title = db.Column(db.String(100), nullable=False)
    #Descrizione
    subtitle = db.Column(db.String(300), nullable=False)
    #Testo
    text = db.Column(db.Text, nullable=False)

    #Produrre l'oggetto e la sua rappresentazione
    def __repr__(self):
        return f'<Card {self.id}>'


#Esecuzione della pagina con il contenuto
@app.route('/')
def index():
    #Emissione degli oggetti dal DB
    #Consegna #2. Fare in modo che gli oggetti del DB siano visualizzati in index.html
    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html', cards=cards)

#Esecuzione della pagina con la scheda
@app.route('/card/<int:id>')
def card(id):
    #Assignment #2. Use the id to show the right card
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Esecuzione della pagina con inizializzazione della scheda
@app.route('/create')
def create():
    return render_template('create_card.html')

#Il modulo della carta
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Creare un oggetto da passare al DB

        #Consegna #2. Creare un modo per memorizzare i dati nel DB
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
