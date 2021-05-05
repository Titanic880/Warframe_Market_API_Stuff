import json
#Name of the 'Master' file
File_Name = 'Test_Items.json'

f = open(File_Name,)
data = json.load(f)
print('Plat, Quantity, Last Updated')
for i in data["payload"]["items"]:
    print(i)
f.close()
