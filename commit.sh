#!/bin/bash
#
# Simple non-root commit script
#

git add .
git commit -m "$(uuidgen)"
git push origin main

