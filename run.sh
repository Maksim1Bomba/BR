docker run --rm --name postgres -e --network net -d -p 5432:5432 -v hs1:/var/lib/postgresql/data postgres;
docker exec -i postgres psql -U a1337 -d a1337 < ./services/psql/database.sql;

docker run --rm -it --name server --network net -p 8080:8080 server & docker run --rm -it --name nginx --network net -p 80:80 -p 443:443 -v ./frontend/*:/usr/share/nginx/ nginx;
