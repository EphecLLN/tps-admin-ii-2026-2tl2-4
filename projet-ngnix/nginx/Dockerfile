FROM nginx:alpine

# Supprime la config par défaut de l'image de base
RUN rm /etc/nginx/conf.d/default.conf

# Copie ta nouvelle config et tes certificats
COPY default.conf /etc/nginx/conf.d/
COPY ssl/ /etc/nginx/ssl/
