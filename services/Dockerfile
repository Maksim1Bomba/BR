FROM nginx:1.26-alpine

# RUN apk update

COPY ./nginx.conf /etc/nginx/
COPY ./frontend/404.html ./frontend/app.html ./frontend/index.js /usr/share/nginx/
COPY ./cert/archive /etc/letsencrypt/archive
COPY ./cert/live/ /etc/letsencrypt/live
COPY ./repositories /etc/apk/repositories