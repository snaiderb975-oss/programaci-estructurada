import libreríalogin
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")

    def iniciar_sesion(self):
        if libreríalogin.autenticar_usuario():
            print("Bienvenido, " + self.nombre + "!")
        else:
            print("No se pudo iniciar sesión.")

    def verificar_token(self):
        if libreríalogin.token_misar():
            print("Token verificado correctamente.")
        else:
            print("Error al verificar el token.")