# IMAGEN BASE Python 3.12
FROM python:3.12-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto donde corre Flask
EXPOSE 1001

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
