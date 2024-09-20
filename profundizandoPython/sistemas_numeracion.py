#clase importada de otra clase
from profundizando_tipo_str import MiClase

#Profundizando Sistemas de Numeracion

#decimal 10
a = 10
#binario 0,1, 0b = binario
a = 0b1010
#octal 8 0o = octal
a = 0o12
#hexadecimal 16 0X = HEXADECIMAL
a = 0xA
print(f'a: {a}')

#Base numerica:
#BASE decimal = 10 el str lo converti a int, el segundo parametro es la base de decimal = 10
a = int('23', 10)
#binario = a base 2
a = int('10111', 2)
#base octal = 8
a = int('27',8)
#Base hexadecimal = 16
a = int('17',16)
print(a)


'''
La "interpolación" es una técnica que se utiliza para agregar nuevos puntos de datos dentro del rango de un conjunto de 
puntos de datos conocidos. Es posible usar la interpolación para rellenar datos faltantes, suavizar datos existentes y
 hacer predicciones, entre otras cosas.
 
 
'''
a = 3.0
print(f'a: {a:.2f}') #la interpolacion se aplica despues de los dos puntos se agrega un punto y un nomero depende el numero es la cantidad de ceros a agregar f = float

#Sobrecarga es cuando pasamos varios tipos de datos al mismo constructor
#constructor float() recibe datos int y str para comnvertirlos a float
a = float(10)
a = float('10')
print(f'a: {a:.2f}')


#Notacion exponencial (valores positivos o negativos)
a = 3e3
a = 3e-5
print(f'a: {a:.5f}')
#cualquier calculo que involucre un float, en automatico se promueve a float
a = 4.8 + 5
print(a)
print(type(a))


#import MiClase
help(MiClase)
print(MiClase.__doc__)
