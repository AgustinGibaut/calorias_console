import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Cargar las variables del .env
load_dotenv()

def create_connection():
    """
    Crea y devuelve la conexión a la base de datos usando variables del .env.
    Retorna None si ocurre un error.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("✅ Conexión a MySQL exitosa")
            return connection
    except Error as e:
        print(f"❌ Error conectando a MySQL: {e}")
        return None
