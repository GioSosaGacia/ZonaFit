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
