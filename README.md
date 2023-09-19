DESCRIPTION

Early Poi spinning documentation project.

https://jquery-plugins.net/building-vertical-timeline-with-css-and-javascript
https://codyhouse.co/gem/vertical-timeline/

TODO

- Page core.
- Metadata harvest:
  extract frame -> ffmpeg -i $FILE -vf "select=eq(n\,35)" -vframes 1 $OUT.png
  extract metadata -> ffprobe

METADATA
<pre>
"file":{
	"metadata":{
		"name":"Rusty",
		"format":"WMV",
		"length":"290"
		"author":["Skunk","Nomad"],
		"edit":["Skunk"],
		"date":"2003",
	"title": {
		"performer":["Le Skunk","NYC],
		"name":["Daniel Holler","?"],
		"location":["Washington Square Park"],
		"country":["US"],
		"music":["1L/Das Nonstop-Programm - Elextrovulse"],
		"date":"8.3.2003"
		"tag":["1L Courtesy of Res Freq Records", "FlambeVolupte","1337","ANTHELION","res-freq.com","1337bu.org","antelion.net"]
}
</pre>
