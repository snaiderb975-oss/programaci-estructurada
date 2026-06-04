import tkinter as tk

ventana = tk.Tk()

# ancho x alto
ventana.geometry("500x800")

ventana.mainloop()

import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("500x800")
ventana.config(bg="#f0f0f0")

# Título
titulo = tk.Label(
    ventana,
    text="Iniciar Sesión",
    font=("Arial", 24, "bold"),
    bg="#f0f0f0"
)
titulo.pack(pady=40)

# Usuario
label_usuario = tk.Label(
    ventana,
    text="Usuario",
    font=("Arial", 14),
    bg="#f0f0f0"
)
label_usuario.pack()

entrada_usuario = tk.Entry(
    ventana,
    font=("Arial", 14),
    width=25
)
entrada_usuario.pack(pady=10)

# Contraseña
label_password = tk.Label(
    ventana,
    text="Contraseña",
    font=("Arial", 14),
    bg="#64776e"
)
label_password.pack()

entrada_password = tk.Entry(
    ventana,
    font=("Arial", 14),
    width=25,
    show="*"
)
entrada_password.pack(pady=10)

# Función login
def login():
    usuario = entrada_usuario.get()
    password = entrada_password.get()

    if usuario == "rapi" and password == "1234":
        resultado.config(text="Login correcto", fg="green")
    else:
        resultado.config(text="Usuario o contraseña incorrectos", fg="red")

# Botón
boton_login = tk.Button(
    ventana,
    text="Ingresar",
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=login
)
boton_login.pack(pady=30)

# Resultado
resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 12),
    bg="#f5eded"
)
resultado.pack()

# Ejecutar ventana
ventana.mainloop()


# Cargar imagen
imagen = Image.open("tokems.jpg")