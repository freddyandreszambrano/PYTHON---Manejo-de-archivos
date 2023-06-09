# Ordenar palabras alfabéticamente: Escribe un programa que lea un archivo de texto que contiene palabras y las ordene alfabéticamente.


from pathlib import Path

archivo_ruta = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V10.txt")

# Comprobar si existe el archivo
existe_archivo = archivo_ruta.exists()

# Validamos si existe
if existe_archivo:
    # Si existe, lo abrimos y trabajamos con el archivo
    with archivo_ruta.open(mode="r+") as archivo:
        contenido = archivo.read()
        sub_lista = contenido.split()
        texto_ordenado = sorted(sub_lista)
        archivo.seek(0)  # Regresamos al inicio del archivo
        archivo.truncate()  # Limpiamos el contenido del archivo
        archivo.write(" ".join(texto_ordenado))  # Escribimos el texto ordenado en el archivo
        print(texto_ordenado)
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
