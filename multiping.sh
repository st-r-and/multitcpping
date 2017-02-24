#!/bin/bash

Hostname=`/bin/hostname`
Trace="/bin/traceroute -I"
Nmap="nmap -p 80,443"
Num=0
Fai=0
for server in `cat ./serverlist.sort | sort --random-sort`
do
 Num=$(($Num + 1)) # server count
 echo -n "$server "
 test=`$Nmap $server | grep done | sed -r -e 's/.*\(([^]]*)\).*/\1/'`
 res=$(echo $test | cut -d" " -f1)
 pri=$(echo $test | sed 's/0/\\\033\[31m0\\\033\[0m/')
 echo -e $pri
 if [ "$res" -eq 0 ]; then
  Fai=$(($Fai +1)) # fail count
 fi
done

echo -n "Server: "
echo $Num
echo -n "Fehler: "
echo $Fai
