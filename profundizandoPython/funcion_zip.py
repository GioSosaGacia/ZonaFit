#nos permite unir iterables
#print(dir(__builtins__))
'''
zip significa comprimir
Nos permite unir 1 o varios iterables: tupla, lista,diccionarios etc
'''


#help(zip)
numeros = [1,2,3]
letras = ['a','b','c']
identificadores = 321, 322, 323, 324, 325
conjunto = {2,3,4,5}
mezclar = zip(numeros,letras,identificadores,conjunto)
print(mezclar)#despues de usar zip crea un objeto de tipo zip y para iterarlo se debe de convertir a una lista
print(list(mezclar))
#una vez consumido el recurso de debe de usar zip de nuevo para poder consumirlo de nuevo
print(tuple(zip(numeros,letras)))
print('')


'''Iterar varios iterables en paralelo con la funcion zip'''
for numero, letra, id, aleatorio in zip(numeros,letras,identificadores,conjunto):
    print(f'Numero: {numeros}, Letras: {letras}, Id: {id}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros,letras,identificadores,conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)



print('')
'''Procesos unzip en python no existe se usara el unpacking
aeparar los elementos de dos o mas iterables
'''

mezcla = [(1,'a'),(2,'b'),(3,'c'),]
numeros, letras = zip(*mezcla) # usamos * para hacer el unpacking
print(f' Numeros: {numeros}, Letras: {letras}')


'''ordenar un zip en python'''
print('Ordenando con zip'.center(30,'-'))
letras = ['c','x','f','a']
numeros = [3,1,8,6]
mezcla = zip(letras,numeros)
#sin ordenar
print(tuple(mezcla))
#ordenando por letra ya que es el primer iterable
print(sorted(zip(letras,numeros))) #aqui nmarca el orden las letras
print(sorted(zip(numeros,letras))) #por numero


'''Creando un diccionario a partir de dos iterables
Donde un iterable será la key y la otra el value
'''
print('Creacion de un diccionario con zip'.center(60,'*'))
llaves = ['nombre', 'apellido','edad']
valores = ['Giovanni','sosa',31]
diccionario = dict(zip(llaves,valores))
print(diccionario)

#modificar un elemento del diccionario
#asi mismo se puede agregar una nueva llave con su valor
llave = ['edad'] # se crea con una lista ya que es iterable
nueva_edad = [32]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)

