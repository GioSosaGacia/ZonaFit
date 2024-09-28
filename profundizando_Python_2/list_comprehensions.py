'''
List comprehension offers a shorter syntax when you want to create a new list based on
 the values of an existing list.
 list comprehensions son for anidados solo que es aplicado a una sola linea

Los generadores utilizan tuplas() en lugar de listas...
'''

numeros = range(10)
lista_pares = []

#Creamos una nueva lista con los valores pares:
for numero in numeros:
    #revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero * numero)#agrega los numeros paras multiplicados pot si mismo
print(f'Lista de pares: {lista_pares} ')

'''hacemos lo mismo pero con list-comprehensions
    With list comprehension you can do all that with only one line of code:
    The Syntax
    newlist = [expression for item in iterable if condition == True]
'''
#1. es la expresion, 2. ciclo for y 3. la coleccion a recorrer y 4. opcional un if el if es opcional
#la condicion del if es opcional
lista_pares = []
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
print(f'Lista pares con list_comprehensions: {lista_pares}')


'''ejemplo con dos condiciones las condicones son opcionales
    solo se agrega el valor a la lista cuando el valor cumple ambas condiciones 
    es decir debe de ser divicible en etre dos y entre seis
'''
pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6==0 ]
print(f'Lista divisible entre 2 y 6: {pares}')



'''Agregando if else'''
lista_pares = []
lista_impares = []
for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')


'''Usando list comprehensions'''
print('')
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

'''lista de listas'''
lista_listas =[[1,2,3],[4,5,6],[7,8,9,10]]
#comvertir la lista de listas a una sola lista
lista_simple = [valor
                for sublista in lista_listas #recupera cada una de las lista
                for valor in sublista #recupera el contenido de cada lista y lo agrega a una sola lista
                ]
print(f'Lista simple: {lista_simple}')

'''lista de numeros pares a partir de una lista de listas'''
#sin list comprehensions
lista_pares = []
for sublista in lista_listas: #iteramos la lista de lista la cual retornara una sublista
    for valor in sublista: # obtenemos el valor de cada una de las sublistas
        if valor % 2 == 0:
            lista_pares.append(valor)
print(f'Lista sin list comprehensions: {lista_pares}')

#con list comprehensions en una sola linea de codigo
#no es necesario separar las lineas solo se hace para mejor lectura decodigo
lista_pares = []
lista_pares = [valor for sublista in lista_listas for valor in sublista if valor%2==0]
print(f'Lista de pares: {lista_pares}')

