FROM nginx:latest

# Installation de certbot et du plugin nginx
RUN apt-get update && apt-get install -y \
    certbot \
    python3-certbot-nginx \
    && rm -rf /var/lib/apt/lists/*

# On garde tes copies de config si nécessaire
COPY default.conf /etc/nginx/conf.d/default.conf
