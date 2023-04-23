#!/bin/bash

rm $4
echo "Scaning ..."
if [ -z "$5"]
then
    airodump-ng $2 -w $1 -I 5 --output-format csv >/dev/null 2>&1 &
    sleep $3
    kill %1
else
    airodump-ng $2 -w $1 -I 5 --channel $5 --output-format csv >/dev/null 2>&1 &

    sleep $3
    kill %1
fi
