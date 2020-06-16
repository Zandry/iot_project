from datetime import datetime
import random
import sys
import math
import os
import time
import json 


# Opening JSON file 
f = 'route_conv.json'

i=0
latitude = []
longitude = []



# -------------------------------------------------------- #
# --------- send data flow temperature, long/lat ----------#
# -------------------------------------------------------- #
# -------------------------------------------------------- #
# ---------------- read json file geocoding ---------------#
# -------------------------------------------------------- #
    
with open(f) as json_file:
    data = json.load(json_file)
    for p in data['gpx']['trk']['trkseg']['trkpt']:
        latitude.append(float(p['@lat']))
        longitude.append(float(p['@lon']))
        print (latitude[i], longitude[i])

        # current date and time to timestamp
        now = datetime.now()

        timestamp = datetime.timestamp(now)
        print("timestamp =", timestamp)


        # temperature random
        temperature = random.uniform(0, 30.5)
        print("temperature : %2.2f" % temperature)
        #print("Random float number is ", random.random())

        # shell command
        os.system("mosquitto_pub -h localhost -t 'iot/data/iotmmsa0e6fe04b/v1/96a4e75e-db6c-4b0a-a79f-bb8605e35436' -m '{\"mode\":\"async\",\"messageType\":\"6acdf37c3cbcd43aa0ea\",\"messages\":[{\"timestamp\": %d ,\"temperature\":%d, \"longitude\":%2f, \"latitude\":%3f}]}'" % (timestamp, temperature, longitude[i], latitude[i]))
        time.sleep(5)
