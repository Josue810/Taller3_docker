import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=" ", #nombre de usuario de mysql
            password=" ", #contraseña de mysql
            database="users" #nombre de la base de datos users
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
