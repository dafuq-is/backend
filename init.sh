#!/bin/bash

source ./.env

FILE='src/index.py'
INIT="DAFUQ_IS_WORDNIK_API_KEY=${DAFUQ_IS_WORDNIK_API_KEY} python3 ${FILE} &"
LAST_MODIFIED=`date -r ${FILE}`

function boot
{
    PID=$(lsof -i:${APP_PORT} | grep Python | awk 'NR==1{print $2}')

    if [[ -n "${PID}" ]]; then
        kill ${PID} 2>/dev/null
    fi

   eval ${INIT}
}

function listen
{
    while true
    do
        MODIFIED=`date -r ${FILE}`
        if [[ "$MODIFIED" != "$LAST_MODIFIED" ]]; then
            echo 'Rebooting...'
            boot

            LAST_MODIFIED=${MODIFIED}
        fi

        sleep 1
    done
}

# Start script
boot

# Listen for changes
listen
