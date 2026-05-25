#!/bin/bash
#
# Copy PTL tooolkit structure to Jekyll frontend structure
#

BASE='/home/user/Desktop/project'

TARGET='/tmp/PoiTimeLine'

# copy screen + image

mkdir -p "$TARGET/assets/PTL/screen/" 2>/dev/null
mkdir -p "$TARGET/assets/PTL/image/" 2>/dev/null

find "$BASE/YAML/video/" -type f -name "*.jpg" -exec cp {} "$TARGET/assets/PTL/screen/" \;
find "$BASE/YAML/artist/" -type f -name "*.jpg" -exec cp {} "$TARGET/assets/PTL/image/" \;

# copy video

mkdir -p "$TARGET/_data/PTL/" 2>/dev/null

rsync -av --exclude '*.jpg' "$BASE/YAML/video/" "$TARGET/_data/PTL/"

# concat artist + group

mkdir -p "$TARGET/_artist/" 2>/dev/null
mkdir -p "$TARGET/_group/" 2>/dev/null

cat "$BASE/YAML/artist/"*.md > "$TARGET/_artist/artist.md"
cat "$BASE/YAML/group/"*.md  > "$TARGET/_group/group.md"

