docker build -t nginx ./services;
docker build -t server ./backend;

sudo docker network create -d bridge net;
