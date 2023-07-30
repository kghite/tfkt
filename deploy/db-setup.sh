#!/bin/bash

docker-compose up -d
sleep 5
docker-compose exec db createdb tracer --user tracer-dev
docker-compose exec web python ./manage.py migrate