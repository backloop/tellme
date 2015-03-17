#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import time
#http://jsonlint.com
import json  
import os

# add path to files to that script can be executed from 
# other folders
dirname = os.path.dirname(os.path.realpath(__file__))

source = dirname + os.sep + "data.txt"
dest_temperature = dirname + os.sep + "data-temperature.json"
dest_humidity = dirname + os.sep + "data-humidity.json"

temperatures = {}
humidities = {}

with open( source, "r") as sf:
    for line in sf:
	parts = line.split()
	
	# only use id and first word in name
	label = '-'.join(parts[0:2])
	
	# skip rest of name (i.e. 'temp/RH' part)
	
	strptime = ' '.join(parts[-4:-2])
	timestamp = int(1000 * time.mktime(datetime.datetime.strptime(strptime, "%Y-%m-%d %H:%M:%S").timetuple()))
	
	temperature = float(parts[-2])
	humidity = float(parts[-1])

	temp = temperatures.get(label, [])
	temp.append([timestamp, temperature])
	temperatures[label] = temp

	temp = humidities.get(label, [])
	temp.append([timestamp, humidity])
	humidities[label] = temp

top = []
for [key, value] in temperatures.iteritems():
    top.append({"label": key, "data": value})
df = open(dest_temperature, "w")
df.write(json.dumps(top))
df.close()

top = []
for [key, value] in humidities.iteritems():
    top.append({"label": key, "data": value})
df = open(dest_humidity, "w")
df.write(json.dumps(top))
df.close()
