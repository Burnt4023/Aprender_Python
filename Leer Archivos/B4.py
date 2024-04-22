import sys
import random


if len(sys.argv) != 4:
    print("Error: Uso incorrecto del script. Debe proporcionar la ruta al archivo como argumento.")
    print("Uso: python B4.py archivo_nombres archivo_apellidos archivo_salida")
    sys.exit(1)  

archivo_nombres = sys.argv[1]
archivo_apellidos = sys.argv[2]
archivo_salida = sys.argv[3]


nombres = []
with open(archivo_nombres, "r") as archivo__nombres: #Generar nombres
    for nombre in archivo__nombres:
        nombres.append(nombre.strip())

apellidos = []
with open(archivo_apellidos, "r") as archivo__apellidos: #Generar apellidos
    for apellido in archivo__apellidos:
        apellidos.append(apellido)
        
n = int(input("Número de nombres a generar: "))

personas = []
for i in range(n):
    personas.append(random.choice(nombres)+" "+random.choice(apellidos)) #Crea n apellidos aleatorios
    
with open(archivo_salida, "a") as archivo: #Los guarda en el archivo de salida
    for persona in personas:
        archivo.write(persona)