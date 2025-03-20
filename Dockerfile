FROM python:3.10-slim

# Evitar prompts interactivos en la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias básicas
RUN apt-get update && apt-get install -y build-essential git

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer puerto
EXPOSE 5005

# Comando para correr el servidor Rasa
# CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug", "--model", "/app/models/20250313-160938-corn-hour.tar.gz"]
