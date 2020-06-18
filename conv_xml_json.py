import xmltodict
import json
import os

# convert xml to json
with open('route.gpx') as xml_file:
    my_dict=xmltodict.parse(xml_file.read())
xml_file.close()
json_data=json.dumps(my_dict)
print(json_data)

# output file
out_file = open("route_conv.json", "w") 
json.dump(my_dict, out_file, indent = 4) 
out_file.close() 