# Usa una imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios
COPY . /app/

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
