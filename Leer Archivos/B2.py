import sys
import regex


if len(sys.argv) != 2:
    print("Error: Uso incorrecto del script. Debe proporcionar la ruta al archivo como argumento.")
    print("Uso: python B2.py Ruta-al-Archivo")
    sys.exit(1)  

archivo = sys.argv[1]



with open(archivo, 'r') as file:
    alumnos = [] # Mapa que relaciona alumno y nota
    
    for linea in file:
        # Divide la línea en nombre, notas y convertir las notas a enteros
        datos = linea.strip().split()
        nombre = datos[0] + ' ' + datos[1]
        notas = [int(nota) for nota in datos[2:]]
        suma=0
        for nota in notas:
            suma=suma+nota
        media = suma/len(notas)
        alumnos.append((nombre, media))


alumnos_ordenados = sorted(alumnos, key=lambda x: x[1], reverse=True) # Ordena la lista de alumnos por su nota media de mayor a menor

print("Notas medias de los alumnos (de mayor a menor):")
for nombre, media in alumnos_ordenados:
    print(f"{nombre}: {media}")