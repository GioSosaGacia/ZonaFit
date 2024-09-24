#funciones anidadas
''' Una funcion anidada es defirnir una función dentro de otra '''


def calculadora(a,b,operacion = 'sumar'):
    #definimos funcion anidada
    def sumar(a,b):
        return a + b

    def restar(a,b):
        return a - b
    #llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Resultado de sumar: {sumar(a,b)}')
    elif operacion == 'restar':
        print(f'Resultado de restar: {restar(a,b)}')

#al momento de mandar a llamar la funcion padre en autimatico las hijas se ejecutaran
calculadora(5,6)
calculadora(10,5,operacion='restar')

