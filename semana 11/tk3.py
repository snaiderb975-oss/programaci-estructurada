import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from datetime import datetime


# Credenciales
USUARIO = "admin"
CONTRASENA = "1234"


# ----------------------------
# Ventana Login
# ----------------------------

root = tk.Tk()
root.title("Login")
root.geometry("350x450")


# Imagen login
try:
    imagen_login = Image.open("tokems.jpg")
    imagen_login = imagen_login.resize((120,120))
    foto_login = ImageTk.PhotoImage(imagen_login)

    lbl_img_login = tk.Label(root,image=foto_login)
    lbl_img_login.image = foto_login
    lbl_img_login.pack(pady=15)

except:
    tk.Label(
        root,
        text="[ Logo no encontrado ]"
    ).pack()



tk.Label(root,text="Usuario").pack(pady=5)

entry_usuario = tk.Entry(root)
entry_usuario.pack()


tk.Label(root,text="Contraseña").pack(pady=5)

entry_password = tk.Entry(
    root,
    show="*"
)
entry_password.pack()



# ----------------------------
# Token
# ----------------------------

def actualizar_token(label):

    token=random.randint(100000,999999)

    label.config(
        text=f"Token: {token}"
    )

    label.after(
        5000,
        actualizar_token,
        label
    )



# ----------------------------
# Ventanas del menú
# ----------------------------

def ventana_archivo():

    archivo=tk.Toplevel()

    archivo.title("Archivo")
    archivo.geometry("300x250")
    archivo.configure(bg="#E3F2FD")


    tk.Label(
        archivo,
        text="Menú Archivo",
        font=("Arial",16,"bold"),
        bg="#E3F2FD",
        fg="#1565C0"
    ).pack(pady=20)


    tk.Button(
        archivo,
        text="Nuevo",
        width=20,
        command=lambda:
        messagebox.showinfo(
            "Archivo",
            "Nuevo archivo creado"
        )
    ).pack(pady=5)


    tk.Button(
        archivo,
        text="Abrir",
        width=20,
        command=lambda:
        messagebox.showinfo(
            "Archivo",
            "Archivo abierto"
        )
    ).pack(pady=5)


    tk.Button(
        archivo,
        text="Cerrar",
        width=20,
        command=archivo.destroy
    ).pack(pady=5)



def ventana_editar():

    editar=tk.Toplevel()

    editar.title("Editar")
    editar.geometry("300x250")
    editar.configure(bg="#FFF3E0")


    tk.Label(
        editar,
        text="Menú Editar",
        font=("Arial",16,"bold"),
        bg="#FFF3E0",
        fg="#E65100"
    ).pack(pady=20)


    tk.Button(
        editar,
        text="Copiar",
        width=20
    ).pack(pady=5)


    tk.Button(
        editar,
        text="Pegar",
        width=20
    ).pack(pady=5)


    tk.Button(
        editar,
        text="Cerrar",
        width=20,
        command=editar.destroy
    ).pack(pady=5)



def ventana_ayuda():

    ayuda=tk.Toplevel()

    ayuda.title("Ayuda")
    ayuda.geometry("300x250")
    ayuda.configure(bg="#E8F5E9")


    tk.Label(
        ayuda,
        text="Ayuda del Sistema",
        font=("Arial",16,"bold"),
        bg="#E8F5E9",
        fg="green"
    ).pack(pady=20)


    tk.Label(
        ayuda,
        text="Sistema de Login\nVersión 1.0\nProyecto educativo",
        bg="#E8F5E9",
        font=("Arial",12)
    ).pack()



    tk.Button(
        ayuda,
        text="Cerrar",
        width=20,
        command=ayuda.destroy
    ).pack(pady=20)



# ----------------------------
# Ventana bienvenida
# ----------------------------

def ventana_bienvenida():

    bienvenida=tk.Toplevel()

    bienvenida.title("Bienvenida")
    bienvenida.geometry("400x300")
    bienvenida.configure(bg="#E3F2FD")


    tk.Label(
        bienvenida,
        text="Bienvenido al Sistema",
        font=("Arial",18,"bold"),
        bg="#E3F2FD",
        fg="#1565C0"
    ).pack(pady=30)


    tk.Label(
        bienvenida,
        text=f"Usuario: {USUARIO}",
        font=("Arial",12),
        bg="#E3F2FD"
    ).pack()


    tk.Button(
        bienvenida,
        text="Ingresar al Menú Principal",
        width=25,
        bg="#1565C0",
        fg="white",
        command=lambda:[
            bienvenida.destroy(),
            abrir_sistema()
        ]
    ).pack(pady=40)



# ----------------------------
# Sistema principal
# ----------------------------

def abrir_sistema():

    ventana=tk.Toplevel()

    ventana.title("Sistema")

    ventana.geometry("500x500")


    # Barra menú

    barra_menu=tk.Menu(ventana)


    barra_menu.add_command(
        label="Archivo",
        command=ventana_archivo
    )


    barra_menu.add_command(
        label="Editar",
        command=ventana_editar
    )


    barra_menu.add_command(
        label="Ayuda",
        command=ventana_ayuda
    )


    ventana.config(
        menu=barra_menu
    )


    hora=datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )


    tk.Label(
        ventana,
        text=f"Hora de ingreso: {hora}",
        font=("Arial",12,"bold")
    ).pack(pady=10)



    try:

        imagen=Image.open("tokems.jpg")

        imagen=imagen.resize(
            (200,200)
        )

        foto=ImageTk.PhotoImage(imagen)


        lbl_imagen=tk.Label(
            ventana,
            image=foto
        )

        lbl_imagen.image=foto

        lbl_imagen.pack()



    except:

        tk.Label(
            ventana,
            text="No se encontró imagen",
            fg="red"
        ).pack()



    lbl_token=tk.Label(
        ventana,
        text="Token:",
        font=("Arial",16)
    )

    lbl_token.pack(pady=20)


    actualizar_token(lbl_token)



    tk.Button(
        ventana,
        text="Actualizar Token",
        command=lambda:
        actualizar_token(lbl_token)
    ).pack()



# ----------------------------
# Login
# ----------------------------

def login():

    usuario=entry_usuario.get()

    password=entry_password.get()


    if usuario==USUARIO and password==CONTRASENA:

        root.withdraw()

        ventana_bienvenida()

    else:

        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )



tk.Button(
    root,
    text="Ingresar",
    width=20,
    command=login
).pack(pady=20)



root.mainloop()