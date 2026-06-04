import secrets

# Función limpiar (ejemplo)
def limpiar():
    print("\n" * 50)

# Función pausa (ejemplo)
def pausa():
    input("\nPresiona Enter para continuar...")

# Función de autenticación
def autenticar_usuario():
    limpiar()
    print("===== LOGIN =====")

    username = input("Usuario: ")
    password = input("Contraseña: ")

    if username == "rapi" and password == "password":
        print("¡Login exitoso!")
        pausa()
        return True
    else:
        print("Contraseña incorrecta.")
        pausa()
        return False

# Función de token
def token_misar():
    while True:
        limpiar()
        print("===== TOKEN MISAR =====")

        token_generado = secrets.token_hex(8)

        print("Tu token es:", token_generado)

        token_ingresado = input("Ingresa el token: ")

        if token_ingresado == token_generado:
            print("Token válido. Acceso concedido.")
            pausa()
            return True
        else:
            print("Contraseña incorrecta.")
            pausa()

# Función de alerta
def alerta():
    limpiar()
    print("===== ALERTA =====")
    print("¡Alerta! Se ha detectado una actividad sospechosa.")
    pausa()

# Función de redirección
def redirigir():
    limpiar()
    print("===== REDIRIGIR =====")
    print("Redirigiendo a la página de inicio...")
    pausa()

# Programa principal
if autenticar_usuario():
    redirigir()

    if token_misar():
        limpiar()
        print("Bienvenido al sistema.")
        pausa()
else:
    alerta()