#! /usr/bin/bash

mkdir "$(pwd)"/../../volumes/brasil

docker volume create \
    --opt type=none \
    --opt device="$(pwd)"/../../volumes/brasil \
    --opt o=bind \
    pg_brasil

# docker build . -t pg_build