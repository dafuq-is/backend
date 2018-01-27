#!/bin/bash


[[ -f .env ]] && source ./.env

FILE='src/index.py'
INIT="bash -c 'DAFUQ_IS_WORDNIK_API_KEY=${DAFUQ_IS_WORDNIK_API_KEY} exec -a dafuqis-backend python3 ${FILE} &'"
checksum=$(md5sum $FILE)

function boot
{
	[[ `pgrep -f dafuqis-backend` ]] && pkill -f dafuqis-backend
   	eval ${INIT}
	sleep 1
}

function inotify_watch 
{

	echo "$(date) - - Starting listening for changes...."

    while inotifywait -q -r -e modify src/
    do   		
		clear
		echo "$(date) - - Change detected, restarting...."
		boot
    done
}

function legacy_watch
{
	echo -e "Notice: inotifywait not found in your system. 
- Using legacy method to restart 
- Can restart only if change is detected in index.py. 
- If you want to enjoy feature of restarting on any changes in the directory, then install inotifywait in your system.
	
$(date) - - Started listening for changes...."
	
	while true
	do
		checksum_new=$(md5sum $FILE)
		if [ "$checksum" != "$checksum_new" ]
		then
			checksum=$checksum_new
			echo "$(date) - - Change detected in $FILE, restarting...."
			boot
		fi
		sleep 1
	done
}


function listen
{

	[[ `which inotifywait` ]] && inotify_watch || legacy_watch
}

# Start script
boot

# Listen for changes
listen
