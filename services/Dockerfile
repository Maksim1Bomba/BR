FROM nginx:1.26-alpine

# RUN apk update

COPY ./nginx.conf /etc/nginx/
COPY ../frontend/* /usr/share/nginx/
COPY ./cert/archive /etc/letsencrypt/archive
COPY ./cert/live/ /etc/letsencrypt/live
COPY ./repositories /etc/apk/repositories