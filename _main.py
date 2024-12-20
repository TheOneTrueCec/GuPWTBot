import os
import configparser
import discord
from discord.ext import tasks, commands
import discord.ext.commands
from dotenv import load_dotenv
import json


#Referenced Files
import discord.ext
import nickNames
import ImageCache

#Constants
FILEPATH = os.path.dirname(__file__)


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
    await Client.tree.sync(guild=discord.Object(id=811763650258927636))
    cacheHeatmap.start()
    print("---Ready---")

#PureMessageParse
@Client.event
async def on_message(message: discord.message.Message):
    if message.author == Client.user:
        return

#Commands
@Client.tree.command(
    name="heatmap",
    description="Arguments to be added",
    guild=discord.Object(id=811763650258927636)
)
async def first_command(interaction: discord.interactions.Interaction):
    file=discord.File("./ImageCache/brHeatMapGRB.png", filename="brHeatMapGRB.png")
    embed = discord.Embed(
        title="Ground RB Heatmap",
        color=discord.Color.random()
    ).set_image(
        url="attachment://brHeatMapGRB.png"
    )
    await interaction.response.send_message(embed=embed, file=file)

#AutoLooped Tasks
@tasks.loop(minutes=1)
async def refreshDatabase():
    return

@tasks.loop(hours=24)
async def cacheHeatmap():
    ImageCache.ImCache()
    return

Client.run(TOKEN)