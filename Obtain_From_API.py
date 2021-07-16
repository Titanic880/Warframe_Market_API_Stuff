import json
import requests

#the primary URL of the used API
API_URL = "https://api.warframe.market/v1/items"
#TESTING ITEM URL
ItemURL = "secura_dual_cestra"


#takes an API element and calls the information from it
def Request_API(Item_Url):
    if not Item_Url:
        return requests.get(API_URL)
    else:
        return requests.get(API_URL+"/"+Item_Url)

#Adds on the information required for orders
def Build_Request_Orders(Item_Url):
    return Item_Url+"/orders?include=item"

def Run_Data(File_Name, Request):
    if Request.status_code >= 400:
        print('Error: '+ str(Request.status_code))
        return
    UnDumped = Request.json()
    with open(File_Name, "w") as dumping:
        json.dump(UnDumped,dumping)
        return

#Asks for the Specific Item (pulls item information)
Run_Data("Test.json", Request_API(ItemURL))
#asks for the specific Items Orders (pulls current orders)
Run_Data(ItemURL+".json", Request_API(Build_Request_Orders(ItemURL)))
#Asks for everything
#Run_Data("Test_Items.json", Request_API(""))
print("Files created!")
