FROM nginx:1.18.0

WORKDIR /nginx
COPY . /nginx

COPY /conf/project.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf