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

"We came whirling out of nothingness, glittering stars like dust,
start that made a circle, where in the middle, we dance."

http://www.homeofpoi.com/ubbthreads/images/users/796.jpg
https://web.archive.org/web/20061214070131/http://www.homeofpoi.com/ubbthreads/showprofile.php?Cat=0&User=1571


A.N.T.H.E.L.I.O.N
Peregrine, Samiya, Anisa, Nomad, Code128, Tito
(filmed by Daniel Furst)
Boston, MA, USA

Tempest (Liam), Rumplestiltskin (Nathan), Phat Boy (Aiden Tempest)
Cheshire
UK 

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

nextfrme=e

storefrme=shift+s
</pre>

STAGE
<pre>
ffmpeg -> 10s clip  start + end
ffmpeg -> audio
ffmpeg -> metadata
</pre>
