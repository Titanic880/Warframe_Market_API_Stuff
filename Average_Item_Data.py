#Takes the average of the user Data and puts it into the CSV
import json
Temp_File = 'Temp.CSV'
#finds the average of the inputted array
def Find_Average():
    with open(Temp_File) as f:
        content = f.read().splitlines()
    for line in content:
        print(line)

def Find_Lowest():
    

def Find_Highest():


Find_Average()
