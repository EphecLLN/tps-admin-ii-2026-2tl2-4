#/bin/bash

set -e

default_version="3"
version=${1:-"$default_version"}


docker build -t timo62559/woody_api:"$version" api 
docker tag timo62559/woody_api:"$version" timo62559/woody_api:latest

docker build -t timo62559/woody_rp:"$version" reverse-proxy
docker tag timo62559/woody_rp:"$version" timo62559/woody_rp:latest

docker build -t timo62559/woody_database:"$version" database
docker tag timo62559/woody_database:"$version" timo62559/woody_database:latest

docker build -t timo62559/woody_front:"$version" front
docker tag timo62559/woody_front:"$version" timo62559/woody_front:latest


# avec le "set -e" du début, je suis assuré que rien ne sera pushé si un seul build ne c'est pas bien passé

docker push timo62559/woody_api:"$version"
docker push timo62559/woody_api:latest

docker push timo62559/woody_rp:"$version"
docker push timo62559/woody_rp:latest

docker push timo62559/woody_front:"$version"
docker push timo62559/woody_front:latest

docker push timo62559/woody_database:"$version"
docker push timo62559/woody_database:latest
