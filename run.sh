docker run --rm -it --name nginx --network net -p 80:8080 nginx;
docker run --rm -it --name server --network net -p 80:80 -p 443:443 server;
