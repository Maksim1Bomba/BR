docker run --rm -it --name server --network net -p 8080:8080 server & docker run --rm -it --name nginx --network net -p 80:80 -p 443:443 nginx;
