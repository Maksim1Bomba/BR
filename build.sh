docker volume create hs1;

sudo certbot certonly --standalone  -d your_domain_name --config-dir /your/path/to/cert --email your_email --agree-tos --force-renewal;
sudo chown -R your_name:your_name ./services/nginx/cert;


docker build -t nginx ./services/nginx/;
docker build -t server ./backend;

sudo docker network create -d bridge net;
