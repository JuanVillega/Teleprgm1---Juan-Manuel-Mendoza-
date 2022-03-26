#Ejercicio 1
from os import remove


vUniTupla = (4,) #Al no tener la coma, Python reconoce el valor 4 como un número en ves de una tupla, si la función len() lo lee devolvera 4 enves de un elemento contado.

print("Cantidad de elementos de la tupla:", len(vUniTupla)) # LA función len(), sirve para contar la cantidad de elementos de una variable.

#Ejercicio 2
vEdades =  [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]

for vNumEdad in vEdades: #Obtener valores de vEdades
  if vNumEdad == 10: vEdades.remove(10) #Remover 10 de la lisa cada vez que vNumEdad sea igual a 10
     
for vNumEdad in vEdades: print("edad", vNumEdad, "años")#Mostrar lista modificada
vTotal = len(vEdades)#Contar total de elementos restantes

print("Total:", vTotal + 1, "elementos restantes")#Mostrar Cantidad de elementos restantes

