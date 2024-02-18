import settings
from datetime import datetime
import os
print("Working DIR" + os.getcwd())

if not os.path.isdir(settings.StorageLocation):
    
    os.mkdir(settings.StorageLocation)
if not os.path.isfile(settings.LogLocation):
    open(settings.LogLocation, 'w').close()
if not os.path.isfile(settings.AdminWhitelistLocation):
    open(settings.AdminWhitelistLocation, 'w').close()

def GetAdminList():
    file = open(settings.AdminWhitelistLocation)
    List = file.read()
    file.close()
    return List

def AddAdmin(name):
    data = GetAdminList().split(",") #Get as array
    
    if settings.Debug: print(data)
    
    data.append(name)
    if settings.Debug:print(data)
    data = ','.join(data)
    if settings.Debug:print(data)
    file = open(settings.AdminWhitelistLocation, "r+")
    file.write(data)
    file.close
    
def RemoveAdminList(name):
    data = GetAdminList().split(",") #Get as array
    
    if settings.Debug: print(data)
    
    data.append(name)
    if settings.Debug:print(data)
    data = ','.join(data)
    if settings.Debug:print(data)
    file = open(settings.AdminWhitelistLocation, "r+")
    file.write(data)

def LogData(user, buy, sell, split, items):
    now = datetime.now()
    log = f""" 
USER: {str(user)}
DateTime:{str(now)}

BUY: {str(buy)}
SELL: {str(sell)}
SPLIT: {str(split)}

ITEMS: {str(items)}
    
__________ 
    """
    
    with open(settings.LogLocation, "a") as myfile:
        myfile.write(log)
def LogError(user, data, error):
    now = datetime.now()
    log = f""" 
---ERROR---
USER: {str(user)}
DateTime:{str(now)}
Error: {str(error)}

Data: {str(data)}
__________ 
    """
    
    with open(settings.LogLocation, "a") as myfile:
        myfile.write(log)

def LogReboot(user):
    log = f'''
    -----
    REBOOT
    User: {str(user)}
    Time: {str(datetime.now())}
    -----
    
    '''
    with open(settings.LogLocation, "a") as myfile:
        myfile.write(log)
