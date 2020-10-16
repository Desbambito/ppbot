import discord
from discord.ext import commands

pp = commands.Bot(command_prefix='pp')

@pp.event
async def on_ready():
    print("Bot Started")

@pp.command()
async def ping(ctx):
    await ctx.send("pong")

pp.run('NzY2NDY2MjUxMDczMzg4NTc0.X4jxUg.Np2NpHQHNePySnPuG5Nq-P2hd5I')