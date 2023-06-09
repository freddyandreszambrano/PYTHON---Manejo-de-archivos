from pathlib import Path

archivo_ruta = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V09.txt")

# Comprobar si existe el archivo
existe_archivo = archivo_ruta.exists()

# Validamos si existe
if existe_archivo:
    # Si existe, lo abrimos y trabajamos con el archivo
    with archivo_ruta.open(mode="r") as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        palabras_distintas = set(palabras)
        cantidad_distintas = len(palabras_distintas)
        print(f"Se han identificado {cantidad_distintas} palabras distintas en el archivo.")
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
