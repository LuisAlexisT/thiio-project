# Proyecto Técnico para Thiio

## Descripción

Este proyecto consiste en configurar un entorno de desarrollo utilizando Docker Compose. Incluye los siguientes servicios:

- Laravel Application
- Nginx
- MySQL
- Random HTTP Docker Image (Opcional)

## Requisitos

- Docker
- Docker Compose

## Pasos para Ejecutar la Aplicación

```sh
# Clonar el Repositorio
git clone https://github.com/LuisAlexisT/tu-repositorio.git
cd tu-repositorio

# Configurar Variables de Entorno
# Copiar .env.example a .env y configurar según sea necesario
# Asegúrate de definir NGINX_CONF_FILE para especificar el archivo de configuración de Nginx a utilizar

# Generar la Clave de Laravel
docker-compose run --rm laravel-app php artisan key:generate

# Levantar los Contenedores sin el servicio random
docker-compose up --build

# Levantar los Contenedores con el servicio random
docker-compose --profile random up --build
```

## Configuración Adicional
Archivo Hosts
Para acceder a devops.test en tu navegador, asegúrate de agregar la siguiente línea a tu archivo hosts:
```sh
127.0.0.1 devops.test
```

## Variables de Entorno
- Laravel .env: Puedes definir variables de entorno específicas de Laravel en el archivo .env ubicado en el directorio raíz del proyecto Laravel.
- Variables de Entorno Globales: Las variables de entorno globales para la configuración del entorno Docker se pueden definir en el archivo .env ubicado en el directorio raíz del proyecto, aqui se configura "NGINX_CONF_FILE", el cual puede tener los archivos de configuración, default o default with  random, para activar ek servicio random http:
```sh
   - default_with_random.conf
   - default.conf
```

## Acceder a la Aplicación
Accede a la aplicación Laravel en el navegador: http://devops.test
Si se activa, accede al servicio Random HTTP: http://devops.test/thiio

## Problemas Comunes
- Configuración Incorrecta de Docker, ya sea que necesites iniciar sesion o descargar las imagenes por separado con los siguientes comandos.
```sh
   docker pull nginx:alpine
   docker pull mysql:5.7
   docker build -t laravel ./laravel
```
- Creación de App Key de Laravel, solo necesitas ejecutar el siguiente comando dentro de la carpeta del proyecto de laravel.
```sh
   php artisan key:generate
```
## Contacto
Si tienes alguna pregunta o encuentras algún problema, por favor contacta a LuisAlexisT en GitHub o envía un correo electrónico a alextepe27@gmail.com.