#!/bin/bash
echo "Enter Your Program Name"
read name
program=`/bin/ps.exe -W | grep ${name}.exe`
if [[ -n $program ]]; then
echo $program
PID=`echo $program | awk '{print $1}'`
/bin/kill.exe -f $PID
fi

