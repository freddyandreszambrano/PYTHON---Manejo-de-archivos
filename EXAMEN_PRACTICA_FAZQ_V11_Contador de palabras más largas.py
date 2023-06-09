# Contador de palabras más largas: Escribe un programa que lea un archivo de texto y cuente la cantidad de palabras más largas que un número dado de caracteres.


from pathlib import Path

archivo_ruta = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V11.txt")

# Comprobar si existe el archivo
existe_archivo = archivo_ruta.exists()

# Validamos si existe
if existe_archivo:
    # Si existe, lo abrimos y trabajamos con el archivo
    with archivo_ruta.open(mode="r") as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        longitud_minima = int(input("Ingrese el número mínimo de caracteres: "))
        contador = 0
        for palabra in palabras:
            if len(palabra) > longitud_minima:
                contador += 1

        print(f"La cantidad de palabras más largas que {longitud_minima} caracteres es: {contador}")
else:
    print("¿Desea crear el archivo? (S/N)")
    respuesta = input()
    if respuesta.lower() == "s":
        with archivo_ruta.open(mode="w") as archivo:
            print("Ingrese el mensaje que desea guardar en el archivo")
            respuesta = input()
            archivo.write(respuesta)
    elif respuesta.lower() == "n":
        print("El proceso ha terminado, gracias.")
    else:
        print("Ruta específica no existe")
