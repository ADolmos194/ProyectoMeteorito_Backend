# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia solo los archivos necesarios
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# Expone el puerto
EXPOSE 8000

# Comando para iniciar Gunicorn
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT

