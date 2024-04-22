import sys

if len(sys.argv) != 3:
    print("Error: Uso incorrecto del script. Debe proporcionar la ruta al archivo como argumento.")
    print("Uso: python B3.py Ruta-al-Archivo-a-Leer Archivo-Ordenado")
    sys.exit(1)  

archivo_entrada = sys.argv[1]
archivo_salida = sys.argv[2]

lineas = []

with open(archivo_entrada, "r") as archivo:
    for linea in archivo:
        lineas.append(linea)
    lineas.sort()
    

with open(archivo_salida, "w") as archivo2:
    for linea in lineas:
        archivo2.write(linea)