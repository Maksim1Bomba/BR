sudo certbot certonly --standalone  -d your_domain --config-dir ./services/nginx/cert/ --email example@mail.com --agree-tos --force-renewal;

sudo chown -R your_name:your_name ./services/nginx/cert;
