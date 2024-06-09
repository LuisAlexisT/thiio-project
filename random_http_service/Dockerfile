# Usa una imagen base de Python
FROM python:3.9-alpine

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requisitos y la aplicación al contenedor
COPY requirements.txt requirements.txt
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 80
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]