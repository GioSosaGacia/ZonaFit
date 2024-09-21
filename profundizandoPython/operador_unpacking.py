#umpacking argumentos en python
# * este operador sirve para desempaquetar el contenido de una variable
#se puede aplicar a cualquier iterable si queremos en diccionarios es con doble **
numeros = [1,2,3]
print(numeros)
#imprime cada uno de los elementos de una lista, desempaquetando 1,2,3
print(*numeros)
print(*numeros, sep=' - ')

#para desempaquetar diccionarios es con doble **
#desempaquetando al momento de pasar un parametroa una fucnion
def sumar(a,b,c):
    print(f'Resultado de la suma: {a+b+c}')
sumar(*numeros) #utilizamos el unpacking *



#desempaquetar con variables
print('')
#extraer elementos de una lista o cualquier iterable
mi_lista = [1,2,3,4,5,6]
a,b,*c,d = mi_lista
print(a,b,c,d) #c de convierte a una lista

#crear listas con el operador umpacking
print('')
#unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1,lista2]
print(f'Lista de listas: {lista3}')
#crear listas con el operador umpacking
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

#Unir diccionarios
dic = {'A':1,'B':2,'C':3}
dic2 = {'D':4,'E':5}
dic3 ={**dic,**dic2}
print(dic3)
#list a partir de un str
lista = [*'holamundo']
print(lista)
#desempaquetando una lista
print(*lista)
print(*lista,sep='') #sep quita el espacio en blanco
