DESCRIPTION

Early Poi spinning documentation project.

https://jquery-plugins.net/building-vertical-timeline-with-css-and-javascript
https://codyhouse.co/gem/vertical-timeline/

"We came whirling out of nothingness, glittering stars like dust,
start that made a circle, where in the middle, we dance."

(HOP COL1/2/3.php wayback harvest)
Jedi White
John Smith
Stillwater, OK, USA 

Daniel Tyler
Wrap Master Funk
Stillwater, OK, USA

Skunk
New York City, NY, USA 

A.N.T.H.E.L.I.O.N
Peregrine, Samiya, Anisa, Nomad, Code128, Tito
(filmed by Daniel Furst)
Boston, MA, USA

Nix?
Tom Caine
Totness, Devon, UK

Tempest (Liam), Rumplestiltskin (Nathan), Phat Boy (Aiden Tempest)
Cheshire
UK 

Bender the Offender
Bill La
Melbourne, VIC Australia

Antti Suniala
Antti Suniala
Finland 

Dio - Wildfire Entertainment
Vernon Skach
Stillwater, OK, USA

Yuta
Yuta Ushiogi
Tokyo, Japan 

Xaeda
Jacinta Patterson
Dunedin, New Zealand 

Nomad
Joseph Donyo
Somerville, MA, USA

Sage
Shawn Robertson
Austin, TX, USA
TODO

- Page core
  - dir struct
  - listing cards
  - timeline + world map scatter
  - Search
  - Video
  - Picture
  - Artist profile
  - Text
  - Archive
  - Wanted
  - Contact

- Metadata harvest:
  extract frame -> ffmpeg -i $FILE -vf "select=eq(n\,35)" -vframes 1 $OUT.png
  extract metadata -> ffprobe

METADATA
<pre>
"file":{
	"metadata":{
		"name":"Rusty",
		"format":"WMV",
		"length":"290",
		"size":"",
		"author":["Skunk","Nomad"],
		"edit":["Skunk"],
		"date":"2003",
	"title": {
		"date":"8.3.2003",
		"author":["Skunk","Nomad"],
		"editor":["Skunk"],
		"performer":["Le Skunk","NYC],
		"name":["Daniel Holler","?"],
		"location":["Washington Square Park"],
		"City":["Washington"],
		"country":["US"],
		"music":["1L/Das Nonstop-Programm - Elextrovulse"],
		"metadata":["1L Courtesy of Res Freq Records", "FlambeVolupte","1337","ANTHELION","res-freq.com","13378u.org","antelion.net"]
}
</pre>
