import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib  # Sirve para guardar el modelo

# 1. Datos de ejemplo (Simulando un sensor de temperatura de una máquina)
# X: Temperatura, y: ¿Necesita mantenimiento? (1=Sí, 0=No)
data = {
    'temp': [20, 25, 30, 80, 85, 90, 95, 100],
    'fail': [0, 0, 0, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# 2. Entrenar el modelo
model = LogisticRegression()
model.fit(df[['temp']], df['fail'])

# 3. GUARDAR EL MODELO (Paso clave en MLOps)
# Esto crea un archivo físico con el "cerebro" del modelo
joblib.dump(model, 'modelo_maquina.pkl')

print("✅ Modelo entrenado y guardado como 'modelo_maquina.pkl'")