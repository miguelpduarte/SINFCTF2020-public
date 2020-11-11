# Based on https://github.com/justcatthefish/justctf-2019/blob/master/challenges/web_firmwareupdater/private/Dockerfile
FROM php:7.4-apache

RUN docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable pdo_mysql

COPY ./private/logout.php /var/www/html
COPY ./private/index.html /var/www/html
COPY ./private/styles.css /var/www/html
COPY ./private/login.php /var/www/html
COPY ./private/flag.php /var/www/html
COPY ./private/flag.txt /etc/flag
