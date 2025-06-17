FROM nginx:1.26-alpine

COPY frontend/404.html frontend/login.html frontend/index.html frontend/login.js /usr/share/nginx
COPY services/nginx/nginx.conf /etc/nginx
COPY services/nginx/cert/archive /etc/letsencrypt/archive
COPY services/nginx/cert/live/ /etc/letsencrypt/live
COPY services//nginx/repositories /etc/apk/repositories