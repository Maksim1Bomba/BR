sudo certbot certonly --standalone  -d your_domain_name --config-dir ./services/nginx/cert/ --email your_email --agree-tos --force-renewal;

sudo chown -R your_name:your_name ./services/nginx/cert;
