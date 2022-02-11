# Pycord packages
import discord
from discord.ext import commands


class Bot(commands.Bot):
  def __init__(self, *args, **kwargs):
    super.__init__(*args, **kwargs)
  async def on_ready(self):
    print("bot is online!")

#OPTIONAL COMMAND PREFIX
client = Bot(command_prefix="!")

@client.event
async def on_message(message):
  if message.content.startwith("Quel est ton prefixe?"):
    await message.channel.send("Mon prefixe est: ! mais vous n'avez pas besoin de l'utiliser.")
  if message.content.startwith("Quel temps fera-t-il demain?"):
    await message.channel.send("je n'en ai aucune idee")

 
client.run(token)
