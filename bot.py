import discord
from discord.ext import commands
import os
import ApiCaller
import reprocess
import settings
import random
import StorageHandler

# Create an instance of the bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)





@bot.command(name='Price')
async def Price(ctx, Market, Percent, *, items):
    
    if not settings.Safety: 
        Call = ApiCaller.Call(None, Market, Percent, items)
        settings.Debug(Call)
        await ctx.send(f""" Market: {Call["Market"]}     Percent: {Call["Percent"]}     Volume: {Call["Volume"]}
                   
Buy: {Call["Buy"]}
Sell: {Call["Sell"]}
Split: {Call["Split"]}""")
        return
    
    try:
        Call = ApiCaller.Call(None, Market, Percent, items)
        settings.Debug(Call)
        await ctx.send(f""" Market: {Call["Market"]}     Percent: {Call["Percent"]}     Volume: {Call["Volume"]}
                   
Buy: {Call["Buy"]}
Sell: {Call["Sell"]}
Split: {Call["Split"]}""")
    except Exception as e: 
        await ctx.send("An error occurred, please try again")
        settings.Debug(e.args[0])
    
    
    
@bot.command(name='Repo')
async def Repo(ctx, Market, MarketPercent, RatePercent, *, items):
    
    if not settings.Safety:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f""" Market: {Call["Market"]}     Percent: {Call["Percent"]}     Volume: {Call["Volume"]}
                   
Buy: {Call["Buy"]}
Sell: {Call["Sell"]}
Split: {Call["Split"]}""")
        return
    
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
        settings.Debug(e.args[0])




@bot.command(name='RepoSell')
async def RepoSell(ctx, Market, MarketPercent, RatePercent, *, items):
    
    if not settings.Safety:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f"""Sell: {Call["Sell"]}""")
        return
    
    try:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f"""Sell: {Call["Sell"]}""")
    except Exception as e: 
        await ctx.send(e.args[0])
        settings.Debug(e.args[0])
    
    
    
    
@bot.command(name='RepoBuy')
async def RepoBuy(ctx, Market, MarketPercent, RatePercent, *, items):
    
    if not settings.Safety:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f"""Buy: {Call["Buy"]}""")
        return
    
    try:
        RepressedItems = reprocess.Call(ctx, RatePercent, items)
        await ctx.send(RepressedItems)
        Call = ApiCaller.Call(None, Market, MarketPercent, RepressedItems)
        await ctx.send(f"""Buy: {Call["Buy"]}""")
    except Exception as e: 
        await ctx.send("An error occurred, please try again")
        if settings.Logging: StorageHandler.LogError(None, input,e)
        settings.Debug(e.args[0])




@bot.command(name='sell')
async def sell(ctx, *, items):
    
    if not settings.Safety:
        RepressedItems = reprocess.Call(ctx, 82.93, str(items).lower())
        settings.Debug(RepressedItems)
        Call = ApiCaller.Call(None, 2, 90, RepressedItems)
        settings.Debug(Call)
        
        #Feel free to customize this message :)
        await ctx.send(f"""Contract to Yvftu for {Call["Buy"]} ISK""")
        return
    
    try:
        RepressedItems = reprocess.Call(ctx, 82.93, str(items).lower())
        settings.Debug(RepressedItems)
        Call = ApiCaller.Call(None, 2, 90, RepressedItems)
        settings.Debug(Call)
        
        #Feel free to customize this message :)
        await ctx.send(f"""Contract to Yvftu for {Call["Buy"]} ISK""") 
    except Exception as e:
        await ctx.send("An error occurred, please try again")
        if settings.Logging: StorageHandler.LogError(None, input,e)
        settings.Debug(e.args[0])




@bot.command(name='Jita')
async def Jita(ctx, *, items):
    
        if not settings.Safety:
            
        
            Call = ApiCaller.Call(None, 2, 100, items)
            settings.Debug(Call)
        
            #Feel free to customize this message :)
            await ctx.send(f""" Market: Jita     Percent: 100     Volume: {Call["Volume"]}
                   
Buy: {Call["Buy"]}
Sell: {Call["Sell"]}
Split: {Call["Split"]}""")
            return
        
        
        
        
@bot.command(name='Buyback')
async def Buyback(ctx, *, items):
    
        
        Call = ApiCaller.Call(None, 2, 90, items)
        settings.Debug(Call)
        
        #Feel free to customize this message, this is for the buy back program of our corp :)
        await ctx.send(f"""Contract to the corp in Imya NPC station for {Call["Buy"]} ISK""")




# Run the bot with your token
bot.run(str(open(settings.DiscordKey).read()))
