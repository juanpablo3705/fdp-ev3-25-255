usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

while True:
    print("1. Iniciar sesión.")
    print("2. Registrar usuario.")
    print("3. Salir.")

    while True:
        try:
            opcion_menu1 = int(input("Ingrese una opción del menú: "))
            break
        except ValueError:
            print("Error. Escriba un número del 1 al 3.")

    if opcion_menu1 == 1:
        if (usuario1 == None) and (usuario2 == None) and (usuario3 == None):
            print("Es necesario registrar un usuario antes.")
            print("Para crear un usuario nuevo, seleccione la opción 2.")
        else:
            print("Ingrese su nombre de usuario y contraseña: ")
            intento_us = input("Usuario: ")
            intento_ct = input("Contraseña: ")

            if (intento_us == usuario1 and intento_ct == contrasena1) or (intento_us == usuario2 and intento_ct == contrasena2) or (intento_us == usuario3 and intento_ct == contrasena3):
                while True:
                    print("1. Realizar llamada.")
                    print("2. Enviar correo electrónico.")
                    print("3. Cerrar sesión.")

                    while True:
                        try:
                            opcion_menu2 = int(input("Ingrese una opción del menú: "))
                            break
                        except ValueError:
                            print("Error. Escriba un número del 1 al 3.")

                    if opcion_menu2 == 1:
                        celular = int(input("Ingrese el número celular: "))
                    elif opcion_menu2 == 2:
                        correo = int(input("Ingrese correo electrónico: "))
                        mensaje = input("Ingrese mensaje a enviar: ")
                    elif opcion_menu2 == 3:
                        print("Volviendo al menú principal...")

            else:
                if (intento_us == usuario1 or usuario2 or usuario3) and (intento_ct != contrasena1 or contrasena2 or contrasena3):
                    print("Contraseña incorrecta.")
                elif (intento_us != usuario1 or usuario2 or usuario3) and (intento_ct != contrasena1 or contrasena2 or contrasena3):
                    print("Nombre de usuario incorrecto.")
                else:
                    print("Nombre y usuario incorrectos.")

    if opcion_menu1 == 2:
        print("Ahora usted podrá registrar un usuario.")
        if usuario1 == None:
            usuario1 = input("Ingrese nuevo nombre de usuario: ")
            contrasena1 = input("Ingrese nueva contraseña: ")
        elif usuario1 != None and usuario2 == None:
            usuario2 = input("Ingrese nuevo nombre de usuario: ")
            contrasena2 = input("Ingrese nueva contraseña: ")
        elif usuario1 != None and usuario2 != None and usuario3 == None:
            usuario3 = input("Ingrese nuevo nombre de usuario: ")
            contrasena3 = input("Ingrese nueva contraseña: ")