# el programa parte sin usuarios creados:
usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

# inicio ciclo grande del menú
while True:
    print("----- Menú -----")
    print("1. Iniciar sesión.")
    print("2. Registrar usuario.")
    print("3. Salir.")

    # verificación que el usuario ingrese sólo números
    try:
        opcion_menu1 = int(input("Ingrese una opción del menú: "))
    except ValueError:
        print("Error. Escriba un número del 1 al 3.")
        continue

    # inicio opción 1: iniciar sesión
    if opcion_menu1 == 1:

        # si no hay usuarios pre-existentes, de vuelta al menú:
        if (usuario1 == None) and (usuario2 == None) and (usuario3 == None):
            print("Error. Es necesario registrar un usuario antes.")
            print("Para crear un usuario nuevo, seleccione la opción 2.")
        # si se detectan usuarios pre-existentes, login:    
        else:
            print("Ingrese su nombre de usuario y contraseña: ")
            intento_us = input("Usuario: ")
            intento_ct = input("Contraseña: ")
            
            # si coincide el login de alguno de los 3 usuarios, pasa al siguiente menú:
            if (intento_us == usuario1 and intento_ct == contrasena1) or (intento_us == usuario2 and intento_ct == contrasena2) or (intento_us == usuario3 and intento_ct == contrasena3):
                while True:
                    print("----- Otro Menú -----")
                    print("1. Realizar llamada.")
                    print("2. Enviar correo electrónico.")
                    print("3. Cerrar sesión.")

                    # verificación que el usuario ingrese sólo números:
                    while True:
                        try:
                            opcion_menu2 = int(input("Ingrese una opción del menú: "))
                            break
                        except ValueError:
                            print("Error. Escriba un número del 1 al 3.")
                    
                    # proceso del segundo menú:
                    if opcion_menu2 == 1:
                        celular = (input("Ingrese el número celular (9 dígitos, comience con 9): "))
                        if len(celular) == 9 and celular.startswith("9") and celular.isdigit():
                            print("Aló... ALÓ!?...")
                        else:
                            print("Error. El número debe tener 9 dígitos y comenzar con 9")
                    elif opcion_menu2 == 2:
                        correo = (input("Ingrese correo electrónico: "))
                        recorrido = False
                        for caracter in correo:
                            if caracter == "@":
                                recorrido = True
                        if recorrido:
                            mensaje = input("Ingrese mensaje del correo: ")
                            print(f"Correo enviado a {correo}. Mensaje: '{mensaje}'.")
                        else:
                            print("Error. El correo debe incluir el caracter '@'.")
                    elif opcion_menu2 == 3:
                        print("Volviendo al menú principal...")
                        break
                    else:
                        print("Error. Ingrese una opción del 1 al 3.")

            # si no coincide el login para alguno de los 3 usuarios, errores:
            else:
                if (intento_us == usuario1 or usuario2 or usuario3) and (intento_ct != contrasena1 or contrasena2 or contrasena3):
                    print("Contraseña incorrecta.")
                elif intento_us != usuario1 or usuario2 or usuario3:
                    print("Nombre de usuario incorrecto.")
                else:
                    print("Nombre y usuario incorrectos.")
    
    # inicio opción 2:
    elif opcion_menu1 == 2:
        if usuario1 != None and usuario2 != None and usuario3 != None:
            print("Error. No se pueden registrar más usuarios. Límite de 3 usuarios alcanzado.")
        else:
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

    # inicio salida opción 3:
    elif opcion_menu1 == 3:
        print("Cerrando sesión...")
        break
    
    # verificación que el usuario ingrese solo del 1 al 3 en primer menú:
    else:
        print("Error. Ingrese una opción válida para el menú (1-3)")