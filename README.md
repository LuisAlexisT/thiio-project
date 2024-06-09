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

Acceder a la Aplicación
Accede a la aplicación Laravel en el navegador: http://devops.test
Si se activa, accede al servicio Random HTTP: http://devops.test/thiio
Configuración Adicional
Archivo Hosts
Para acceder a devops.test en tu navegador, asegúrate de agregar la siguiente línea a tu archivo hosts:
127.0.0.1 devops.test
Variables de Entorno
Laravel .env: Puedes definir variables de entorno específicas de Laravel en el archivo .env ubicado en el directorio raíz del proyecto Laravel.
Variables de Entorno Globales: Las variables de entorno globales para la configuración del entorno Docker se pueden definir en el archivo .env ubicado en el directorio raíz del proyecto.
Problemas Comunes
# Configuración Incorrecta de Docker
# Creación de App Key de Laravel
Contacto
Si tienes alguna pregunta o encuentras algún problema, por favor contacta a LuisAlexisT en GitHub o envía un correo electrónico a alextepe27@gmail.com.