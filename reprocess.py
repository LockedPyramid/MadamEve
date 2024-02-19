"""Calls the Janice API with a user input

use Call() function to initiate API call

Returns:
    String: String to send to user
"""

import requests
import json
import os
import settings
import StorageHandler
import re
import ApiCaller

mineralsList = ["tritanium", "pyerite", "mexallon", "isogen", "nocxium", "zydrine", "megacyte", "morphite", "heavywater", "liquidozone", "strontiumclathrates", "heliumisotopes", "hydrogenisotopes", "nitrogenisotopes", "oxygenisotopes", "atmosphericgases", "evaporitedeposits", "hydrocarbons", "silicates", "cobalt", "scandium", "titanium", "tungsten", "cadmium", "vanadium", "chromium", "platinum", "caesium", "technetium", "hafnium", "mercury", "promethium", "dysprosium", "neodymium", "thulium"]

def GetAmount(input):
    ToReturn = str(re.findall(r'\d+', str(input).replace(",",""))).removeprefix("['").removesuffix("']")
    if settings.Debug: print(ToReturn)
    return ToReturn
    

def Call(user, RepoPercentage, InputData):
    """Get the repo items

        user(string): The user
        Market (string): which market does the user want
        Percent (string): Percent of the
         InputData (string): User input data
         
    Returns:
        string: String to send to user
    """
    Out = []
    Items = str(InputData).split("\n")
    
    with open(settings.RepoJsonLocation) as f:
        Repo = json.loads(str(f.read()).lower())
    
    DictHold = {
        "tritanium": "0",
        "pyerite": "0",
        "mexallon": "0",
        "isogen": "0",
        "nocxium": "0",
        "zydrine": "0",
        "megacyte": "0",
        "morphite": "0",
        "heavy water": "0",
        "liquid ozone": "0",
        "strontium clathrates": "0",
        "helium isotopes": "0",
        "hydrogen isotopes": "0",
        "nitrogen isotopes": "0",
        "oxygen isotopes": "0",
        "atmospheric gases": "0",
        "evaporite deposits": "0",
        "hydrocarbons": "0",
        "silicates": "0",
        "cobalt": "0",
        "scandium": "0",
        "titanium": "0",
        "tungsten": "0",
        "cadmium": "0",
        "vanadium": "0",
        "chromium": "0",
        "platinum": "0",
        "caesium": "0",
        "technetium": "0",
        "hafnium": "0",
        "mercury": "0",
        "promethium": "0",
        "dysprosium": "0",
        "neodymium": "0",
        "thulium": "0"
        }
    
    for item in Items:
        try:
            Amount = (GetAmount(item)).split("',")[0]
        except:
            Amount = "1"
        ItemName = (str(item.removesuffix(str(Amount))).lower()) # Get item name
        settings.Debug("Amount:" + str(Amount))
        
        
        

        #Get rid of everything after number
        match = re.search(r'\d', ItemName)
        if match:
            index_of_first_digit = match.start()
            ItemName = ItemName[:index_of_first_digit]
        
        #Clean up string
        Counter = 0
        while Counter < 20:
            ItemName = ItemName.removesuffix(" ").removeprefix(" ")
            Counter += 1
        ItemName = ItemName.removeprefix("compressed ")
        settings.Debug("Item Name: " + ItemName)
        
        RepoGot = Repo[ItemName] # Get data from repo
        
        settings.Debug("RepoGot: " + str(RepoGot))
        
        for key in RepoGot.keys():
            if settings.Debug:print(RepoGot[key])
            repo_value = int(RepoGot[key]) 

            
            dict_hold_value = int(DictHold[key])

             
            try:
                amount_int = int(Amount)
            except:
                amount_int = 1
            
            sum_value = int(((float(repo_value)/100) * amount_int)*(float(RepoPercentage)/100)) + dict_hold_value

            DictHold[key] = sum_value
            
    Out = DictHold.copy()
    settings.Debug("out: " + str(Out))

    Out = str(Out).removesuffix("}]").removeprefix("[{")
    split_string = Out.split(',')
    result = '\n'.join(split_string)
    Out = result.replace(":","").replace("'","").replace("{","").replace("}","")
    if settings.debug: print("---DONE PROCESSING---")
    
    settings.Debug("out: \n"+ Out)
    settings.Debug("-----CLEANING DATA-----")
    lines = Out.strip().split('\n')

    filtered_lines = [line for line in lines if ' 0' not in line]
    Out = '\n'.join(filtered_lines)    
    settings.Debug("-----ADDING EXECS-----")
    settings.Debug("-----REPO DONE-----")

    return Out
    



#Call(None,83.93,'''Compressed Glistening Zeolites    157    Ubiquitous Moon Asteroids
#Compressed Gneiss    49,600    Gneiss
#Compressed Iridescent Gneiss    62,400    Gneiss
#Compressed Prismatic Gneiss    36,000    Gneiss
#Compressed Twinkling Cobaltite    72,463    Common Moon Asteroids
#Compressed Twinkling Titanite    12,487    Common Moon Asteroids
#Compressed Crystalline Crokite    1,698    Crokite
#Compressed Dark Ochre    4,357    Dark Ochre
#Compressed Fiery Kernite    12,989    Kernite
#Compressed Fiery Kernite    7,796    Kernite
#Compressed Fiery Kernite    8,317    Kernite
#Compressed Gneiss    4,070    Gneiss
#Compressed Iridescent Gneiss    9,145    Gneiss
#Compressed Kernite    11,620    Kernite
#Compressed Kernite    12,535    Kernite
#Compressed Kernite    20,887    Kernite
#Compressed Luminous Kernite    50,608    Kernite
#Compressed Luminous Kernite    85,821    Kernite
#Compressed Luminous Kernite    88,030    Kernite
#Compressed Obsidian Ochre    7,167    Dark Ochre
#Compressed Prismatic Gneiss    15,745    Gneiss
#Compressed Pristine Jaspet    3,399    Jaspet
#Compressed Pure Jaspet    15,668    Jaspet
#Compressed Pure Jaspet    18,758    Jaspet
#Compressed Pure Jaspet    5,305    Jaspet''')