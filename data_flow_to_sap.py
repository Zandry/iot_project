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

# -------------------------------------------------------- #
# --------- send data flow temperature, long/lat ----------#
# -------------------------------------------------------- #
# -------------------------------------------------------- #
# ---------------- read json file geocoding ---------------#
# -------------------------------------------------------- #
    
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

        # shell command
        os.system("mosquitto_pub -h localhost -t 'iot/data/iotmmsa0e6fe04b/v1/96a4e75e-db6c-4b0a-a79f-bb8605e35436' -m '{\"mode\":\"async\",\"messageType\":\"6acdf37c3cbcd43aa0ea\",\"messages\":[{\"timestamp\": %d ,\"temperature\":%d, \"longitude\":%2f, \"latitude\":%3f}]}'" % (timestamp, temperature, longitude, latitude))
        time.sleep(2)

