from os.path import exists
import requests
import json
import os

class API_Pull:
    Folder_Name = 'TestData'
    Weapon_JSON_Name = Folder_Name+'/weapons.json'
    Frame_JSON_Name = Folder_Name+'/warframes.json'
    Weapon_CSV_Name = Folder_Name+'/weapons_Output.csv'
    Frames_CSV_Name = Folder_Name+'/frames_Output.csv'
    Mastery_File = Folder_Name+'/Mastery_Rank.txt'
    Search_By_Name = Folder_Name+'/Name_Find.txt'
    Search_Result = Folder_Name+'/Search_Result.txt'
    def __init__(self):
        if not exists(self.Folder_Name):
            os.mkdir(self.Folder_Name)
        if not exists(self.Mastery_File):
            self.Make_File(self.Mastery_File, 5)
        if not exists(self.Search_By_Name):
            self.Make_File(self.Search_By_Name, 'weapons,Acceltra')
        if not exists(self.Weapon_JSON_Name):
            self.To_File(self.Weapon_JSON_Name,self.Get_From_API('weapons'))
        if not exists(self.Frame_JSON_Name):
            self.To_File(self.Frame_JSON_Name,self.Get_From_API('warframes'))
    def Get_From_API(self, Specific):
        print('Pulling '+Specific+' Data from API, this might take awhile!')
        return requests.get('https://api.warframestat.us/'+Specific)
    def To_File(self, File_Name, Request):
        if Request.status_code >= 400:
            print('Error: '+ str(Request.status_code))
            return
        UnDumped = Request.json()
        with open(File_Name, "w") as dumping:
            json.dump(UnDumped,dumping)
        return
    def To_Json(self, File_Name, Request):
        if Request.status_code >= 400:
            print('Error: '+ str(Request.status_code))
            return
        UnDumped = Request.json()
        with open(File_Name, 'w') as dumping:
            json.dump(UnDumped,dumping)
        return
    def To_CSV(self, Source, Destination):
        f = open(self.Mastery_File)
        MasteryCap = int(f.read())
        f = open(Destination, 'w')
        f.write('Name, Mastery Level\n')
        f = open(Source)
        data = json.load(f)
        f = open(Destination, 'a')
        for i in data:
            if(i['masteryReq'] <= MasteryCap):
                f.write('\n'+
                str(i['name'])+","+
                str(i['masteryReq']))
        f.close()
        return
    def Get_File_Contents(self, File_Name):
        f = open(File_Name, 'r')
        vTemp = f.read()
        return vTemp
    def Make_File(self, File_Name, Default_Contents):
        f = open(File_Name, "x")
        f.write(str(Default_Contents))
        print(File_Name+' File Made!')
        return
    def Find_Specific(self):
        f = open(self.Search_By_Name)
        name = str(f.read()).split(',')
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
        f.write('Name,Category,Type,Riven Dispo,MR Req,'+
        'Accuracy,Crit Chance,Crit Damage,Fire Rate,'+
        'MultiShot,Noise,Reload Time,Status Chance,Trigger Style,'+
        'Impact,Puncture,Slash')
        for i in data:
            print(i['name']+' '+i['category'])
            if i['category'] == "Primary" and i['productCategory'] != "SentinelWeapons":
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
        return
