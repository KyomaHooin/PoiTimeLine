#!/usr/bin/python
#
# JSON generator
#
# Struct:
#
# "artist": {
#	"name":"",
#	"nick":[],
#	"origin":[],
#	"website":"",
#	"video":[],
#	"meta":[]
# }

import os, json

print "\n--# JSON Generator #--\n"

dn,name,origin, web = '','','',''
nick,video,meta = [],[],[]

artist = {}

while not dn: dn = raw_input("Dir: ")
while not name: name = raw_input("Name: ")
while not origin: origin = raw_input("Origin: ")
while not web: web = raw_input("Website: ")

artist['name'] = name
artist['origin'] = origin
artist['web'] = web

while 1:
	n = raw_input("Nick: ")
	if n == '.': break
	if n: nick.append(n)
while 1:
	v = raw_input("Video: ")
	if v == '.': break
	if v: video.append(v)
while 1:
	m = raw_input("Meta: ")
	if m == '.': break
	if m: meta.append(m)

artist['nick'] = nick
artist['video'] = video
artist['meta'] = meta

# PREVIEW
preview = raw_input("\nShow preview? [y/n]: ")
if preview == 'y': print(json.dumps(artist, indent=2))

# WRITE
write = raw_input('Write to file ' + '[' + dn + '/' + dn + '.json ]? [y/n]: ')
if write == 'y':
	f = open(dn + '/' + dn + '.json', 'a')
	f.write(json.dumps(artist))
	f.close()
	print "Done."

