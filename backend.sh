#!/bin/bash
#
# Copy PTL tooolkit structure to Jekyll frontend
#

BASE='/home/user/Desktop/project'

TARGET='/tmp/PoiTimeLine'

# copy video snapshots and artist images

mkdir -p "$TARGET/assets/screen/" 2>/dev/null
mkdir -p "$TARGET/assets/picture/" 2>/dev/null

find "$BASE/YAML/video/" -type f -name "*.jpg" | xargs -iSNAP bash -c "cp SNAP $TARGET/assets/screen/"
rsync -av "$BASE/YAML/artist/" --exclude "*.md" "$TARGET/assets/picture/"

# copy video, artist and group data

mkdir -p "$TARGET/_data/video/" 2>/dev/null
mkdir -p "$TARGET/PTL/_artist/" 2>/dev/null
mkdir -p "$TARGET/PTL/_group/" 2>/dev/null

rsync -av --exclude '*.jpg' "$BASE/YAML/video/" "$TARGET/_data/video/"
rsync -av --exclude '*.jpg' --exclude '*.jpeg' --exclude '*.png' "$BASE/YAML/artist/" "$TARGET/PTL/_artist/"
rsync -av --exclude '*.jpg' "$BASE/YAML/group/" "$TARGET/PTL/_group/"

# create video collection

mkdir -p "$TARGET/PTL/_video/" 2>/dev/null

find "$BASE/YAML/video/" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; \
| xargs -iDIR bash -c "echo -e '---\nname: DIR\nlayout: video\n...' >  $TARGET/PTL/_video/DIR.md"

