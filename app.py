from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para recibir datos desde Azure
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json  # Recibir datos JSON
    # Realizar acciones con los datos recibidos (por ejemplo, controlar la Raspberry Pi)
    print("Datos recibidos desde Azure:", data)
    return jsonify({"message": "Datos recibidos correctamente"})

if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo debug
