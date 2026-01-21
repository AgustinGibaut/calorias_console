import bcrypt
import getpass
from db import create_connection

def login_user():
    conn = create_connection()
    if not conn:
        return None

    cursor = conn.cursor()
    username = input("Nombre de usuario: ").strip()
    password = getpass.getpass("Contraseña: ").encode('utf-8')

    cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result and bcrypt.checkpw(password, result[0].encode('utf-8')):
        print(f"Bienvenido {username}! 🎉")
        return username
    else:
        print("Usuario o contraseña incorrectos ❌")
        return None
