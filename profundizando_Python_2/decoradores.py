'''Nos permite extender funcionalidad, añade caracteristicas a una función'''

'''
    Decoradores: es una funcion a que recibe una funcion b y regresa otra funcion c
    Se utiliza para extender funcionalidad
    1. Funcion decorador (a)
    2. Funcion a decorar (b)
    3. Funcion Decorada (c)
    Se utiliza para extender funcionalidad
'''
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        print('Antes de ejecutar la función ')
        funcion_a_decorar_b()
        print('Despues de ejecutar la función')

    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde función mostar_mensaje')

mostrar_mensaje()



'''Un decorador no solo sirve para modificar una funcion, si no varias'''
@funcion_decorador_a
def imprimir():
    print('Hola desde función imprimir')
print('')
imprimir()





'''Decoradores con argumentos: '''
print('')
def funcion_decorador_d(funcion_a_decorar_e):
    def funcion_decorada_f(*args,**kwargs):
        print('Antes de ejecutar la función decorada f ')
        resultado = funcion_a_decorar_e(*args,**kwargs)
        print('Despues de ejecutar la función decorada f')
        return resultado


    return funcion_decorada_f

@funcion_decorador_d
def sumar(a,b):
    return a + b

resultado = sumar(5,6)
print(f'Resultado de la suma: {resultado}')




