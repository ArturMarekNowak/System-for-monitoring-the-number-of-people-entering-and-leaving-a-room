#!/bin/bash
echo "Start of the scripts"
SECONDS=0

python3 detection/publisher.py & 
#python3 detection/demo.py haar &
python3 tests/testDetection.py c &

while : 
do

	echo "Press q to quit"
		
	read quit
	
	if [ "$quit" = "q" ]
	then
		echo "Stopping"
		ps axf | grep testDetection.py | grep -v grep | awk '{print "kill -9 " $1}' | sh
		ps axf | grep publisher.py | grep -v grep | awk '{print "kill -9 " $1}' | sh
		duration=$SECONDS
		break
	else
		echo "Continuouing"
	fi
done

echo "Runtime: $(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed" 
