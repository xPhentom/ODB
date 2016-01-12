#!/bin/python

import urllib2
import json
import os
import sys
from array import array

def readVillo(number):
    
    stationNumber = data["records"][number]["fields"]["number"]
    stationName = data["records"][number]["fields"]["name"][6:]
    stationContract = data["records"][number]["fields"]["contract_name"]
    stationStatus = data["records"][number]["fields"]["status"]

    print "\n%s.    %s in %s is %s" % (stationNumber, stationName, stationContract, stationStatus)
    
def readParking(number):
    try:
        parking = data["records"][number]["fields"]["nombre_de_places"]
        parking_name = data["records"][number]["fields"]["description"]
        print "\n There are %s parking spots in %s\n" % (parking, parking_name)
    except:
        pass    

def readATM(number):
    description = data["records"][number]["fields"]["description"]
    print "\n There is an ATM at %s\n" % description

def readInfo(answer):

    if answer == "villo":
        url = "https://bruxellesdata.opendatasoft.com/api/records/1.0/search/?dataset=villo-stations-beschikbaarheid-in-real-time&lang=nl&facet=banking&facet=bonus&facet=status&facet=contract_name"
    elif answer == "parking":
        url = "https://bruxellesdata.opendatasoft.com/api/records/1.0/search/?dataset=public-parkings&lang=en"
    elif answer =="atm":
        url = "https://bruxellesdata.opendatasoft.com/api/records/1.0/search/?dataset=atms&lang=en"

    response = urllib2.urlopen(url)
    
    global data

    data = json.loads(response.read())

    x = 0

    for data["datasetid"] in data["records"]:
        if answer == "villo":
            readVillo(x)
        elif answer == "parking":
            readParking(x)
        elif answer == "atm":
            readATM(x)
        else:
            print "The number you've chosen isn't in the list"
            sys.exit()

        x = x + 1 

################# End readInfo

options = ["Villo", "Parking", "ATM"]

def choices():
    for i in range (0, len(options)):
        print"\n - %s" % options[i]

os.system('clear')

print "\n Hi \n Welcome to ODB, the Open Data reader for Brussels. \n For the Moment, you can choose between: "

choices()

print "\n Which one do you choose?"

ans = raw_input(">>>   ")

ans = ans.lower()

readInfo(ans)
