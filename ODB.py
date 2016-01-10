#!bin/python

import urllib2
import json

def readVilloStations(): # TODO: make user choose between the first three numbers of the data OR use ["number"]
    url = "https://bruxellesdata.opendatasoft.com/api/records/1.0/search/?dataset=villo-stations-beschikbaarheid-in-real-time&lang=nl&facet=banking&facet=bonus&facet=status&facet=contract_name" #Sets url

    response = urllib2.urlopen(url) #Reads data from url
    data = json.loads(response.read())#Set info as json file

    x = 0 #Counter for going through all the data

    for data["datasetid"] in data["records"]:#For each data in json file

	number = data["records"][x]["fields"]["number"]
        name = data["records"][x]["fields"]["name"][6:]
        contract_name = data["records"][x]["fields"]["contract_name"]
        status = data ["records"][x]["fields"]["status"]

        print "\n%s.	%s in %s is %s" % (number, name, contract_name, status)
	
        x = x + 1

    print "\n Choose a number to get more info about the station:\n"
    answer =  raw_input(">>>	")
        
    counter = 0       
 
    for data["datasetid"] in data["records"]:
         
        number = data["records"][counter]["fields"]["number"]

	if float(answer) == float(number):
            name = data["records"][counter]["fields"]["name"][6:]
            contract_name = data["records"][counter]["fields"]["contract_name"]
            status = data ["records"][counter]["fields"]["status"]

        counter = counter + 1
    

    print "\n%s in %s is %s" % (name, contract_name, status)

########END readVilloStations function##########


def choices(): #TODO: make an array to make this easier
    print "\n - Villo"


print "\n Hi \n Welcome to ODB, the Open Data reader for Brussels.\n For the moment, you can choose between: "

choices()

print "\n Which one do you choose?"

ans = raw_input(">>>   ")

ans = ans.lower()

if ans == "villo":
    readVilloStations()
