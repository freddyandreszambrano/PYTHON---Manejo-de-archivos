from pathlib import Path

Fl_ruta_file = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V05.txt")

#comprobar si existe el archivo
Lb_existe = Fl_ruta_file.exists()

#validamos si exsite

if (Lb_existe):
    #si existe lo abrimos y trabajamos con el archivo
    with Fl_ruta_file.open(mode = "r+") as archivo_05:
        print("*** ingrese la palabra que desea buscar **")
        Lv_buscar = input()
        print("*** ingrese la palabra con la que desea reemplazarla ***")
        Lv_reemplazar = input()
        Lv_contenido = archivo_05.read().replace(Lv_buscar, Lv_reemplazar)
        archivo_05.seek(0)
        archivo_05.write(Lv_contenido)
        archivo_05.truncate()
        print("se ha modificado el archivo")


else:
    print("desea crear el archivo S/N")
    Lb_control = input()
    if (Lb_control  == "s" or Lv_control == "S"):
        with open("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V05.txt", "w") as file_05:
            print("ingrese el mensaje que desea guardar el archivo");
            Lb_respueta = input()
            file_05.write(Lb_respueta)
    elif(Lv_control == 'N' or Lv_control == "n"):
        print("El proceso a terminado, gracias.");
    else:
        print("Cod035 - Ruta especifica no existe")