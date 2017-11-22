#!/bin/sh

clear

git add -A 
git commit -a -m "'$*'"
git pull origin master
git push origin master
