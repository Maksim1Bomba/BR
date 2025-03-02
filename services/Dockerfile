FROM nginx:1.27.4-alpine-slim

# RUN apk update

COPY ./nginx.conf /etc/nginx/
COPY ./static/* /usr/share/nginx/
COPY ./cert/archive /etc/letsencrypt/archive
COPY ./cert/live/ /etc/letsencrypt/live