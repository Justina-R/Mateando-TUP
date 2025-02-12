from app import crear_app
import os

app = crear_app()

if __name__ == "__main__":
    # Obtén el puerto desde la variable de entorno o usa el puerto 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)