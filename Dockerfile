# Utilisation d'une image Python légère
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port de l'API
EXPOSE 8000

# Commande pour démarrer l'API FastAPI avec Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
