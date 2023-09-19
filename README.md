DESCRIPTION

Early Poi spinning documentation project.

https://jquery-plugins.net/building-vertical-timeline-with-css-and-javascript
https://codyhouse.co/gem/vertical-timeline/

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
