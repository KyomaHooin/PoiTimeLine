#!/bin/bash
#
# Theorist - Metadata
#

export LC_NUMERIC="en_US.UTF-8"

SOURCE="/home/user/Desktop/Theorist/"
TARGET="/home/user/Desktop/Theorist_meta"

mkdir "$TARGET" 2>/dev/null

cd "$SOURCE"
for D in $(find . -mindepth 1 -maxdepth 1 -type d -printf '%P\n'); do
 echo "[*] $D: conversion:"

 echo -n "[*] $D: creating target direcory... "
 mkdir "$TARGET/$D" 2>/dev/null
 echo "[done]"

 for F in $(find "$SOURCE/$D" -type f -printf "%P\n"); do


  FN=$(basename "$D/$F")
  OUT="$TARGET/$D/$FN"

  DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$D/$F") 
  DURATION=$(printf "%.0f" "$DURATION") 

  echo -n "[*] $FN: creating target directory... "
  mkdir "$OUT" 2>/dev/null
  echo "[done]"

  echo -n "[*] $FN: writing metadata... "
  ffmpeg -v error -y -i "$D/$F" -f ffmetadata "$OUT/$FN.meta"
  echo "[done]"

  if [ "$DURATION" -gt 20 ];then

   echo -n "[*] $FN: writing intro... "
   ffmpeg -v error -y -i "$D/$F" -ss 0 -t 20 -c copy "$OUT/intro-$FN"
   echo "[done]"

   echo -n "[*] $FN: writing outro... "
   ffmpeg -v error -y -sseof -20 -i "$D/$F" -c copy "$OUT/outro-$FN"
   echo "[done]"

  else

   echo -n "[*] $FN: writing full... "
   cp "$D/$F" "$OUT/ful-$FN"
   echo "[done]"

  fi

  echo -n "[*] $FN: writing audio... "
  ffmpeg -v error -y -i "$D/$F" "$OUT/$FN.mp3"
  echo "[done]"

 done
done

exit 0
