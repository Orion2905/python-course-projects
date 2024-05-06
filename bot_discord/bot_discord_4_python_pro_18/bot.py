import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import create_actionrow, create_button
from discord_slash.model import ButtonStyle

import os, random
import requests

def get_random_duck():
    url = 'https://random-d.uk/api/random'
    response = requests.get(url)
    data = response.json()
    return data["url"]

intents = discord.Intents.default()
intents.message_content = True
# Inizializzazione del bot di discord test
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

# Evento di avvio del bot
@bot.event
async def on_ready():
    print('Bot avviato come', bot.user)

@bot.command()
async def meme(ctx):
    images = os.listdir('images')
    random_image = random.choice(images)
    with open(f"images/{random_image}", "rb") as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)

@slash.slash(name="domanda", description="Invia una domanda con due opzioni", guild_ids=["1158791560675205130"])
async def domanda(ctx: SlashContext):
    # Creazione dei bottoni
    bottoni = [
        create_button(style=ButtonStyle.blue, label="Opzione 1", custom_id="opzione1"),
        create_button(style=ButtonStyle.blue, label="Opzione 2", custom_id="opzione2")
    ]
    action_row = create_actionrow(*bottoni)
    
    # Invia il messaggio con i bottoni
    await ctx.send("Scegli un'opzione:", components=[action_row])

@bot.event
async def on_component(ctx):
    # Gestione delle interazioni con i bottoni
    if ctx.custom_id == "opzione1":
        await ctx.send(content="Hai scelto l'opzione 1!")
    elif ctx.custom_id == "opzione2":
        await ctx.send(content="Hai scelto l'opzione 2!")

@bot.command()
async def duck(ctx, **args):
    image_url = get_random_duck()
    await ctx.send(image_url)


@bot.command()
async def random_word(ctx, **args):
    word_list = ["ciao", "test", "agaaga"]
    word = random.choice(word_list)
    await ctx.send(f"Questa è la parola {word}")



bot.run("La tua chiave qui")