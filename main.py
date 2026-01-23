import os
from register import register_user
from login import login_user
from dashboard import dashboard

def clear_console():
    os.system('clear')  


def print_title(text):
    print(f"\033[1;34m{text}\033[0m")  

def print_success(text):
    print(f"\033[1;32m{text}\033[0m")  

def print_error(text):
    print(f"\033[1;31m{text}\033[0m") 

def main():
    while True:
        clear_console()
        print_title("\n=== BIENVENIDO AL CALCULADOR DE CALORÍAS ===\n")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir\n")

        choice = input("Elige una opción: ").strip()

        if choice == '1':
            clear_console()
            print_title("--- Registro de Usuario ---\n")
            register_user()
            input("\nPresiona Enter para volver al menú...")
        elif choice == '2':
            clear_console()
            print_title("--- Inicio de Sesión ---\n")
            user = login_user()
            if user:
                input("\nPresiona Enter para entrar al dashboard...")
                dashboard(user)
            else:
                input("\nPresiona Enter para volver al menú...")
        elif choice == '3':
            print_success("\n¡Gracias por usar el calculador de calorías! \n")
            break
        else:
            print_error("\nOpción inválida, intenta nuevamente.")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()