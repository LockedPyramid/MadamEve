import discord
from discord.ext import commands
import os
import ApiCaller
import reprocess
import settings
import random

# Create an instance of the bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)





@bot.command(name='Price')
async def Price(ctx, Market, Percent, *, items):
    
    
    try:
        Call = ApiCaller.Call(None, Market, Percent, items)
        print(Call)
        await ctx.send(f""" Market: {Call["Market"]}     Percent: {Call["Percent"]}     Volume: {Call["Volume"]}
                   
Buy: {Call["Buy"]}
Sell: {Call["Sell"]}
Split: {Call["Split"]}""")
    except Exception as e: 
        await ctx.send("An error occurred, please try again")
        print(e.args[0])
    
@bot.command(name='Repo')
async def Price(ctx, Market, MarketPercent, RatePercent, *, items):
    
    try:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f""" Market: {Call["Market"]}     Percent: {Call["Percent"]}     Volume: {Call["Volume"]}
                   
Buy: {Call["Buy"]}
Sell: {Call["Sell"]}
Split: {Call["Split"]}""")
    
    except Exception as e: 
        await ctx.send("An error occurred, please try again")
        print(e.args[0])

@bot.command(name='RepoSell')
async def RepoSell(ctx, Market, MarketPercent, RatePercent, *, items):
    
    try:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f"""Sell: {Call["Sell"]}""")
    except Exception as e: 
        await ctx.send(e.args[0])
        print(e.args[0])
    
@bot.command(name='RepoBuy')
async def RepoBuy(ctx, Market, MarketPercent, RatePercent, *, items):
    
    try:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f"""Buy: {Call["Buy"]}""")
    except Exception as e: 
        await ctx.send("An error occurred, please try again")
        print(e.args[0])

@bot.command(name='sell')
async def sell(ctx, *, items):
    
        RepressedItems = reprocess.Call(ctx, 82.93, str(items).lower())
        print(RepressedItems)
        Call = ApiCaller.Call(None, 2, 90, RepressedItems)
        print(Call)
        await ctx.send(f"""Contract to Yvftu for {Call["Buy"]} ISK""") 

@bot.command(name='see')
async def see(ctx, *, items):
    if items == "DEEZ NUTS":
        await ctx.send(f"""Suck on these you cunt! O O""") 
    if items == "boobz":
        randomNum = random()
        if randomNum > 0.9:
            await ctx.send("Here you go: (.Y.)")
        if randomNum < 0.9:
            await ctx.send("I am a minor you perve!")

# Run the bot with your token
bot.run(str(open("/home/ada/Janice/Storage/Discord.key").read()))
