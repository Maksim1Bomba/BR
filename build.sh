sudo certbot certonly --standalone  -d your_domain --config-dir ./services/nginx/cert/ --email example@mail.com --agree-tos --force-renewal;
sudo chown -R your_name:your_name ./services/nginx/cert;

docker volume create hs1;
docker build -t postgres ./services/psql/;
docker build -t nginx -f ./services/nginx/Dockerfile .;
docker build -t server ./backend;

sudo docker network create -d bridge net;

docker run --name postgres -d -p 5432:5432 -v hs1:/var/lib/postgresql/data postgres;
docker exec -i postgres psql -U boss -d boss < ./services/psql/database.sql;
docker stop postgres;




