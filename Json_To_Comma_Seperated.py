import json
import datetime
#TESTING ITEM URL
ItemURL = 'secura_dual_cestra'
CSV_Name = 'Test_output.csv'
Temp_File = 'Temp.CSV'

#overwrites old .CSV and adds a banner
def Rebuild_CSV():
    f = open(CSV_Name, 'w')
    f.write('Plat, Quantity, Username, Last Updated')
    Add_To_CSV(ItemURL)
#Generates and fills the CSV with the given Order
def Add_To_CSV(ITEM_URL):
    f = open(ITEM_URL+'.json',)
    data = json.load(f)
    f = open(Temp_File, 'a')
    for i in data["payload"]["orders"]:
        if i['order_type'] == 'sell' and i['user']['status'] == 'ingame':
            f.write(
            str(i['platinum'])+","+
            str(i['quantity'])+","+
            i['user']['ingame_name']+","+
            Clean_Time(i['last_update'])+"\n")
    f.close()
#removes stray characters/data from the datetime
def Clean_Time(Time_Cleaned):
    TC = Time_Cleaned.replace('T',' ')
    return TC.replace('+00:00',' ')
#Individual Testing run
Rebuild_CSV()
print('CSV has been generated!')
