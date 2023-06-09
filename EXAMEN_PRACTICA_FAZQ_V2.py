

from pathlib import Path

#crear un archivo especificando la ruta existente
Fl_ruta_file = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23.txt")


print("********** Contar palabras en un archivo **************")

#Contar palabras en un archivo: Escribe un programa que cuente la cantidad de palabras en un archivo de texto.


Lb_existe = Fl_ruta_file.exists();      #verificar si exite el archivo

if (Lb_existe):
    with Fl_ruta_file.open(mode = "r") as archivo:
        Lv_contenido = archivo.read()
        Lv_texto = Lv_contenido.split()
        print(Lv_texto)
        Ln_cantidad_palabras = len(Lv_texto)
        print(f"la cantidad de palabras que ingreso en el archivo txt es {Ln_cantidad_palabras}")
else:
    print("El archivo no existe, ¿Desea crearlo S/N?");
    Lv_control = input();
    if (Lv_control == 's' or Lv_control == "S"):
        with open("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23.txt", "w") as file01:
            Lv_valores = input("ingrese el mensaje que desea guardar en el archivo txt: ")
            file01.write(Lv_valores)
    elif(Lv_control == 'N' or Lv_control == "o"):
        print("El proceso a terminado, gracias.");
    else:
        print("Cod035 - Ruta especifica no existe")










