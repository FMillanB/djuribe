import discord
from discord.ext import commands
from keep import seguir_vivito

from music import music_cog

Bot = commands.Bot(command_prefix="!")

@Bot.event
async def on_ready():
  activity = discord.Game(name="LO MEJOR EN GUARACHAS", type=3)
  await Bot.change_presence(status=discord.Status.idle, activity=activity)
  print("URIBE LISTO Y PREPARADO")


Bot.add_cog(music_cog(Bot))

token = "ODg0NTUxMjAyMDEwOTY4MTQ0.YTaIgA.bMUtsGjWos9QQMicWVKlLizS8po"

seguir_vivito()
Bot.run(token)


  