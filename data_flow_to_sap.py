from datetime import datetime
import random
import sys
import math
import os
#from time import sleep
import time
import json 

# -------------------------------------------------------- #
# ---------------- read json file geocoding ---------------#
# -------------------------------------------------------- #
# Opening JSON file 
f = 'route_conv.json'

i=0
j=0
latitude = []
longitude = []
with open(f) as json_file:
    data = json.load(json_file)
    for p in data['gpx']['trk']['trkseg']['trkpt']:
        latitude.append(float(p['@lat']))
        longitude.append(float(p['@lon']))

        #print (latitude[j], longitude[j])
        j +=1 


#latitude = 48.30
#longitude = 2.10



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

#------------Generate random geolocation latitude & longitude ------------------
    #generate long lat 

    #def generate_random_data(lat, lon, num_rows):
    #    for _ in range(num_rows):
    #        hex1 = '%012x' % random.randrange(16**12) # 12 char random string
    #        flt = float(random.randint(0,100))
    #        dec_lat = random.random()/100
    #        dec_lon = random.random()/100
    #        print ("%s %.1f %.6f %.6f" , (hex1.lower(), flt, lon+dec_lon, lat+dec_lat))
    #
    #generate_random_data(latitude, longitude, 5)
    
   #hex1 = '%012x' % random.randrange(16**12) # 12 char random string
   #flt = float(random.randint(0,100))
   #dec_lat = random.random()/100
   #dec_lon = random.random()/100
   #print ("%s %.1f %.6f %.6f" , (hex1.lower(), flt, longitude+dec_lon, latitude+dec_lat))

   #longitude = longitude+dec_lon
   #latitude =latitude+dec_lat

    
   #print (latitude, longitude)
#------------Generate random geolocation latitude & longitude------------------



    print (latitude[i], longitude[i])
    #using shell command to acces mosquitto_pub
    #os.system('ls -la')
    #os.system("mosquitto_pub -h localhost -t 'iot/data/iotmmsa0e6fe04b/v1/96a4e75e-db6c-4b0a-a79f-bb8605e35436' -m '{\"mode\":\"async\",\"messageType\":\"6acdf37c3cbcd43aa0ea\",\"messages\":[{\"timestamp\":1591967590,\"temperature\":\"36\", \"longitude\":\"2.35095\", \"latitude\":\"48.85684\"}]}'")
    os.system("mosquitto_pub -h localhost -t 'iot/data/iotmmsa0e6fe04b/v1/96a4e75e-db6c-4b0a-a79f-bb8605e35436' -m '{\"mode\":\"async\",\"messageType\":\"6acdf37c3cbcd43aa0ea\",\"messages\":[{\"timestamp\": %d ,\"temperature\":%d, \"longitude\":%2f, \"latitude\":%3f}]}'" % (timestamp, temperature, longitude[i], latitude[i]))
    i = i + 1
    time.sleep(5)
