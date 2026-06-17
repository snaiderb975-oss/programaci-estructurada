from graphviz import Digraph

# Crear diagrama
dot = Digraph("Cliente")
dot.attr(rankdir='TB')
dot.attr('node', fontname='Arial')

# Nodos
dot.node('A', 'Inicio', shape='oval')
dot.node('B', 'Llega a la clínica', shape='box')
dot.node('C', 'Solicita atención', shape='parallelogram')
dot.node('D', '¿Tiene cita?', shape='diamond')

dot.node('E', 'Espera turno', shape='box')
dot.node('F', 'Solicita cita', shape='box')

dot.node('G', 'Ingresa al consultorio', shape='box')
dot.node('H', 'Recibe atención', shape='box')
dot.node('I', 'Recibe receta', shape='parallelogram')
dot.node('J', 'Fin', shape='oval')

# Conexiones
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')

dot.edge('D', 'E', label='Sí')
dot.edge('D', 'F', label='No')

dot.edge('E', 'G')
dot.edge('F', 'G')

dot.edge('G', 'H')
dot.edge('H', 'I')
dot.edge('I', 'J')

# Guardar y mostrar
dot.render('diagrama_cliente', format='png', view=True, cleanup=True)

print("Diagrama del cliente creado correctamente.")