import discord
from discord.ext import commands
import random
import requests


intents = discord.Intents.default()
intents.message_content = True
# Inizializzazione del bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Lista di consigli su come non inquinare
consigli = [
    "Riduci l'uso di plastica monouso, preferisci materiali riutilizzabili.",
    "Ricicla carta, plastica, vetro e metallo per ridurre i rifiuti.",
    "Utilizza mezzi di trasporto pubblici o bicicletta quando possibile per ridurre le emissioni di gas serra.",
    "Risparmia energia spegnendo luci e dispositivi non necessari.",
    "Preferisci prodotti biodegradabili e amici dell'ambiente.",
    "Partecipa a iniziative di pulizia dell'ambiente nella tua comunità.",
    "Riduci lo spreco alimentare consumando in modo consapevole e pianificando gli acquisti.",
    "Evita l'utilizzo e lo smaltimento improprio di prodotti chimici nocivi.",
    "Informa e sensibilizza gli altri sull'importanza di preservare l'ambiente.",
    "Mantieni pulite le strade e i parchi, non gettare rifiuti per terra."
]

# Dizionario che mappa il nome del rifiuto al luogo di smaltimento
smaltimento_rifiuti = {
    "plastica": "Nel contenitore per la plastica.",
    "carta": "Nel contenitore per la carta.",
    "vetro": "Nel contenitore per il vetro.",
    "organico": "Nel contenitore per l'organico.",
    "alluminio": "Nel contenitore per l'alluminio.",
    "batterie": "Negli appositi contenitori per le batterie.",
    "pile": "Negli appositi contenitori per le pile.",
    "elettronica": "Presso un centro di raccolta elettronica autorizzato.",
    "indifferenziato": "Nel contenitore per i rifiuti indifferenziati.",
    # Aggiungi altri rifiuti e i relativi metodi di smaltimento qui
}

# Comando per ottenere un consiglio su come non inquinare
@bot.command()
async def consiglio(ctx):
    consiglio = random.choice(consigli)
    await ctx.send(consiglio)

    # Chiamata all'API di Picsum per ottenere un'immagine casuale
    url = "https://picsum.photos/1200/800"
    await ctx.send(url)

# Evento di avvio del bot
@bot.event
async def on_ready():
    print('Bot avviato come', bot.user)

# Comando per ottenere informazioni sullo smaltimento di un rifiuto
@bot.command()
async def smaltisci(ctx, *, rifiuto):
    rifiuto = rifiuto.lower()  # Converti il nome del rifiuto in minuscolo per la corrispondenza esatta
    if rifiuto in smaltimento_rifiuti:
        messaggio = f"Per smaltire il rifiuto '{rifiuto}', buttalo: {smaltimento_rifiuti[rifiuto]}"
    else:
        messaggio = f"Mi dispiace, non ho informazioni su come smaltire il rifiuto '{rifiuto}'."
    
    await ctx.send(messaggio)

# Token del bot Discord
bot.run('La tua chiave qui')