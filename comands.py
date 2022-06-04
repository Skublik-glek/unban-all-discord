import discord
from discord import utils

from vars import bot


@bot.command()
async def unbanall(ctx):
    bans = await ctx.guild.bans()
    for ban in bans:
        user: discord.User = ban[1]
        guild: discord.Guild = ctx.guild
        await guild.unban(user)