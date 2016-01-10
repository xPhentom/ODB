#!bin/python

import urllib2
import json

def readOpenData():
    url = "https://bruxellesdata.opendatasoft.com/api/records/1.0/search/?dataset=villo-stations-beschikbaarheid-in-real-time&lang=nl&facet=banking&facet=bonus&facet=status&facet=contract_name"

    response = urllib2.urlopen(url)
    data = json.loads(response.read())

    x = 0

    for data["datasetid"] in data["records"]:

        name = data["records"][x]["fields"]["name"]
        contract_name = data["records"][x]["fields"]["contract_name"]
        status = data ["records"][x]["fields"]["status"]

        print "%s in %s is %s\n" % (name, contract_name, status)
	
        x = x + 1

readOpenData()
