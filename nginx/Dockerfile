FROM nginx:1.21-alpine

WORKDIR /www

COPY django/static ./static
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
