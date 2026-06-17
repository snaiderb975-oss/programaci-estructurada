from graphviz import Digraph

# Crear diagrama
dot = Digraph("Doctor")
dot.attr(rankdir='TB')
dot.attr('node', fontname='Arial')

# Nodos
dot.node('A', 'Inicio', shape='oval')
dot.node('B', 'Recibe al paciente', shape='box')
dot.node('C', 'Escucha síntomas', shape='parallelogram')
dot.node('D', 'Realiza evaluación', shape='box')
dot.node('E', '¿Necesita exámenes?', shape='diamond')

dot.node('F', 'Solicita exámenes', shape='box')
dot.node('G', 'Diagnostica', shape='box')

dot.node('H', 'Prescribe tratamiento', shape='box')
dot.node('I', 'Entrega receta', shape='parallelogram')
dot.node('J', 'Fin', shape='oval')

# Conexiones
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')

dot.edge('E', 'F', label='Sí')
dot.edge('E', 'G', label='No')

dot.edge('F', 'H')
dot.edge('G', 'H')

dot.edge('H', 'I')
dot.edge('I', 'J')

# Guardar y mostrar
dot.render('diagrama_doctor', format='png', view=True, cleanup=True)

print("Diagrama del doctor creado correctamente.")