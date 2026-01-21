from db import create_connection
from datetime import date


def get_user_id(username):
    """Obtiene el ID del usuario a partir del nombre."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None


def add_food(username):
    user_id = get_user_id(username)
    if not user_id:
        print("Usuario no encontrado.")
        return

    food_name = input("Nombre de la comida: ").strip()
    calories = input("Cantidad de calorías: ").strip()
    
    if not calories.isdigit():
        print(" Ingresa un número válido para calorías.")
        return
    
    calories = int(calories)
    today = date.today()

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO food_log (user_id, food_name, calories, log_date) VALUES (%s, %s, %s, %s)",
        (user_id, food_name, calories, today)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f" {food_name} con {calories} calorías agregado para hoy.")

def show_calories(username):
    user_id = get_user_id(username)
    if not user_id:
        print("Usuario no encontrado.")
        return

    today = date.today()
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT food_name, calories FROM food_log WHERE user_id=%s AND log_date=%s",
        (user_id, today)
    )
    logs = cursor.fetchall()
    cursor.close()
    conn.close()

    if not logs:
        print("No hay alimentos registrados hoy.")
        return

    total_calories = sum(cal for _, cal in logs)
    print(f"\n--- Registro de calorías de hoy ({today}) ---")
    for food, cal in logs:
        print(f"{food}: {cal} cal")
    print(f"Total consumido hoy: {total_calories} cal\n")

def dashboard(username):
    while True:
        print(f"\n--- DASHBOARD de {username} ---")
        print("1. Agregar comida")
        print("2. Mostrar calorías consumidas hoy")
        print("3. Salir del dashboard")
        choice = input("Elige una opción: ").strip()

        if choice == '1':
            add_food(username)
        elif choice == '2':
            show_calories(username)
        elif choice == '3':
            break
        else:
            print("Opción inválida, intenta nuevamente.")