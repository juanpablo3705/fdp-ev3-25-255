print("¡Bienvenido al software de registro de usuarios!")

usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

while True:
    # primer ingreso de opcion menu 1:
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if opcion > 0:
                break
            else:
                print("Error. El valor debe ser mayor a cero.")
        except ValueError:
            print("Error. El valor debe ser numérico, no letras.")
    # opcion 1 iniciar sesion:
    if (usuario1 == None) and (usuario2 == None) and (usuario3 == None):
        print("Es necesario registrar un usuario antes. Presiones opción 2.")
        continue    
    else:        
        while True:
            print("1. Realizar llamada")
            print("2. Enviar correo electrónico")
            print("3. Cerrar sesión")
            while True:
                try:
                    opcion_2 = int(input("Seleccione una opción: "))
                    if (opcion_2 > 0) and (opcion_2 < 4):
                        break
                    else:
                        print("Error. Debe ingresar un valor entre 1 y 3.")
                except ValueError:
                    print("Error. Debe ingresar sólo numeros enteros, no letras.")
                match opcion_2:
                    case 1:
                        while True:
                            try:
                                celular = int(input("Ingrese el número celular: "))
                                if celular.startswith(9) and len(celular) == 9:
                                    print("Llamando...")
                                    print("¡Llamada exitosa!")
                                    break
                                else:
                                    print("Error. El celular debe comenzar con 9 y tener 9 dígitos.")
                            except ValueError:
                                print("Error. El celular debe contener sólo dígitos, no letras.")
                    case 2:
                        while True:
                            correo = input("Ingrese la dirección de correo electrónico: ")
                            if "@" in correo:
                                mensaje = input("Escriba su mensaje:")
                                print(f"¡Mensaje enviado! Su mensaje fue: '{mensaje}'.")
                                break
                            else:
                                print("Error. La dirección de correo debe contener un @.")
                    case 3:
                        print("Cerrando sesión...")
                        print("Volviendo al menú principal...")
                        break
                
