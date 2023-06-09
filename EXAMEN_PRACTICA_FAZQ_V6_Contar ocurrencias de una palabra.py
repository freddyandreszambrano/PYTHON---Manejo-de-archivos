from pathlib import Path

Fl_ruta_file = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V06.txt")

# Comprobar si existe el archivo
Lb_existe = Fl_ruta_file.exists()

# Validamos si existe
if Lb_existe:
    # Si existe, lo abrimos y trabajamos con el archivo
    with Fl_ruta_file.open(mode="r") as archivo_06:
        Lv_contenido = archivo_06.read()
        # Dividir una cadena de texto en una lista de subcadenas
        Lv_texto = Lv_contenido.split()
        # Conjunto para almacenar las palabras contadas
        palabras_contadas = set()
        for indice, palabra in enumerate(Lv_texto):
            if palabra in palabras_contadas:
                # Omitir la palabra si ya ha sido contada
                continue
            # Reiniciamos el contador para cada palabra
            lv_contador = 0
            for otra_palabra in Lv_texto:
                if palabra == otra_palabra:
                    lv_contador += 1
            # Agregar la palabra al conjunto de palabras contadas
            palabras_contadas.add(palabra)
            print(f"La palabra '{palabra}' se repite {lv_contador} veces")

else:
    print("¿Desea crear el archivo? (S/N)")
    Lb_control = input()
    if Lb_control.lower() == "s":
        with open("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V06.txt", "w") as file_05:
            print("Ingrese el mensaje que desea guardar en el archivo")
            Lb_respueta = input()
            file_05.write(Lb_respueta)
    elif Lb_control.lower() == "n":
        print("El proceso ha terminado, gracias.")
    else:
        print("Cod035 - Ruta específica no existe")
