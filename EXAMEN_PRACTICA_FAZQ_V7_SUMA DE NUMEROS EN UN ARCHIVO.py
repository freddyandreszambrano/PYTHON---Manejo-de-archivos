from pathlib import Path

Fl_ruta_file = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V07.txt")

# Comprobar si existe el archivo
Lb_existe = Fl_ruta_file.exists()

# Validamos si existe
if Lb_existe:
    # Si existe, lo abrimos y trabajamos con el archivo
    with Fl_ruta_file.open(mode="r") as archivo_06:
        Lv_contenido = archivo_06.read()
        Ln_sublist = Lv_contenido.split()
        print(Ln_sublist)
        Ln_suma = 0
        for num in Ln_sublist:
            try:
                Ln_num = int(num)
                Ln_suma += Ln_num
            except ValueError:
                print("Error en el archivo")
        print(f"La suma de los valores del archivo es {Ln_suma}")
else:
    print("¿Desea crear el archivo? (S/N)")
    Lb_control = input()
    if Lb_control.lower() == "s":
        with open("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V07.txt", "w") as file_05:
            print("Ingrese el mensaje que desea guardar en el archivo")
            Lb_respueta = input()
            file_05.write(Lb_respueta)
    elif Lb_control.lower() == "n":
        print("El proceso ha terminado, gracias.")
    else:
        print("Cod035 - Ruta específica no existe")
