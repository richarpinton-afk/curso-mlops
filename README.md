# 🚀 End-to-End MLOps Pipeline: Predicción Automática

Este proyecto demuestra la implementación de un ciclo de vida completo de Machine Learning (MLOps), enfocándose en la **automatización**, **reproducibilidad** y **despliegue profesional**.

## 🎯 Objetivo del Proyecto
Desarrollar una infraestructura que no solo entrene un modelo de IA, sino que garantice que cada cambio en el código sea probado y empaquetado automáticamente mediante contenedores.

## 🛠️ Stack Tecnológico
*   **Lenguaje:** Python 3.12
*   **Gestor de Dependencias:** [uv](https://astral.sh/uv/) (Alto rendimiento)
*   **Automatización (CI/CD):** GitHub Actions
*   **Contenerización:** Docker
*   **Librerías de ML:** Scikit-learn, Pandas

## 🤖 Automatización con GitHub Actions
El proyecto cuenta con un "Robot" de integración continua configurado en `.github/workflows/main.yml` que realiza las siguientes tareas en cada envío de código (push):
1.  **Entorno:** Levanta un servidor virtual con Linux.
2.  **Instalación:** Configura Python y las dependencias exactas usando archivos de bloqueo (`uv.lock`).
3.  **Entrenamiento:** Ejecuta `train.py` para generar el modelo actualizado.
4.  **Validación Docker:** Verifica que el `Dockerfile` sea capaz de construir una imagen funcional.

## 📦 Cómo ejecutar este proyecto localmente

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/curso-mlops.git](https://github.com/tu-usuario/curso-mlops.git)