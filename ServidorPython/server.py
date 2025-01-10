from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para servir un video específico
@app.route('/video/<filename>', methods=['GET'])
def get_video(filename):
    try:
        # Envía el archivo desde la carpeta "videos"
        return send_file(f'videos/{filename}', as_attachment=False)
    except FileNotFoundError:
        return "Archivo no encontrado", 404

if __name__ == '__main__':
    # Ejecuta el servidor en todas las interfaces de red
    app.run(host='0.0.0.0', port=5000)
