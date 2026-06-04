import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from datetime import datetime

# Credenciales
USUARIO = "admin"
CONTRASENA = "1234"

# ----------------------------
# Ventana principal
# ----------------------------
root = tk.Tk()
root.title("Login")
root.geometry("350x450") # Aumenté el alto a 450 para que quepa la imagen

# --- AGREGAR IMAGEN AL LOGIN ---
try:
    # Puedes cambiar "login_logo.jpg" por el nombre de tu archivo (ej. "tokems.jpg")
    imagen_login = Image.open("tokems.jpg") 
    imagen_login = imagen_login.resize((120, 120)) # Tamaño adecuado para el login
    foto_login = ImageTk.PhotoImage(imagen_login)

    lbl_img_login = tk.Label(root, image=foto_login)
    lbl_img_login.image = foto_login # Mantener referencia
    lbl_img_login.pack(pady=15)
except Exception as e:
    # Si la imagen no existe, muestra un texto amigable o simplemente no pone nada
    tk.Label(root, text="[ Logo no encontrado ]", fg="gray").pack(pady=10)
# -------------------------------

tk.Label(root, text="Usuario").pack(pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.pack()

tk.Label(root, text="Contraseña").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()


def actualizar_token(label):
    token = random.randint(100000, 999999)
    label.config(text=f"Token: {token}")
    # Guardamos la referencia del 'after' en una variable por si la necesitas cancelar luego
    label.after_id = label.after(5000, actualizar_token, label)  # cambia cada 5 segundos


def abrir_sistema():
    # Oculta la ventana de login al entrar al sistema (Opcional, pero recomendado)
    root.withdraw() 

    ventana = tk.Toplevel()
    ventana.title("Sistema")
    ventana.geometry("500x500")
    
    # Si cierran la ventana del sistema, se cierra toda la aplicación
    ventana.protocol("WM_DELETE_WINDOW", root.destroy)

    hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    tk.Label(
        ventana,
        text=f"Hora de ingreso: {hora}",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    # Imagen del Sistema
    try:
        imagen = Image.open("tokems.jpg")
        imagen = imagen.resize((200, 200))
        foto = ImageTk.PhotoImage(imagen)

        lbl_imagen = tk.Label(ventana, image=foto)
        lbl_imagen.image = foto
        lbl_imagen.pack(pady=10)

    except:
        tk.Label(
            ventana,
            text="No se encontró tokems.jpg",
            fg="red"
        ).pack()

    lbl_token = tk.Label(
        ventana,
        text="Token:",
        font=("Arial", 16)
    )
    lbl_token.pack(pady=20)

    actualizar_token(lbl_token)


def login():
    usuario = entry_usuario.get()
    password = entry_password.get()

    if usuario == USUARIO and password == CONTRASENA:
        abrir_sistema()
    else:
        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )


tk.Button(
    root,
    text="Ingresar",
    command=login,
    width=20
).pack(pady=20)

root.mainloop()