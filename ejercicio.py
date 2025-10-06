class Lista:
    def __init__(self):
        self.lista = []

# Leer el contenido completo del archivo (opcional, si necesitas mostrarlo después)
with open('lista/listas.txt', 'r', encoding='utf-8') as file:
    lista_contenido = file.read()

# Leer los nombres línea por línea, quitando saltos de línea
with open('lista/listas.txt', 'r', encoding='utf-8') as file:
    nombres = [nombre.strip() for nombre in file.readlines()]

for nombre in nombres:
    print("-", nombre)

nuevo_nombre=input("Ingresa un elemento a la lista:")

    # Agregar el nuevo nombre al archivo
with open('lista/listas.txt', 'a', encoding='utf-8') as file:
    file.write(nuevo_nombre)
