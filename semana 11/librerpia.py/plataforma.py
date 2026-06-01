import libreríalogin
class plataforma:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f"Plataforma: {self.nombre}")

    def alerta(self):
        libreríalogin.alerta()

    def redirigir(self):
        libreríalogin.redirigir()