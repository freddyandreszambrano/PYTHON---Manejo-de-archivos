print(" ")
print("********** Contar caracteres **************")
print(" ")
#Contar caracteres en un archivo: Escribe un programa que cuente la cantidad de caracteres en un archivo de texto.



from pathlib import Path

#crear un archivo especificando la ruta existente
Fl_ruta_file = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_02.txt")

Lb_existe = Fl_ruta_file.exists();      #verificar si exite el archivo

if (Lb_existe):
    with Fl_ruta_file.open(mode = "r") as archivo:
        Lv_contenido = archivo.read()
        lengt = len (Lv_contenido)
        Ln_contador_caracter = 0
        for indice in range(0, lengt):
            if (Lv_contenido[indice] != " "):
                Ln_contador_caracter += 1
        print(f"la cantidad de caracteres es {Ln_contador_caracter}")

else:
    print("El archivo no existe, ¿Desea crearlo S/N?");
    Lv_control =input();
    if (Lv_control == 's' or Lv_control == "S"):
        with open("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_02.txt", "w") as file01:
            Lv_valores = input("ingrese el mensaje que desea guardar en el archivo txt: ")
            file01.write(Lv_valores)
    elif(Lv_control == 'N' or Lv_control == "n"):
        print("El proceso a terminado, gracias.");
    else:
        print("Cod035 - Ruta especifica no existe")


