from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route("/process")
def process_request():
    # Simula error transitorio (50% de probabilidad de fallo)
    if random.random() < 0.5:
        return jsonify({"error": "Servicio temporalmente no disponible"}), 503
    else:
        return jsonify({"message": "Procesado con éxito"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
