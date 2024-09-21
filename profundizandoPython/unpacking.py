#desempaquetando  unpacking
valores = 1,2,4  #tupla de valores
print(type(valores))
print(valores)

'''
El desempaquetado o unpacking en Python es una técnica que permite asignar los elementos 
de una secuencia a variables individuales. Se utiliza principalmente para extraer 
los valores de una tupla o lista y asignarlos a variables separadas.
'''

#aplicando el unpacking
valor1, valor2, valor3 = 1,2,3 #se asigna cada valor a cada una de las variables segun el orden
print(valor1,valor2,valor3)
print(type(valor1))

valor1, valor2, *valor3, valor4, valor5 = 1,2,3,4,5,6,7,8,9 #* indica que los valores restantes se asignaran al valor3
print(valor1,valor2,valor3,valor4,valor5)
print(type(valor3))
valor1, valor2, *valor3, valor4, valor5 = [1,2,3,4,5,6,7,8,9] #* indica que los valores restantes se asignaran al valor3
print(valor1,valor2,valor3,valor4,valor5)
print(type(valor3))

# *_ hace referencia a la omicion de los datos para que estos no los imprima, pero aunn si se guardan los datos en tal variable
def regresar_varios_valores():
    return 1 ,2 ,3

valor1,valor2,valor3 = regresar_varios_valores()
print(valor1,valor2,valor3)

hora, separador, minutos = '09:16'.partition(':') #partition divide una cadena en tres partes
print(hora,separador,minutos)
help(str.partition)
