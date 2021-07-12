import discord
from discord import channel
from discord.ext import commands

bot = commands.Bot(command_prefix='a!')

@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_all_channel(769876063839846401)
    await channel.send(f'{member} join!')

bot.run('ODYzODY4NjM4MDI5NDE0NDAx.YOtKXQ.4EheBiWeKs_XuBOEQlHtZblYCXs')