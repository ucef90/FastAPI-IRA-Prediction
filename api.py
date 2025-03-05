from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

# Charger le modèle
model = joblib.load("LightGBM_best_model.pkl")

# Créer une instance FastAPI
app = FastAPI()


# Autoriser toutes les origines, méthodes et en-têtes (à adapter si besoin) pour eviter cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplacez "*" par ["http://localhost:8000"] pour plus de sécurité
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Définition de la route principale
@app.get("/")
def home():
    return {"message": "API de prédiction des admissions IRA"}

# Route pour effectuer une prédiction
@app.post("/predict/")
def predict(data: dict):
    try:
        # Convertir les données en DataFrame
        df = pd.DataFrame([data])
        
        # Faire la prédiction
        prediction = model.predict(df)
        
        return {"prediction_ira": int(prediction[0])}
    
    except Exception as e:
        return {"error": str(e)}

