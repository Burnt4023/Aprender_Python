import sys


if len(sys.argv) != 2:
    print("Error: Uso incorrecto del script. Debe proporcionar la ruta al archivo como argumento.")
    print("Uso: python B1.py Ruta-al-Archivo")
    sys.exit(1)  

archivo = sys.argv[1]


maximo = float("-inf")  
minimo = float("inf")   

with open(archivo, "r") as f:
    for linea in f:
        numero = int(linea)
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero


print("El mayor es", maximo, "y el menor es", minimo)