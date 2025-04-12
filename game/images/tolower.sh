#!/bin/sh
OIFS="$IFS"
IFS=$'\n'
for entry in `find .`; do
	rename=`echo $entry | tr '[:upper:]' '[:lower:]'`
	mv $entry $rename
done