# Technical Project for Thiio

## Description

This project involves setting up a development environment using Docker Compose. It includes the following services:

- Laravel Application
- Nginx
- MySQL
- Random HTTP Docker Image (Optional)

## Requirements

- Docker
- Docker Compose

## Steps to Run the Application

```sh
# Clone the Repository
git clone https://github.com/LuisAlexisT/tu-repositorio.git
cd tu-repositorio

# Configure Environment Variables
# Copy .env.example to .env and configure as needed
# Make sure to define NGINX_CONF_FILE to specify the Nginx configuration file to use

# Generate Laravel Key
docker-compose run --rm laravel-app php artisan key:generate

# Start Containers without the random service
docker-compose up --build

# Start Containers with the random service
docker-compose --profile random up --build
```

## Additional Configuration
Hosts File
To access devops.test in your browser, make sure to add the following line to your hosts file:
```sh
127.0.0.1 devops.test
```

## Environment Variables
- Laravel .env: You can define Laravel-specific environment variables in the .env file located in the root directory of the Laravel project.
- Global Environment Variables: Global environment variables for Docker environment configuration can be defined in the .env file located in the root directory of the project. Here, "NGINX_CONF_FILE" is configured, which can have the configuration files, default or default with random, to activate the random HTTP service:
```sh
   - default_with_random.conf
   - default.conf
```

## Accessing the Application
Access the Laravel application in the browser: http://devops.test
If activated, access the Random HTTP service: http://devops.test/thiio

## Common Issues
- Incorrect Docker Configuration, whether you need to log in or download the images separately using the following commands.
```sh
   docker pull nginx:alpine
   docker pull mysql:5.7
   docker build -t laravel ./laravel
```
- Creating Laravel App Key, you only need to execute the following command within the Laravel project folder.
```sh
   php artisan key:generate
```
## Contact
If you have any questions or encounter any issues, please contact LuisAlexisT on GitHub or send an email to alextepe27@gmail.com.