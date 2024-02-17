import string
import settings

def GetModifiers(data):
    """Get Modifiers from input

    Args:
        data (str): string input from user
    """
    Mods = {"Percent":settings.DefaultPercent,"Station":settings.DefaultStation}
    Mod = str(data)
    Mod = Mod.split(">")[0]
    if settings.Debug: print("data: " + Mod)
    
    if "%" in Mod and "@" in Mod:
        Mod = Mod.split("@")
        Percent = Mod[0].removeprefix("%")
        Station = Mod[1]
        Mods["Percent"] = Percent
        Mods["Station"] = Station        
    elif "%" in Mod:
        if settings.Debug: print("mods: " + Mod.removeprefix("%"))
        Mods["Percent"] = Mod.removeprefix("%") 
    elif "@" in Mod:
        if settings.Debug: print("mods: " + Mod.removeprefix("@"))
        Mods["Station"] = Mod.removeprefix("@")         
   
    if settings.Debug: print(f'Mods: {Mods}')
    return(Mods)

#*------------------------------------------------------
#* Toggles
#*------------------------------------------------------
def ToggleDebug():
    Debug = settings.Debug
    if Debug == False: settings.Debug = True
    else: settings.Debug = False

def ToggleLogging():
    if Logging == False: Logging = True
    else: Logging = False