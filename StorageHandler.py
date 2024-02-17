import settings
from datetime import datetime
import os
print("Working DIR" + os.getcwd())

if not os.path.isdir("/home/ada/Janice/Storage/"):
    
    os.mkdir("/home/ada/Janice/Storage/")
if not os.path.isfile("/home/ada/Janice/Storage/Log.log"):
    open("/home/ada/Janice/Storage/Log.log", 'w').close()
if not os.path.isfile("/home/ada/Janice/Storage/AdminWhitelist.log"):
    open("/home/ada/Janice/Storage/AdminWhitelist.log", 'w').close()

def GetAdminList():
    file = open("/home/ada/Janice/Storage/AdminWhitelist.log")
    List = file.read()
    file.close()
    return List

def AddAdmin(name):
    data = GetAdminList().split(",") #Get as array
    
    if settings.Debug: print(data)
    
    data.append(name)
    print(data)
    data = ','.join(data)
    print(data)
    file = open("/home/ada/Janice/Storage/AdminWhitelist.log", "r+")
    file.write(data)
    file.close
    
def RemoveAdminList(name):
    data = GetAdminList().split(",") #Get as array
    
    if settings.Debug: print(data)
    
    data.append(name)
    print(data)
    data = ','.join(data)
    print(data)
    file = open("/home/ada/Janice/Storage/AdminWhitelist.log", "r+")
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
    
    with open("/home/ada/Janice/Storage/Log.log", "a") as myfile:
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
    
    with open("/home/ada/Janice/Storage/Log.log", "a") as myfile:
        myfile.write(log)

def LogReboot(user):
    log = f'''
    -----
    REBOOT
    User: {str(user)}
    Time: {str(datetime.now())}
    -----
    
    '''
    with open("/home/ada/Janice/Storage/Log.log", "a") as myfile:
        myfile.write(log)
