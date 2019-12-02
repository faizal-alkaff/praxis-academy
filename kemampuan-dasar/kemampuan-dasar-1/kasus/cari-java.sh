#!/bin/bash
find=`find $1 -name "*.java" -exec dirname {} \; | sort -u`

if [[ `echo $find | grep / | wc -l` -ne 0 ]]; then
#printf '%s\n' "Ada file Java pada direktori" $find
printf '%s\n' $find | awk '{print "Ada file Java pada direktori",$0}'
fi
