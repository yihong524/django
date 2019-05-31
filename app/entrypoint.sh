#!/bin/sh

# GUNICORN=/usr/local/bin/gunicorn
# ROOT=/path/to/project
# PID=/var/run/gunicorn.pid

APP=web_project.wsgi:application

# if [ -f $PID ]; then rm $PID; fi

exec gunicorn -c gunicorn.conf.py $APP