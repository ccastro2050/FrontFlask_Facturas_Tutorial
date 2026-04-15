"""
config.py — Configuración centralizada del frontend.

Este archivo guarda valores que se usan en VARIOS lugares del proyecto.
En vez de escribir "http://localhost:8000" en cada archivo, lo ponemos
aquí UNA SOLA VEZ. Si mañana la API cambia de puerto, solo modificamos
este archivo.

Analogía: es como la agenda de contactos de tu teléfono.
En vez de memorizar cada número, lo guardas una vez y lo usas siempre.
"""

# ─── URL base de la API backend ─────────────────────────────
# Esta es la dirección donde está corriendo la API FastAPI.
# "http://localhost:8000" significa:
#   - http://     → protocolo de comunicación web
#   - localhost   → tu propia computadora (127.0.0.1)
#   - :8000       → puerto donde escucha la API (uvicorn usa 8000 por defecto)
#
# IMPORTANTE: esta URL NO incluye /api/producto ni ninguna ruta.
# Solo es la "raíz" del servidor. Las rutas se agregan después
# en api_service.py cuando hacemos las peticiones.
#
# Si la API estuviera en otro servidor, cambiarías esto a:
#   API_BASE_URL = "http://192.168.1.100:8000"
# ─────────────────────────────────────────────────────────────
API_BASE_URL = "http://127.0.0.1:8000"

# ─── Clave secreta de Flask ─────────────────────────────────
# Flask necesita una clave secreta para:
#   1. Firmar las cookies de sesión (evitar que alguien las modifique)
#   2. Proteger los mensajes flash (los avisos verdes/rojos de éxito/error)
#
# ¿Qué es una cookie de sesión?
#   Es un pequeño archivo que el navegador guarda para "recordar"
#   información entre páginas (por ejemplo, mensajes de éxito).
#
# En producción, esta clave debe ser larga, aleatoria y SECRETA.
# En este tutorial usamos una clave simple para facilitar el aprendizaje.
# ─────────────────────────────────────────────────────────────
SECRET_KEY = "clave-secreta-flask-tutorial-2024"
