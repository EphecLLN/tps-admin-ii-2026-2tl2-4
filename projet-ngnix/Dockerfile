FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /var/www/html/www
RUN mkdir -p /var/www/html/blog
