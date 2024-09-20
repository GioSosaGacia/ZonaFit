

#bool = booleano true and false
#tipos numericos, falso = 0 y true = para los demas valores diferentes de 0
valor = 0
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
valor = 1
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')


#tipo str retorna false si la cadena esta vacia ' ' y distinto de vacio'Hola' retorna true
valor = ''
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
valor = 'Hola'
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

                                                                #key         value
#Tipo colecciones vacio = falso  con datos = true  [lista] {'diccionario':'Larousse'} (Tupla)
valor = []
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
valor = [1,2,3,4,5]
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')




'''Tipo bool en sentencias de control y con ciclo while'''
if bool(''):
    print('Regreso Verdadero')
else:
    print('Regreso falso')

if bool((1,)): #tupla
    print('Regreso Verdadero')
else:
    print('Regreso falso')

if bool([]): #lista
    print('Regreso Verdadero')
else:
    print('Regreso falso')
