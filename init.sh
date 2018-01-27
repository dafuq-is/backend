#!/bin/bash

[[ -f .env ]] && source ./.env

FILE='src/index.py'
INIT="bash -c 'DAFUQ_IS_WORDNIK_API_KEY=${DAFUQ_IS_WORDNIK_API_KEY} exec -a dafuqis-backend python3 ${FILE} &'"

function boot
{
	[[ `pgrep -f dafuqis-backend` ]] && pkill -f dafuqis-backend
   	eval ${INIT}
	sleep 1
}

function listen
{
	echo "$(date) - - Starting listening for changes...."
    while inotifywait -q -r -e modify src/
    do   		
		clear
		echo "$(date) - - Change detected, restarting...."
		boot
    done
}

# Start script
boot

# Listen for changes
listen
