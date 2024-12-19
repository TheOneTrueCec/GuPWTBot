import os
import configparser
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import json


#Referenced Files
import nickNames

#Instantiation
if __name__ == "__main__":

    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")

    config = configparser.ConfigParser()
    config.read("./.config")

    ADMINS = json.loads(config.get("General","admins"))
    COMPARAM = json.loads(config.get("General", "param"))

    intents = discord.Intents.default()
    intents.message_content = True
    Client = commands.Bot(command_prefix='$', intents=intents)

@Client.event
async def on_ready():
    print(f'We have logged in as {Client.user}')
    await Client.tree.sync(guild=discord.Object(id=830305706573561876))
    print("---Ready---")

#PureMessageParse
@Client.event
async def on_message(message: discord.message.Message):
    if message.author == Client.user:
        return

#Commands
@Client.tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=830305706573561876)
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

#AutoLooped Task
@tasks.loop(minutes=1)
async def refreshDatabase():
    Client.cha
    return


Client.run(TOKEN)