from flask import Flask, request, jsonify, redirect, url_for
from database import get_db_connection  # Importa la función de conexión

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)  # Devuelve datos en formato JSON

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()  # Obtiene los datos en formato JSON
    username = data.get('username')
    name = data.get('name')
    password = data.get('password')
    
    if username and name and password:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)",
            (username, name, password)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "User added successfully"}), 201  # Devuelve una respuesta en formato JSON
    return jsonify({"error": "Missing data"}), 400  # Devuelve un error en formato JSON

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "User deleted successfully"})  # Devuelve una respuesta en formato JSON

# Ruta para editar usuarios de la bdd
@app.route('/user/<int:id>', methods=['PUT'])
def edit_user(id):
    data = request.get_json()
    username = data.get('username')
    name = data.get('name')
    password = data.get('password')

    if username and name and password:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE users SET username = %s, name = %s, password = %s WHERE id = %s",
            (username, name, password, id)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "Missing data"}), 400

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return jsonify(user)
if __name__ == '__main__':
    app.run(port=5000, debug=True)
