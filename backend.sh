#!/bin/bash
#
# Copy PTL tooolkit structure to Jekyll frontend structure
#

BASE='/home/user/Desktop/project'

TARGET='/tmp/PoiTimeLine'

# copy screen + image

mkdir -p "$TARGET/assets/screen/" 2>/dev/null
mkdir -p "$TARGET/assets/image/" 2>/dev/null

find "$BASE/YAML/video/" -type f -name "*.jpg" -exec cp {} "$TARGET/assets/screen/" \;
find "$BASE/YAML/artist/" -type f -name "*.jpg" -exec cp {} "$TARGET/assets/image/" \;

# copy video data file

mkdir -p "$TARGET/_data/video/" 2>/dev/null

rsync -av --exclude '*.jpg' "$BASE/YAML/video/" "$TARGET/_data/video/"
find "$TARGET/_data/video/" -type f -name "*.md" | xargs rename 's/\.md$/\.yml/' *.md

# concat artist + group

mkdir -p "$TARGET/PTL/_artist/" 2>/dev/null
mkdir -p "$TARGET/PTL/_group/" 2>/dev/null

rsync -av --exclude '*.jpg' "$BASE/YAML/artist/" "$TARGET/PTL/_artist/"
rsync -av --exclude '*.jpg' "$BASE/YAML/group/" "$TARGET/PTL/_group/"

# create video collection
#
# /PTL/_video/name.md -> name: ... layout: video ...
#
