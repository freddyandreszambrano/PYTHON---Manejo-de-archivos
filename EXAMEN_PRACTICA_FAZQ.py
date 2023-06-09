
print("**********contar numeros impares**************")
#contar numeros impares
Ln_numero = []

Ln_rango = int(input(("ingrese el rango de numeros de la lista:")))
for indi in range(Ln_rango):
     Ln_valor = int(input("ingrese valores numericos:"))
     Ln_numero.append(Ln_valor)

Ln_contador_par = 0
Ln_contador_impar = 0

for indice in Ln_numero:
    if (indice % 2 == 0):
        Ln_contador_par += 1
    else:
        Ln_contador_impar += 1
print("   ")
print(f"los cantidad de numeros pares son: {Ln_contador_par}");
print("   ")
print(f"los cantidad de numeros impares son: {Ln_contador_impar}");

print(" ")
print("**********Orden inverso**************")
print(" ")
#Orden inverso: Escribe un programa que tome una lista de números y la imprima en orden inverso.
Ln_rango = int(input(("ingrese el rango de numeros de la lista:")))
Ln_lista_num = []

for indi in range(Ln_rango):
    Ln_valor = int(input("ingrese los valores de la lista:"))
    Ln_lista_num.append(Ln_valor)

#imprimir en orden inverso con la funcion reversed
print("los valores seran mostrados de manera inversa")
for indice in reversed(Ln_lista_num):
    print(indice)


print(" ")
print("********** Ordenamiento de una lista **************")
print(" ")
#Ordenamiento de una lista: Escribe un programa que ordene una lista de números ingresada por el usuario de forma ascendente o descendente.
Ln_rango = int(input(("ingrese el rango de numeros de la lista:")))
Ln_list_num = []

for indi in range(Ln_rango):
    Ln_valor = int(input("ingrese los valores de la lista:"))
    Ln_list_num.append(Ln_valor);

length = len(Ln_list_num) -1
#metodo burbuja
#Recorrer toda la lista.
for indice in range(0, length):
    #Ordenar los elementos de la lista
    for Ln_ind in range(0,length):
        if (Ln_list_num[Ln_ind] > Ln_list_num[Ln_ind +1]):
            Ln_temporal= Ln_list_num[Ln_ind];
            Ln_list_num[Ln_ind] = Ln_list_num[Ln_ind + 1]
            Ln_list_num[Ln_ind + 1] = Ln_temporal

print('la lista ha sido ordenada exitodamente')
#Imprimir resultados
print(Ln_list_num)



print(" ")
print("********** Búsqueda en una lista **************")
print(" ")
#Búsqueda en una lista: Escribe un programa que busque un elemento específico en una lista ingresada por el usuario y muestre su posición.
Ln_rango = int(input(("ingrese el rango de numeros de la lista:")))
Ln_list_num = []
Ln_posicion = -1
Ln_indicador =0
for indi in range(Ln_rango):
    Ln_valor = int(input("ingrese los valores de la lista:"))
    Ln_list_num.append(Ln_valor);

Ln_buscar = int(input("Ingrese el valor que desea buscar:"));

for indi in range(len(Ln_list_num)):

    if (Ln_list_num[Ln_indicador] == Ln_buscar):
        Ln_posicion = Ln_indicador
        print(f"el valor {Ln_buscar} se encuentra en la posicion {Ln_posicion}")
    #variable indicador
    Ln_indicador +=1

if (Ln_posicion == -1):
    print(f"el valor {Ln_buscar} no se encuentra establecida en la lista")









