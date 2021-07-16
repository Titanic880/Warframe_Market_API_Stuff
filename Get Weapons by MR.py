import json
import requests
from os.path import exists
import os

Folder_Name = 'TestData'
JSON_Name = Folder_Name+'/weapons.json'
CSV_Name = Folder_Name+'/Weapons_Output.csv'
Mastery_File = Folder_Name+'/Mastery_Rank.txt'

def Directory_Check():
    if(not exists(Folder_Name)):
        os.mkdir(Folder_Name)
    if(not exists(Mastery_File)):
        Make_Mastery()
    if(not exists(JSON_Name)):
        To_File(JSON_Name,Get_Weapons())
    return
def Get_Mastery():
    f = open(Mastery_File, 'r')
    vTemp = f.read()
    if vTemp.isdigit():
        return int(vTemp)
    return
def Make_Mastery():
    f = open(Mastery_File, "x")
    f.write(str(5))
    print('Mastery File Made!')
    return
def Get_Weapons():
    print('Pulling weapon data from API, this might take awhile!')
    return requests.get('https://api.warframestat.us/weapons')
def To_File(File_Name, Request):
    if Request.status_code >= 400:
        print('Error: '+ str(Request.status_code))
        return
    UnDumped = Request.json()
    with open(File_Name, "w") as dumping:
        json.dump(UnDumped,dumping)
        return
#overwrites old .CSV and adds a banner
def Rebuild_CSV():
    f = open(CSV_Name, 'w')
    f.write('Name, Mastery\n')
    Add_To_CSV_Weapon(Get_Mastery())
#Generates and fills the CSV with the given Order
def Add_To_CSV_Weapon(MasteryCap):
    f = open(JSON_Name)
    data = json.load(f)
    f = open(CSV_Name, 'a')
    for i in data:
        if(i['masteryReq'] <= MasteryCap):
            f.write('\n'+
            str(i['name'])+","+
            str(i['masteryReq']))
    f.close()
    return


Directory_Check()
Rebuild_CSV()
print('CSV has been generated!')
