"""new code"""
import nextcord
import discord
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from nextcord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')
    
@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')
    await bot.change_presence(activity=nextcord.CustomActivity(name="Hi harvici"),status='online')

if __name__ == '__main__':
    bot.run("")

"""new code"""
