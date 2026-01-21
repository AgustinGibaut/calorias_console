import bcrypt
import getpass
from db import create_connection

def register_user():
    conn = create_connection()
    if not conn:
        return

    cursor = conn.cursor()
    username = input("Elige un nombre de usuario: ").strip()
    password = getpass.getpass("Elige una contraseña: ").encode('utf-8')

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
                    (username, hashed_password))
        conn.commit()
        print("Usuario registrado con éxito ")
    except Exception as e:
        print("Ese usuario ya existe o hubo un error:", e)
    finally:
        cursor.close()
        conn.close()
