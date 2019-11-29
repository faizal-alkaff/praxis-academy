#!/bin/bash
find=`find $1 -name "*.java" -exec dirname {} \; | sort -u`

if [[ `echo $find | grep / | wc -l` -ne 0 ]]; then
echo "Ada file Java pada direktori $find"
fi
