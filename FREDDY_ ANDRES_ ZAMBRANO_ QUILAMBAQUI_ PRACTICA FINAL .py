

#APLICAR TODO LOS CONOCIMIENTOS DEL CODIGO

from pathlib import Path

Fl_ruta_file = Path("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_P1.txt")


#verificar con exists haber si existe

#contar caracteres de un archivo
Lb_existe = Fl_ruta_file.exists()

if (Lb_existe):
    with Fl_ruta_file.open(mode = "r") as archivo:
        #para transformar a lectura
        Lv_contenido = archivo.read()
        Ln_caracter = 0
        lenght = len(Lv_contenido)
        for e in range(0, lenght):
            if (Lv_contenido[e] != " "):
                Ln_caracter +=1
        print("caracter : ", Ln_caracter)

else:
    print("El archivo no existe, ¿Desea crearlo S/N?");
    Lv_control =input();
    if (Lv_control == 's' or Lv_control == "S"):
        with open("T:\ESTRUCTURA DE DATOS\Mis talleres\Archivo_prueba_07_06_23_P1.txt", "w") as file01:
            Lv_valores = input("ingrese el mensaje que desea guardar en el archivo txt: ")
            file01.write(Lv_valores)
    elif(Lv_control == 'N' or Lv_control == "n"):
        print("El proceso a terminado, gracias.");
    else:
        print("Cod035 - Ruta especifica no existe")

