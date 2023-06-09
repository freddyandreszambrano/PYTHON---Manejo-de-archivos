
from pathlib import Path

#Contar líneas en un archivo: Escribe un programa que cuente la cantidad de líneas en un archivo de texto.

Fl_ruta_file = (Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V03.txt"));


#comprobar si exite el archivo

Lb_existe = Fl_ruta_file.exists()

if(Lb_existe):
    #si existe lo abrimos y ejecutamos el ejercicio
    with Fl_ruta_file.open(mode = "r") as archivo:
        Ln_total_lines = sum(1 for line in archivo)

    print(f"El total de lineas del archivo es {Ln_total_lines}")
else:
    #preguntamos si desea crearlo
    print("desea crear el archivo S/N")
    Lv_control = input()
    if (Lv_control == "s" or Lv_control =="S"):
        with open("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_V03.txt", "w") as file_01:
            print("ingrese el mensaje que desea usar")
            Lv_mensaje = input();
            Lv_mensaje += "\n"
            print("***ingrese otro mensaje***")
            Lv_mensaje += input();
            file_01.write(Lv_mensaje);
    elif(Lv_control == 'N' or Lv_control == "n"):
        print("El proceso a terminado, gracias.");
    else:
        print("Cod035 - Ruta especifica no existe")
















