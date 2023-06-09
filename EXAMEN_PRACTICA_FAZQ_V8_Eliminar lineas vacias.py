from pathlib import Path

#Eliminar líneas vacías: Escribe un programa que lea un archivo de texto y elimine todas las líneas vacías.

archivo_ruta = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V08.txt")

# Comprobar si existe el archivo
existe_archivo = archivo_ruta.exists()

# Validamos si existe
if existe_archivo:
    # Si existe, lo abrimos y trabajamos con el archivo
    with archivo_ruta.open(mode="r") as archivo:
        lineas = archivo.readlines()

    # Filtrar las líneas eliminando las líneas vacías
    lineas_filtradas = [linea for linea in lineas if linea.strip()]

    # Abrir el archivo en modo escritura
    with archivo_ruta.open(mode="w") as archivo:
        # Escribir las líneas no vacías en el archivo
        archivo.writelines(lineas_filtradas)

    print("Líneas vacías eliminadas en el archivo", archivo_ruta)
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
