import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import logging
from pathlib import Path

# Configuración de Logging para rastro profesional
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def train():
    # 1. Datos de ejemplo
    logger.info("Cargando datos de entrenamiento...")
    data = {
        'temp': [20, 25, 30, 80, 85, 90, 95, 100],
        'fail': [0, 0, 0, 1, 1, 1, 1, 1]
    }
    df = pd.DataFrame(data)

    # 2. Entrenar el modelo
    logger.info("Iniciando entrenamiento de Regresión Logística...")
    model = LogisticRegression()
    model.fit(df[['temp']], df['fail'])

    # 3. Evaluación (Vital para MLOps)
    predictions = model.predict(df[['temp']])
    acc = accuracy_score(df['fail'], predictions)
    logger.info(f"Modelo entrenado con una precisión de: {acc * 100}%")

    # 4. Guardado seguro usando Pathlib
    model_path = Path('modelo_maquina.pkl')
    joblib.dump(model, model_path)
    logger.info(f"✅ 'Cerebro' del modelo exportado exitosamente a: {model_path}")

if __name__ == "__main__":
    train()