#funciones de autentificacion
def autenticar_usuario():
    limpiar()
    print("===== LOGIN =====")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    # Aquí puedes agregar lógica de autenticación real
    if username == "admin" and password == "password":
        print("¡Login exitoso!")
        pausa()
        return True
    else:
        print("Credenciales incorrectas.")
        pausa()
        return False
#funcion de tokenmisar
def token_misar():
    limpiar()
    print("===== TOKEN MISAR =====")
    token = input("Ingresa tu token: ")

    # Aquí puedes agregar lógica de validación de token real
    if token == "misar123":
        print("Token válido. Acceso concedido.")
        pausa()
        return True
    else:
        print("Token inválido. Acceso denegado.")
        pausa()
        return False
    
#funcion de alerta
def alerta():
    limpiar()
    print("===== ALERTA =====")
    print("¡Alerta! Se ha detectado una actividad sospechosa.")
    pausa()

#funcion de redirigir
def redirigir():
    limpiar()
    print("===== REDIRIGIR =====")
    print("Redirigiendo a la página de inicio...")
    pausa()