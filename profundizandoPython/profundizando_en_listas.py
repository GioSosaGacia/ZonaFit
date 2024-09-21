#las listas son mutables
#el metodo split retorna una lista de elementos dentro de una cadena mientras cada palabra este separada por una ,


nombres = ['Giovanni','Angelica','Maria','Luis']
nombres1 = 'Laura Raquel Ernesto'.split()

#sumar dos listas
print(f'Sumar listas: {nombres + nombres1}')
#Extender una lista sobre otra
nombres.extend(nombres1)
print(nombres)

#lista de nuemros
numeros = [10,1,34,23,4,8,3,6,1]
print(numeros)
#obtener el indice del primer elemento encontrado en una lista
#help(list.index)
print(numeros.index(3))

#invertir el orden de los elementos de una lista
numeros.reverse()
print(numeros)

#ordenar de manera desc como asc
numeros.sort() #sort permite ordenar los elementos de una lista
print(numeros)
numeros.sort(reverse=True)
print(f' Ordenar lista de manera desc con sort(reverse = True): {numeros}')


#Obtener elvalor minimo y maximo de una lista
print(f'Valor minimo: {min(numeros)}')
print(f'Valor maximo: {max(numeros)}')

#copiar elelemntos de una lista
numeros2 = numeros.copy()
print(f'Copia de lista: {numeros2}')
#checar si es la misma referencia a la hora de hacer la copia con is: permite preguntar si una variable apunta a la misma referencia
print(f'Misma referencia? {numeros is numeros2}') #da falso porque se ha copiado de manera correcta ya que no tienen la misma referencia
print(numeros == numeros2)#en cuestion de contenido

#otra menera de copiar una lista es con el constructor de la lista = list()
numeros3 = list(numeros)
print(numeros3)
print(f'Misma referencia? {numeros is numeros3}')

#slicing para hacer una copia
numeros4 = numeros[:] #starts:ends
print(numeros4)
print(f'Misma referencia? {numeros is numeros4}')


#Multiplicacion de listas
lista_multiplicacion = 5*[[2,5]]
print(lista_multiplicacion)
print(f'Misma referencia? {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Misma Contenido? {lista_multiplicacion[0] == lista_multiplicacion[1]}')

lista_multiplicacion[2].append(10) #se afectan todas las listas ya que comparten el mismo objeto
print(lista_multiplicacion)


#Matriz esta compuesta por una lista de listas la cual esta comformada por columnas y filas
print('')
matriz = [[10,20],[30,40,50],[60,70,80,90]]
print(f'Matriz: {matriz}')
#recuperando cada uno de los elementos:
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 2, Columna 2: {matriz[2][2]}')
print(f'Renglon 2, Columna 3: {matriz[2][3]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')


print('')
#Ordenamiento de listas
lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
#ordenar la lista por el largo de cada lista o candidad de elementos
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')



#built-in hace referencia a que son parte del lenguaje de python
print('')
#help(sorted)
nombres1 = ['juan carlos','pedro','esperanza','karla']
nombres1 = sorted(nombres1)
print(nombres1)
#ordenar de manera descendente y alfabeticamente
nombres1 = sorted(nombres1,reverse=True)
print(nombres1)
#ordenar por la cantidad de caracteres
nombres1 = sorted(nombres1,key=len)
print(nombres1)
#built-in tipo reversed
nombres1 = reversed(nombres1)
print(list(nombres1))
