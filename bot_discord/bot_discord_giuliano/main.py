import discord
from discord.ext import commands
import random , os
import time

intents = discord.Intents.default()
intents.message_content = True
# Inizializzazione del bot di discord test
bot = commands.Bot(command_prefix='!', intents=intents)

# Definisci il messaggio da inviare quando il bot è pronto
async def send_message_on_ready():
    # Recupera il canale in cui inviare il messaggio (modifica l'ID del canale come necessario)
    channel = bot.get_channel("1158791560675205133")
    # Invia il messaggio nel canale
    await channel.send("Sono il bot ecologico! Ponimi domande inerenti l'ambiente con i seguenti richiami  !ecologia, !articoli, !riciclo e grazie per il supporto!")

# Evento di avvio del bot
@bot.event
async def on_ready():
    print('Bot avviato come', bot.user)
    await send_message_on_ready()

@bot.command()
async def meme(ctx):
    images = os.listdir('images')
    random_image = random.choice(images)
    with open(f"images/{random_image}", "rb") as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)

async def articoli(ctx):
    articles= os.listdir('articles')
    random_article= random.choice(articles)
    with open(f"articles/{random_article}", "rb" ) as f:
        picture= discord.File(f)

    await ctx.send(file=picture)

async def ecologia(ctx):
    impronta=(input("cosa ti interessa sapere a riguardo?"))
    if impronta== ecologia:
        await ctx.send("potresti ricercare più informazioni su questo sito")
        time.sleep(2)
        await ctx.send("GEOPOP- https://www.geopop.it/")
    else:
        ctx.send("non disponiamo ancora di documenti certi, prova a rispondere alla domanda con la parola ecologia, ti divertirai un mondo ;) ")

async def riciclo(ctx):
    ricicliamo=(input("cosa ti interessa sapere a riguardo?"))
    if ricicliamo== riciclo:
        await ctx.send("potresti ricercare più informazioni su questo sito")
        time.sleep(2)
        await ctx.send("WIKIHOW- https://www.wikihow.it/Riciclare")
    else:
        ctx.send("non disponiamo ancora di documenti certi, prova a rispondere alla domanda con la parola riciclo, ti divertirai un mondo ;) ")
    



bot.run("La tua chiave qui")