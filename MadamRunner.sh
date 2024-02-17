#!/bin/bash

while true; do
	
	if ping -q -c 1 google.com &> /dev/null; then
		
		python3 /home/ada/MadamEve/bot.py
		break
	else
		sleep 5
	fi
done