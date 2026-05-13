# Usamos una versión ligera de Python
FROM python:3.12-slim

# Instalamos 'uv' dentro del contenedor para que sea veloz
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Establecemos la carpeta de trabajo
WORKDIR /app

# Copiamos los archivos de configuración primero (para aprovechar la caché)
COPY pyproject.toml .

# Instalamos las dependencias
RUN uv pip install --system -r pyproject.toml

# Copiamos el resto del código (incluyendo el modelo entrenado)
COPY . .

# Exponemos el puerto 8000 que es el que usa FastAPI
EXPOSE 8000

# Comando para arrancar la API cuando el contenedor inicie
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]