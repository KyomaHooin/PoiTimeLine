#!/usr/bin/python
#
# JSON generator
#
# Struct:
#
# "video": {
#	"name":"",
#	"date":"",		<- DD.MM.YYYY
#	"size":"",		<- Mb
#	"duration":"",		<- min
#	"location":[],
#	"artist":[],
#	"music":[],
#	"meta":[]
# }

import os, json

print "\n--# JSON Generator #--\n"

dn,name,date,size,duration = '','','','',''
location,artist,music,meta = [],[],[],[]

video = {}

while not dn: dn = raw_input("Dir: ")
while not name: name = raw_input("Name: ")
while not date: date = raw_input("Date: ")
while not size: size = raw_input("Size: ")
while not duration: duration = raw_input("Duration: ")

video['name'] = name
video['date'] = date
video['size'] = size
video['duration'] = duration

while 1:
	l = raw_input("Location: ")
	if l == '.': break
	if l: location.append(l)
while 1:
	a = raw_input("Artist: ")
	if a == '.': break
	if a: artist.append(a)
while 1:
	m = raw_input("Music: ")
	if m == '.': break
	if m: music.append(m)
while 1:
	m = raw_input("Meta: ")
	if m == '.': break
	if m: meta.append(m)

video['location'] = location
video['artist'] = artist
video['music'] = music
video['meta'] = meta

# PREVIEW
preview = raw_input("\nShow preview? [y/n]: ")
if preview == 'y': print(json.dumps(video, indent=2))

# WRITE
try:
	os.mkdir(dn)
except: pass

fn = name.split('.')[0]
write = raw_input('Write to file ' + '[' + dn + '/' + fn + '.json ]? [y/n]: ')
if write == 'y':
	f = open(dn + '/' + fn + '.json', 'a')
	f.write(json.dumps(video))
	f.close()
	print "Done."

