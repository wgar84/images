#! /usr/bin/bash

mkdir "$(pwd)"/../../volumes/postgis_brasil

docker volume create \
    --opt type=none \
    --opt device="$(pwd)"/../../volumes/postgis_brasil \
    --opt o=bind \
    postgis_brasil

docker build . -t postgis_feeder