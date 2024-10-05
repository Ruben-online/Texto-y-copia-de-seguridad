from text import *
from backup import *

while True:
    print("Bienvenido")
    print("1. Ingresar texto ")
    print("2. Dividir el texto ")
    print("3. Crear copia de seguridad ")
    print("4. Salir")

    menu = int(input("\nIngrese una opción: "))

    if menu == 1:
        save_text()
    elif menu == 2:
        paginate_text()
    elif menu == 3:
        create_backup()
    elif menu == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo!")