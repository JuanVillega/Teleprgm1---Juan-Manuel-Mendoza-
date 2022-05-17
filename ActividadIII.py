#Ejericicio 1

import math

def IntroducirRadio(vRadio):
    vArea = math.pi * vRadio ** 2
    print("Ejercicio 1------------>: Introducir Radio para econtrar el Area de un Circulo")
    print("El Area del Circulo es:", vArea)
IntroducirRadio(vRadio = (int(input("Elige un valor entero para el radio del circulo:"))))

#Ejericio 2

vMaximoValor = None

def Milista(vLista):
    for numlista in vLista:
            if numlista ==  max(vLista):
             print("Ejercicio 2------------>: vLista = [4,12,24]")
             print("El Maximo valor es:", numlista)
Milista(vLista = [4,12,24])


#Ejericio 3

def MilistaNumeros(vNumeros):
    Sumar_Impares=0
    for i in range(0,len(vNumeros)):
        if vNumeros[i] % 2 != 0:
            Sumar_Impares=Sumar_Impares+vNumeros[i]
    print("Ejercicio 3------------>: vNumeros = [3,4,5,6,7,12,15,24,33]")
    print("Suma de Valores Impares:" , Sumar_Impares)
    return Sumar_Impares


MilistaNumeros(vNumeros = [3,4,5,6,7,12,15,24,33])

#Ejercicio 4

def ContarCaracteres(vString):
    vContador = 0

    while vString[vContador:]:
        vContador +=1
    print("Ejercicio 4------------>:Introducir String y Cantidad de Caracteres necesarios para que el string este centrado")
    
    print("{:^150}".format(vString),"Cantidad de Caracteres del texto:",vContador)
    print("Cantidad de Caracteres necesarios para que salga centrado:", vContador^150) 

    return vContador

ContarCaracteres(vString = input("Introduce un texto 'String':"))