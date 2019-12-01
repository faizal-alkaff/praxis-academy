#!/bin/bash
echo "Enter Your Program Name"
read name
program=`/bin/ps.exe -W | grep ${name}.exe`
if [[ -n $program ]]; then
PID=`echo $program | awk '{print $1}'`
echo "Kill Program"
echo ${program}
/bin/kill.exe -f $PID
fi

