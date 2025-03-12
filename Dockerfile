# Usa una imagen de Python optimizada
FROM python:3.11-slim

# Define el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia y instala dependencias
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . /code/

# Exponer el puerto en el que correrá Django
EXPOSE 8000

# Ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
