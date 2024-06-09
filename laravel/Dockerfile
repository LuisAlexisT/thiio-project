# Dockerfile para Laravel
FROM php:8.0-fpm-alpine

# Instalación de dependencias
RUN apk add --no-cache \
    bash \
    mysql-client \
    libpng-dev \
    libjpeg-turbo-dev \
    libwebp-dev \
    freetype-dev \
    zip \
    libzip-dev \
    unzip \
    oniguruma-dev

# Instalación de extensiones de PHP
RUN docker-php-ext-configure gd --with-freetype --with-jpeg --with-webp \
    && docker-php-ext-install pdo pdo_mysql mbstring gd zip

# Instalación de Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Copiar el código de Laravel al contenedor
WORKDIR /var/www
COPY . .

# Exponer el puerto 9000 para php-fpm
EXPOSE 9000

CMD ["php-fpm"]