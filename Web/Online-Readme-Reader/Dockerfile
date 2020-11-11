# Based on https://github.com/justcatthefish/justctf-2019/blob/master/challenges/web_firmwareupdater/private/Dockerfile
FROM php:7.4-apache

# RUN apt-get update && apt-get install -y zlib1g-dev libzip-dev && apt-get clean
# RUN docker-php-ext-install zip
RUN apt-get update && apt-get install -y unzip && apt-get clean

# Dumb name to not be dirb'd
RUN mkdir '/var/www/html/uploadzzz'

COPY ./private/flag.txt /etc/flag
COPY ./private/index.html /var/www/html
COPY ./private/read.php /var/www/html
