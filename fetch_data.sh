#!/bin/bash
while true
do
	python3 manage.py runscript fetch_data
	sleep 40
done
