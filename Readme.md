# BladeRunner 2049

Films shop, about buying access for watching film 

## Programminng languages

- python
- typescript

## Backing services

- nginx
- postgres

## Install

My project was built due to docker so lots of modules not necessary to use. I use simple version of docker, not docker-compose. To install it, do:		

```
 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Test your installation:

```
sudo docker run hello-world
```
For more information: info(https://docker-curriculum.com/)

Nginx for working with https requires certificates (domain name, expire and so on), certbot help determine this problem:

```
sudo snap install --classic certbot
```

If you have had old versions of certbot, reinstall it:

```
sudo apt-get remove certbot
sudo snap install --classic certbot
```
All files was recived in ./services/cert/

## Run

### Server
For backend you need python 3.10. Main libr for server is socket. Most of modules was writed with OOP.

### Services
Services contain nginx and postgres, nginx take js and html files to give them client

Start the server in docker conteiner, you just need to type some commands shown below:

```
sh build.sh
sh run.sh 
```

## Copywright

2025 Egor