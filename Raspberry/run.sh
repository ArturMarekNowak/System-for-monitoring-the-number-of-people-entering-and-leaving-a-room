#!/bin/bash
echo "Start of the scripts"
SECONDS=0

python3 foo.py & 
python3 bar.py &

while : 
do

	echo "Press q to quit"
		
	read quit
	
	if [ "$quit" = "q" ]
	then
		echo "Stoping"
		ps axf | grep bar.py | grep -v grep | awk '{print "kill -9 " $1}' | sh
		ps axf | grep foo.py | grep -v grep | awk '{print "kill -9 " $1}' | sh
		duration=$SECONDS
		break
	else
		echo "Continuouing"
	fi
done

echo "Runtime: $(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed" 
