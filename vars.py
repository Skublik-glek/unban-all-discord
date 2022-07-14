import discord
from discord import message
from discord.ext import commands
import sqlite3


TOKEN = ""

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=('!'), intents=intents)

bot.remove_command('help')

tdict = {}
