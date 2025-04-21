docker volume create hs1;

sudo certbot certonly --standalone  -d your_domain_name --config-dir /your/path/to/cert --email your_email --agree-tos --force-renewal;
sudo chown -R your_name:your_name ./services/nginx/cert;

docker build -t postgres ./services/psql/;
docker build -t nginx -f ./services/nginx/Dockerfile .;
docker build -t server ./backend;

sudo docker network create -d bridge net;

docker run --rm --name postgres -e --network net -d -p 5432:5432 -v hs1:/var/lib/postgresql/data postgres;
docker exec -i postgres psql -U your_user -d database_name < ./services/psql/database.sql;


