import discord
from discord.ext import commands
import os
import ApiCaller
import reprocess
import settings
import random
import StorageHandler
import time

# Create an instance of the bot
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)





@bot.command(name='Price')
async def Price(ctx, Market, Percent, *, items):
    await ctx.send("Processing...")
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
        if settings.Logging: StorageHandler.LogError(None, input,e)
        settings.Debug(e.args[0])
    
    
    
@bot.command(name='Repo')
async def Repo(ctx, Market, MarketPercent, RatePercent, *, items):
    await ctx.send("Processing...")
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
        if settings.Logging: StorageHandler.LogError(None, input,e)
        settings.Debug(e.args[0])




@bot.command(name='RepoSell')
async def RepoSell(ctx, Market, MarketPercent, RatePercent, *, items):
    await ctx.send("Processing...")
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
        if settings.Logging: StorageHandler.LogError(None, input,e)
        settings.Debug(e.args[0])
    
    
    
    
@bot.command(name='RepoBuy')
async def RepoBuy(ctx, Market, MarketPercent, RatePercent, *, items):
    await ctx.send("Processing...")
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
    start_time = time.time()
    await ctx.send("Processing...")
    if not settings.Safety:
        RepressedItems = reprocess.Call(ctx, 82.93, str(items).lower())
        settings.Debug(RepressedItems)
        Call = ApiCaller.Call(None, 2, 90, RepressedItems)
        settings.Debug(Call)
        
        await ctx.send(f"""Items Reprocessed and excess items: {RepressedItems}""")
        #Feel free to customize this message :)
        await ctx.send(f"""Contract to Yvftu for {Call["Buy"]} ISK""")
        await ctx.send("--- %s seconds ---" % (time.time() - start_time))
        return
    
    try:
        
        RepressedItems = reprocess.Call(ctx, 82.93, str(items).lower())
        settings.Debug(RepressedItems)
        Call = ApiCaller.Call(ctx.author.name, 2, 90, RepressedItems)
        settings.Debug(Call)
        
        embed = discord.Embed(title="Madam Janice")
        embed.add_field(name="Reprocessed items and excess: ",value=RepressedItems)
        embed.add_field(name="Contract to Amarr Mining and Investments Inc for",value=str(Call["Buy"])+" ISK")
        await ctx.send(embed=embed)
        await ctx.send("--- %s seconds ---" % (time.time() - start_time))
         
    except Exception as e:
        await ctx.send("An error occurred, please try again")
        if settings.Logging: StorageHandler.LogError(ctx.author.name, input,e)
        settings.Debug(e.args[0])
        await ctx.send("--- %s seconds ---" % (time.time() - start_time))




@bot.command(name='Jita')
async def Jita(ctx, *, items):
        start_time = time.time()
        await ctx.send("Processing...")
        if not settings.Safety:
            
        
            Call = ApiCaller.Call(ctx.author.name, 2, 100, items)
            settings.Debug(Call)
        
            #Feel free to customize this message :)
            await ctx.send(f""" Market: Jita     Percent: 100     Volume: {Call["Volume"]}
                   
Buy: {Call["Buy"]}
Sell: {Call["Sell"]}
Split: {Call["Split"]}""")
            await ctx.send("--- %s seconds ---" % (time.time() - start_time))
            return
        
        try:
            RepressedItems = reprocess.Call(ctx, 82.93, str(items).lower())
            settings.Debug(RepressedItems)
            Call = ApiCaller.Call(ctx.author.name, 2, 90, RepressedItems)
            settings.Debug(Call)
            
            EmbedMod = discord.Embed(title="Modifiers")
            EmbedMod.add_field(name="Market: ",value="Market: Jita")
            EmbedMod.add_field(name="Percent: ",value="%100")
            EmbedMod.add_field(name="Volume: ",value=Call["Volume"])
            await ctx.send(embed=EmbedMod)
            
            EmbedPrice = discord.Embed(title="Prices")
            EmbedPrice.add_field(name="Buy: ",value=round(Call["Buy"], 2))
            EmbedPrice.add_field(name="Sell: ",value=round(Call["Sell"], 2))
            EmbedPrice.add_field(name="Split: ",value=round(Call["Split"], 2))
            await ctx.send(embed=EmbedPrice)
            await ctx.send("--- %s seconds ---" % (time.time() - start_time))
        except Exception as e:
            await ctx.send("An error occurred, please try again")
            if settings.Logging: StorageHandler.LogError(ctx.author.name, input,e)
            settings.Debug(e.args[0])
            await ctx.send("--- %s seconds ---" % (time.time() - start_time))
        
        
@bot.command(name='Buyback')
async def Buyback(ctx, *, items):
        await ctx.send("Processing...")
        
        Call = ApiCaller.Call(None, 2, 90, items)
        settings.Debug(Call)
        
        #Feel free to customize this message, this is for the buy back program of our corp :)
        await ctx.send(f"""Contract to the corp in Imya NPC station for {Call["Buy"]} ISK""")




# Run the bot with your token
bot.run(str(open(settings.DiscordKey).read()))
