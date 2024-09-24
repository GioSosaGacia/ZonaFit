
'''Las funciones en python son ciudadanos de primera clase'''
#First class citizens
'''Las podemos definir en cualquier parte del codigo,
    las podemos usar como argumentos
    podemos asignar una funcion a una variable
    retornar funciones
'''
#1. definimos la funcion
def sumar(a,b):
    return a + b

#asignar una funcion a una variable(no se usan parentesis)
mi_funcion = sumar

#verificar el tipo de la variable
print(type(mi_funcion))

#llamamos la funcion a traves de la variable, ya usamos los parentesis()
resultado = mi_funcion(5,5)
print(resultado)


'''2. Funcion como argumento'''
def operacion(a,b,sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a,b)}')

operacion(4,5,sumar)


'''3. Podemos retornar una funcion'''
def retornar_funcion():
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'resultado de la funcion retornada: {mi_funcion_retornada(6,7)}')
