from datetime import datetime
import random
import sys
import math
import os
import time
import json 

# -------------------------------------------------------- #
# ---------------- read json file geocoding ---------------#
# -------------------------------------------------------- #

# Opening JSON file 
f = 'route_conv.json'

i=0
latitude = []
longitude = []
with open(f) as json_file:
    data = json.load(json_file)
    for p in data['gpx']['trk']['trkseg']['trkpt']:
        latitude.append(float(p['@lat']))
        longitude.append(float(p['@lon']))


# -------------------------------------------------------- #
# --------- send data flow temperature, long/lat ----------#
# -------------------------------------------------------- #
while i<50:
    # current date and time to timestamp
    now = datetime.now()

    timestamp = datetime.timestamp(now)
    print("timestamp =", timestamp)


    # temperature random
    temperature = random.uniform(0, 30.5)
    print("Random float number is ", temperature)
    #print("Random float number is ", random.random())

    print (latitude[i], longitude[i])
    
    # shell command
    os.system("mosquitto_pub -h localhost -t 'iot/data/iotmmsa0e6fe04b/v1/96a4e75e-db6c-4b0a-a79f-bb8605e35436' -m '{\"mode\":\"async\",\"messageType\":\"6acdf37c3cbcd43aa0ea\",\"messages\":[{\"timestamp\": %d ,\"temperature\":%d, \"longitude\":%2f, \"latitude\":%3f}]}'" % (timestamp, temperature, longitude[i], latitude[i]))
    i = i + 1
    time.sleep(5)
