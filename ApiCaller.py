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



def Call(user, Market,Percent, InputData):
    """Get the API data from the user input

         InputData (string): User input data
    Returns:
        string: String to send to user
    """
    Amount = 0
    Volume = 0
    Buy = 0
    Sell = 0
    Split = 0
    ApiKey = open(settings.JaniceKey).read()

    
    # Pull api data from Janice
    url = 'https://janice.e-351.com/api/rest/v1/pricer?key='+ApiKey+'&market='+str(Market)
    headers = {'content-type': 'text/plain', 'accept':'application/json'}
    

    settings.Debug(f'Data in {InputData}')
    try:
        input = str(InputData) #Get data as string
        data = str(input)
        settings.Debug(f' ')
        
        Items = data.split("\n")
        
        settings.Debug(f'Items: {Items}')
        
        for item in Items: 
            
            r = requests.post(url, data=item, headers=headers)
            rToLib = json.loads(json.dumps(r.json()).removeprefix("[").removesuffix("]")) # Turn into Json
            settings.Debug(r)
            Amount = str(re.findall(r'\d+', str(item).replace(",",""))).removeprefix("['").removesuffix("']")
            settings.Debug(Amount)
            try:Amount = float(Amount) 
            except Exception as e: 
                if settings.Logging: StorageHandler.LogError(user,input,e)
                return f'Error in float(Amount) {Amount} ERROR: {e}'
            
            Volume = Volume + (float(rToLib["volume"])*Amount)  
            Buy = Buy + (float(rToLib["buyPriceMax"])*Amount)
            Sell = Sell + (float(rToLib["sellPriceMin"])*Amount)
            Split = Split + (float(rToLib["splitPrice"])*Amount)
        
        ToSend = {"Market": Market, "Percent": Percent, "Volume": Volume , "Buy": (Buy * (float(Percent)/100)), "Sell": (Sell * (float(Percent)/100)), "Split": (Split * (float(Percent)/100))}
        
        if settings.Logging: StorageHandler.LogData(user, Buy * (float(Percent)/100), Sell * (float(Percent)/100), Split * (float(Percent)/100), data)
        
        if ToSend == "[]":
             if settings.Debug : return "NOTICE: Data inputted is invalid. result> " + ToSend
             else: return "NOTICE: Your data is wrong, please try again"
        settings.Debug(ToSend)
        
        return (ToSend)
            
    except Exception as e:
        if settings.Logging: StorageHandler.LogError(user,input,e)

        if(settings.debug):
            return str(e.args[0])
        else:
            return "Check documentation. if error persists please contact Erold Hareka"
