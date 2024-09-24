'''Funciones lambdas, se consideran funciones anonimas'''
#son pequeñas, no tienen nombre asigando y es en una sola linea de codigo,
#no requiere agregar parentesis para los paremetros
#no requiere del uso de la palabra return, pero di debe de regresar una expresión

#directamente no podemos asignar una funcion a una variable en esta forma de sintaxis
#mi_funcion = def sumar(a,b): return a + b


mi_funcion_landa = lambda a, b: a + b
resultado = mi_funcion_landa(4,6)
print(f'Resultado de sumar con la función lambda: {resultado}')


'''Funcion lambda sin argumentos '''
mi_funcion_landa = lambda: 'Funcion sin argumentos'
print(f'Llamar funcion lambda sin argumentos: {mi_funcion_landa()}')


'''Funcion lambda con parmetros por default'''
mi_funcion_landa = lambda a=2, b=3.0: a + b
print(f'Funcion lambda con valores por default: {mi_funcion_landa()}')


'''funcion landa con argumentos variables utilizando *args y **kwargs'''
mi_funcion_landa = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado de argumentos variables: {mi_funcion_landa(1,2,3,4, a=5,b=6)}')


'''Funciones lambda con argumentos, arguemntos variables y valores por default'''
mi_funcion_landa = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(F'Resultado funcion lambda: {mi_funcion_landa(1,2,4,5,6,7,d=8,e=9)}')
