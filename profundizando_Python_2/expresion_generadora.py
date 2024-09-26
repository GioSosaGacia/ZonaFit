'''
expresion generadora: es un generador anonimo
    una expresion generadora debe de estar entre parentesis para que sea valida,
    execto cuando se pasa a una funcion y esta sea una funcion valida
'''

#el valor de la derecha es asignado al for para crear el generador que se almacenara en la var multuplicacion
#El valor de la izq se asigna a la var multiplcacion para almacenar el generador creado por la expresion
multiplicacion = (valor*valor for valor in range(4))
#checamos el tipo
print(type(multiplicacion))
#consumimos el generador
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

#Tambien se puede pasar una funcion generadora a una funcion, sin utilizar parentesis
import math
suma = sum(valor * valor for valor in range(4))
print(f'Resultado de la suma: {suma}')




'''
    Expresiones generadoras con listas
    Tambien podemos utilizar una lista o cualquier otro iterador
    Los genradores se utilizan para recumerar grandes cantidades de datos a demanda
'''
lista = ['Juan','Perez']
#creamos el generador, si no lo pasamos como argumento a una función debemos de usar()
#recuperar datos a traves de un generador
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))





'''
Crear un str a partir de un generador, creado a partir de una lista
'''
lista = ['Karla','Gomez']
contador = 0
#Definimos una funcion para incrementar contador
def incrementar():
    global contador
    contador += 1
    return contador
#La primera parte es el yiel y la segunda el for, entre ()
'''el . quiere decir a donde se le aplicara el metodo, aqui usamos la funcion incrementar la cual se aplicara al nombre dentro del ciclo for'''
generador = (f'{incrementar()}.{nombre}' for nombre in lista)
'''generador lo convertimos a una lista'''
lista = list(generador)
print(lista)

'''Generar una cadena a partir de una lista'''
cadena = ', '.join(lista)
print(f'Cadena generada partir de la lista: {cadena}')
