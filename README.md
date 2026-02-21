DESCRIPTION

Early Poi spinning documentation project.

https://jquery-plugins.net/building-vertical-timeline-with-css-and-javascript
https://codyhouse.co/gem/vertical-timeline/


Missing: (wayback 2001)

AnthelionFireVideoDSL06b.mov

061203yutaaska.wmv

Here is a one minute clip of ShadowFire spinning fire to "Bombs over Bagdad" by OutKast. ShadowFire is from  San Antonio, Texas , USA

mvc-001v.mpg 1.3M

skunk.mov

1.7M

Skunk from Snowy, NYC, USA. Doing Fire poi in the snow.

"We came whirling out of nothingness, glittering stars like dust,
start that made a circle, where in the middle, we dance."

(HOP COL1/2/3.php wayback harvest)
Jedi White
John Smith, J.T. Smith
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

Xaeda
Jacinta Patterson
Dunedin, New Zealand 

Nomad
Joseph Donyo
Somerville, MA, USA

Sage
Shawn Robertson
Austin, TX, USA

ARCHITECTURE
<pre>

2002|----- XXX
    |
2003|----- XXX
    |
    |
...

[collection]
|--[mcp]
|----[*]lab2.avi
|----[*]lab3.avi
|--[TePooka]
|----[*]rubbish.avi
....

/assets/icons/mcp.png
/assets/video/lab2.png

/_data/artst.md <- dataset
/_data/group.md <- dataset

/video/mcp/_post/YEAR-MONTH-DAY-lab2.md
/video/mcp/_post/YEAR-MONTH-DAY-lab3.md
</pre>
STRUCT
<pre>
JSON->Markdown-templater.py->

struct:video|artist|group

COLLECTION video: name, fn, date, music, performer(tag), screenshot(asset), size, duration
artist: HOP icon, nickname(list), firstname, surname, country, location
group: name, artist, country, location

</pre>
TODO
<pre>
lphlist
</pre>
META
<pre>
Metadata: ffprobe
VLC: [e] = next frame; [shift] + [e] = screenshot
Resize: mogrify -resize 320x224\! *.png
</pre>
