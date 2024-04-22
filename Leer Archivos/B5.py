import sys

if len(sys.argv) != 2:
    print("Error: Uso incorrecto del script. Debe proporcionar la ruta al archivo como argumento.")
    print("Uso: python B5.py archivo_diccionario")
    sys.exit(1)  

diccionario = sys.argv[1]

for letra in range(ord('a'), ord('z')+1):
    letra = chr(letra)
    with open(letra + ".txt", "w", encoding="utf-8") as archivo_letra:
        with open(diccionario, "r", encoding="utf-8") as archivo_diccionario:
            for palabra in archivo_diccionario:
                if palabra.startswith(letra):
                    archivo_letra.write(palabra)