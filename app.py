from fastapi import FastAPI
import joblib

app = FastAPI()

# Cargar el modelo que guardamos en train.py
model = joblib.load('modelo_maquina.pkl')

@app.get("/")
def home():
    return {"status": "MLOps API Running"}

@app.get("/predict")
def predict(temp: float):
    prediction = model.predict([[temp]])[0]
    result = "MANTENIMIENTO REQUERIDO" if prediction == 1 else "TODO OK"
    return {"temperatura": temp, "diagnostico": result}