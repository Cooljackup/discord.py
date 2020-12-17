import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Python develop."))
    print('Bot is online and ready.')

@bot.command()
async def ping(command):
    await command.send(f'Pong! Latency is {round(bot.latency * 1000)}ms.')
    pass


@bot.command()
async def hello(command):
    await command.send('Hello!')
    pass


bot.run('token')