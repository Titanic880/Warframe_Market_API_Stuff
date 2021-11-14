#from _typeshed import Self
from os.path import exists
import requests
import json
import os

def Get_From_API(Specific):
    print('Pulling '+Specific+' Data from API, this might take awhile!')
    return requests.get('https://api.warframestat.us/'+Specific)
def To_Json(File_Name, Request):
    if Request.status_code >= 400:
        print('Error: '+ str(Request.status_code))
        return
    UnDumped = Request.json()
    with open(File_Name, 'w') as dumping:
        json.dump(UnDumped,dumping)
    return
def Make_File(File_Name, Default_Contents):
    f = open(File_Name, "x")
    f.write(str(Default_Contents))
    print(File_Name+' File Made!')
    return

class API_Pull:
    Folder_Name = 'TestData'
    Error_Log_Name = Folder_Name+'/Error_Items.txt'
    Weapon_JSON_Name = Folder_Name+'/weapons.json'
    Frame_JSON_Name = Folder_Name+'/warframes.json'
    Weapon_CSV_Name = Folder_Name+'/weapons_Output.csv'
    Melee_CSV_Name = Folder_Name+'/Melee_Output.csv'
    Frames_CSV_Name = Folder_Name+'/frames_Output.csv'
    Mastery_File = Folder_Name+'/Mastery_Rank.txt'
    Search_By_Name = Folder_Name+'/Name_Find.txt'
    Search_Result = Folder_Name+'/Search_Result.json'
    def __init__(self):
        if not exists(self.Folder_Name):
            os.mkdir(self.Folder_Name)
        if not exists(self.Mastery_File):
            Make_File(self.Mastery_File, '5')
        if not exists(self.Search_By_Name):
            Make_File(self.Search_By_Name, 'weapons,Acceltra')
        if not exists(self.Weapon_JSON_Name):
            To_Json(self.Weapon_JSON_Name,Get_From_API('weapons'))
        if not exists(self.Frame_JSON_Name):
            To_Json(self.Frame_JSON_Name,Get_From_API('warframes'))
        if not exists(self.Error_Log_Name):
            Make_File(self.Error_Log_Name, "Issue items will be named here:")
    def Find_Specific(self):
        f = open(self.Search_By_Name)
        name = str(f.read()).split(',')
        print('Searching for: '+name[0]+' ; '+name[1])
        f = open(self.Folder_Name+'/'+name[0]+'.json', 'r')
        data = json.load(f)
        f = open(self.Search_Result, 'w')
        for i in data:
            if i['name'] == name[1]:
                f.write(json.dumps(i,sort_keys=True,indent=4))
                return
        print('item: '+name[1]+' was not found!')
        return
    def warframe_Base_Stats(self):
        f = open(self.Frame_JSON_Name, 'r')
        data = json.load(f)
        f = open(self.Frames_CSV_Name, 'w')
        f.write('Name,Health,Shields,Armor,Energy Cap, Sprint Speed,MR Req')
        for i in data:
            f.write('\n'+
            str(i['name'])+','+
            str(i['health'])+','+
            str(i['shield'])+','+
            str(i['armor'])+','+
            str(i['power'])+','+
            str(i['sprintSpeed'])+','+
            str(i['masteryReq']))
        return
    def weapon_Base_Stats(self):
        f = open(self.Weapon_JSON_Name,'r')
        data = json.load(f)
        f = open(self.Weapon_CSV_Name, 'w')
        m = open(self.Melee_CSV_Name, 'w')
        e = open(self.Error_Log_Name, 'w')
        f.write('Name,Category,Type,Riven Dispo,MR Req,'+
        'Accuracy,Crit Chance,Crit Multiplier,Fire Rate,'+
        'MultiShot,Noise,Reload Time,Status Chance,Trigger Style,'+
        'Impact,Puncture,Slash')
        #THIS IS A SPACING WHILE I FIGURE OUT THE MELEE SECTION CAUSE IM STUPID
        m.write('Name,Type,Riven Dispo,MR Req,Attack Speed,Blocking Angle,'+
        'Combo Duration,Crit Chance,Crit Multiplier,Follow Through,'+
        'Range,Slam Attack,Slam Radial Dmg,Slam Radius,Slide Attack,'+
        'Status Chance,Impact,Puncture,Slash,'+
        'Heavy Dmg,HSlam Attack,HSlam Radial Dmg,Wind Up')
        for i in data:
            if i['category'] != "Melee" and i['productCategory'] != 'SentinelWeapons':
                try:
                    f.write('\n'+
                    str(i['name'])+','+
                    str(i['category'])+','+
                    str(i['type'])+','+
                    str(i['disposition'])+','+
                    str(i['masteryReq'])+','+
                    str(i['accuracy'])+','+
                    str(i['criticalChance'])+','+
                    str(i['criticalMultiplier'])+','+
                    str(i['fireRate'])+','+
                    str(i['multishot'])+','+
                    str(i['noise'])+','+
                    str(i['reloadTime'])+','+
                    str(i['procChance'])+','+
                    str(i['trigger'])+','+
                    str(i['damagePerShot'][0])+','+
                    str(i['damagePerShot'][1])+','+
                    str(i['damagePerShot'][2])
                )
                except:
                    e.write('\n'+str(i['name'])+','+str(i['type']))
                    print("Item(s) Added to error file")
            else:
                if i['category'] == 'Melee' and i['productCategory'] != 'SentinelWeapons':
                    try:
                        m.write('\n'+
                        str(i['name'])+','+
                        str(i['type'])+','+
                        str(i['disposition'])+','+
                        str(i['masteryReq'])+','+
                        str(i['fireRate'])+','+
                        str(i['blockingAngle'])+','+
                        str(i['comboDuration'])+','+
                        str(i['criticalChance'])+','+
                        str(i['criticalMultiplier'])+','+
                        str(i['followThrough'])+','+
                        str(i['range'])+','+
                        str(i['slamAttack'])+','+
                        str(i['slamRadialDamage'])+','+
                        str(i['slamRadius'])+','+
                        str(i['slideAttack'])+','+
                        str(i['procChance'])+','+
                        str(i['damagePerShot'][0])+','+
                        str(i['damagePerShot'][1])+','+
                        str(i['damagePerShot'][2])+','+
                        str(i['heavyAttackDamage'])+','+
                        str(i['heavySlamAttack'])+','+
                        str(i['heavySlamRadialDamage'])+','+
                        str(i['windUp'])
                        )
                    except:
                        e.write('\n'+str(i['name'])+','+str(i['type']))
                        print("Item(s) Added to error file")
        return
