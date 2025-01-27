import discord
import random
import os
import requests

from discord.ext import commands
from app import gen_pass

#configuracion
intenciones=discord.Intents.default()
intenciones.message_content=True

bot = commands.Bot(command_prefix="/",intents=intenciones)

@bot.event
async def  on_ready():
    print("El bot ya arranca :v")

@bot.command()
async def hola(ctx):
    await ctx.send(f"Ola papu como estas {ctx.author.name} :V?")

@bot.command()
async def comandos(ctx):
    await ctx.send(f"Solo hay 12 comandos por ahora, intenta, /hola /generador")

@bot.command()
async def amogus(ctx):
    await ctx.send(f"No.")   

@bot.command()
async def generador(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(10)}")

@bot.command()
async def spam(ctx, count_spam = 5):
    await ctx.send("spam" * count_spam)

@bot.command()
async def chistes(ctx):
    await ctx.send("No me se hacer chistes")

@bot.command()
async def momobarato1(ctx):
    with open('chatbot\img\momo1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def momobarato2(ctx):
    with open('chatbot\img\momo2.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def momobarato3(ctx):
    with open('chatbot\img\momo3.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def momobarato4(ctx):
    with open('chatbot\img\momo4.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def momoaleatorio(ctx):
    listaMomos=os.listdir('chatbot/img')
    with open(f'chatbot\img\{random.choice(listaMomos)}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)                 

def dame_la_url_de_un_perro():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función dame_la_url_de_un_perro'''
    image_url = dame_la_url_de_un_perro()
    await ctx.send(image_url)                      
    
bot.run("")

