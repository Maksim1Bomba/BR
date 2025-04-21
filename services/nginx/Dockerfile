FROM nginx:1.26-alpine

COPY frontend/404.html frontend/hello.html frontend/index.html frontend/login.js /etc/nginx/
COPY services/nginx/nginx.conf /usr/share/nginx/
COPY services/nginx/cert/archive /etc/letsencrypt/archive
COPY services/nginx/cert/live/ /etc/letsencrypt/live
COPY services//nginx/repositories /etc/apk/repositories