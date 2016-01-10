#!bin/python

import urllib2
import json

def readVilloStations(): # TODO: make user choose between the first three numbers of the data
    url = "https://bruxellesdata.opendatasoft.com/api/records/1.0/search/?dataset=villo-stations-beschikbaarheid-in-real-time&lang=nl&facet=banking&facet=bonus&facet=status&facet=contract_name"

    response = urllib2.urlopen(url)
    data = json.loads(response.read())

    x = 0

    for data["datasetid"] in data["records"]:

        name = data["records"][x]["fields"]["name"]
        contract_name = data["records"][x]["fields"]["contract_name"]
        status = data ["records"][x]["fields"]["status"]

        print "\n%s in %s is %s" % (name, contract_name, status)
	
        x = x + 1

def choices(): #TODO: make an array to make this easier
    print "\n - Villo"


print "\n Hi \n Welcome to ODB, the Open Data reader for Brussels.\n For the moment, you can choose between: "

choices()

print "\n Which one do you choose?"

ans = raw_input(">>>   ")

ans = ans.lower()

if ans == "villo":
    readVilloStations()
