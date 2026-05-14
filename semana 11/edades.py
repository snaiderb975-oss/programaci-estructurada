from datetime import datetime

# Pedir año de nacimiento
nacimiento = int(input("Ingrese su año de nacimiento: "))

# Obtener año actual
actual = datetime.now().year

# Calcular edad
edad = actual - nacimiento

# Mostrar resultado
print("Tu edad es:", edad, "años")