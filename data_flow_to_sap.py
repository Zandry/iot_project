# --------------------------------------------------------------- #
# --------- the purpose of this program is to create    --------- #
# --------- random values ​​to simulate the temperature   --------- #
# --------- and to read the geolocation data.           --------- #
# --------- And allows to send them to the IoT cockpit  --------- #
# --------------------------------------------------------------- #
# --------------------------------------------------------------- #
# --- Author: Arnauld ANDRIANIAINA | Creation date: 16/06/2020 -- #
# --------------------------------------------------------------- #
from datetime import datetime
import random
import sys
import math
import os
import time
import json 
import xmltodict

# -------------------------------------------------------- #
# ---------------- convert xml file to json ---------------#
# -------------------------------------------------------- #

with open('route.gpx') as xml_file:
    my_dict=xmltodict.parse(xml_file.read())
xml_file.close()
json_data=json.dumps(my_dict)
#print(json_data)
print("convert success")
print("##### send data to IoT cockpit #####")

# output file
out_file = open("route_conv.json", "w") 
json.dump(my_dict, out_file, indent = 4) 
out_file.close() 


# -------------------------------------------------------- #
# --------- send data flow temperature, long/lat ----------#
# -------------------------------------------------------- #
# -------------------------------------------------------- #
# ---------------- read json file geocoding ---------------#
# -------------------------------------------------------- #

# Opening JSON file 
f = 'route_conv.json'

i=0    

with open(f) as json_file:
    data = json.load(json_file)
    for p in data['gpx']['trk']['trkseg']['trkpt']:
        latitude = float(p['@lat'])
        longitude = float(p['@lon'])
        print (latitude, longitude)

        # current date and time to timestamp
        now = datetime.now()

        timestamp = datetime.timestamp(now)
        print("timestamp =", timestamp)


        # temperature random
        temperature = random.uniform(0, 30.5)
        print("temperature : %2.2f" % temperature)
        #print("Random float number is ", random.random())

        # shell command  publish data to the broker 
        os.system("mosquitto_pub -h localhost -t 'iot/data/iotmmsa0e6fe04b/v1/96a4e75e-db6c-4b0a-a79f-bb8605e35436' -m '{\"mode\":\"async\",\"messageType\":\"6acdf37c3cbcd43aa0ea\",\"messages\":[{\"timestamp\": %d ,\"temperature\":%d, \"longitude\":%2f, \"latitude\":%3f}]}'" % (timestamp, temperature, longitude, latitude))
        time.sleep(10)

