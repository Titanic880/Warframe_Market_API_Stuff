import json
import requests
from os.path import exists
import os

Folder_Name = 'TestData'
JSON_Name = Folder_Name+'/weapons.json'
CSV_Name = Folder_Name+'/Weapons_Output.csv'
Mastery_File = Folder_Name+'/Mastery_Rank.txt'

def Get_Weapons():
    print('Pulling weapon Data from API, this might take awhile!')
    return requests.get('https://api.warframestat.us/weapons')

def Get_Frames():
    print('Pulling warframe Data from API, this might take awhile!')
    return requests.get('https://api.warframestat.us/warframes')

def To_File(File_Name, Request):
    if Request.status_code >= 400:
        print('Error: '+ str(Request.status_code))
        return
    UnDumped = Request.json()
    with open(File_Name, "w") as dumping:
        json.dump(UnDumped,dumping)
        return

To_File('Vaulted.json',Get_Weapons())
