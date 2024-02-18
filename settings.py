Debug = True
Logging = True
DefaultStation = 2
DefaultPercent = 100

#Change these locations to match your system
DiscordKey = open("/home/ada/Janice/Storage/Discord.key").read()
JaniceKey = open("/home/ada/Janice/Storage/Janice.key").read()

def Debug(input): 
    if Debug: print(input)