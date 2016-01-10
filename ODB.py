#!bin/python

import urllib2
import json
import os
import sys

def readVilloStations(): 
    url = "https://bruxellesdata.opendatasoft.com/api/records/1.0/search/?dataset=villo-stations-beschikbaarheid-in-real-time&lang=nl&facet=banking&facet=bonus&facet=status&facet=contract_name" #Sets url

    response = urllib2.urlopen(url) #Reads data from url
    data = json.loads(response.read())#Set info as json file

    x = 0 #Counter for going through all the data

    for data["datasetid"] in data["records"]:#For each data in json file

	number = data["records"][x]["fields"]["number"]
        name = data["records"][x]["fields"]["name"][6:]
        contract_name = data["records"][x]["fields"]["contract_name"]
        status = data ["records"][x]["fields"]["status"]

        print "\n%s.	%s in %s is %s" % (number, name, contract_name, status) #Display basic info of the stations
	
        x = x + 1 #Add to counter called x

    print "\n Choose a number to get more info about the station:\n"
    answer =  raw_input(">>>	") #User can now choose a specific station to get more info from it
        
    counter = 0 #Make second counter so that you can get the chosen number      
 
    for data["datasetid"] in data["records"]: #Go through al the data
         
        number = data["records"][counter]["fields"]["number"] 

	if float(answer) == float(number): #Take the chosen date, given by the answer of the user
            name = data["records"][counter]["fields"]["name"][6:]
            contract_name = data["records"][counter]["fields"]["contract_name"]
            status = data ["records"][counter]["fields"]["status"]
	    bike_stands = data ["records"][counter]["fields"]["bike_stands"]
            available_stands = data ["records"][counter]["fields"]["available_bike_stands"]
	    available_bikes = data ["records"][counter]["fields"]["available_bikes"]
        

	counter = counter + 1
    

    print "\n %s in %s is %s\n\n There are currently %s out of %s bikestands available.\n\n %s bikes are still available\n\n" % (name, contract_name, status, available_stands, bike_stands, available_bikes)

########END readVilloStations function##########


def choices(): #TODO: make an array to make this easier
    print "\n - Villo"


###Here starts the program


os.system('clear')
print "\n Hi \n Welcome to ODB, the Open Data reader for Brussels.\n For the moment, you can choose between: "

choices()

print "\n Which one do you choose?"

ans = raw_input(">>>   ")

ans = ans.lower()

if ans == "villo":
    readVilloStations()
else:
    print "The number you've chosen isn't in the list"
    sys.exit()
