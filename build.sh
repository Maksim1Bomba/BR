docker volume create hs1;

docker build -t nginx ./services;
docker build -t server ./backend;

sudo docker network create -d bridge net;

sudo certbot certonly --standalone  -d your_domain_name --config-dir ./services/nginx/cert/ --email your_email --agree-tos --force-renewal
