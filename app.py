"""
app.py - Punto de entrada de la aplicacion Flask.

Adaptado para la API generica FastAPI (sin JWT, sin roles/rutas dinamicos).
La autenticacion verifica solo sesion activa (email + contrasena via BCrypt).
"""

from flask import Flask
from config import SECRET_KEY

# Crear la aplicacion Flask
app = Flask(__name__)

# ─── Configurar middleware de autenticacion ────────────────────
# El middleware se registra ANTES de los blueprints para que
# intercepte todas las peticiones y verifique sesion activa.
from middleware.auth_middleware import crear_middleware
app.secret_key = SECRET_KEY
crear_middleware(app)

# ─── Registrar Blueprints ─────────────────────────────────────
from routes.auth import bp as auth_bp
from routes.home import home_bp
from routes.producto import bp as producto_bp
from routes.usuario import bp as usuario_bp
from routes.persona import bp as persona_bp
from routes.cliente import bp as cliente_bp
from routes.empresa import bp as empresa_bp
from routes.vendedor import bp as vendedor_bp
from routes.rol import bp as rol_bp
from routes.ruta import bp as ruta_bp
from routes.factura import bp as factura_bp

app.register_blueprint(auth_bp)       # /login, /logout, /cambiar-contrasena
app.register_blueprint(home_bp)       # /
app.register_blueprint(producto_bp)   # /producto
app.register_blueprint(usuario_bp)    # /usuario
app.register_blueprint(persona_bp)    # /persona
app.register_blueprint(cliente_bp)    # /cliente
app.register_blueprint(empresa_bp)    # /empresa
app.register_blueprint(vendedor_bp)   # /vendedor
app.register_blueprint(rol_bp)        # /rol
app.register_blueprint(ruta_bp)       # /ruta
app.register_blueprint(factura_bp)    # /factura

if __name__ == '__main__':
    from waitress import serve
    print(" * Frontend Flask corriendo en: http://127.0.0.1:5300")
    print(" * Servidor: Waitress (multi-hilo)")
    print(" * Presiona Ctrl+C para detener")
    serve(app, host="127.0.0.1", port=5300, threads=4)
