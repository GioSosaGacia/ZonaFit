'''Profundizando en tuplas ()'''
#declarar variables
a,b = 'hola','adios'
print(a,b)

#swap (intercambio
a,b = b,a
print(a,b)

#regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5,6,7,8])
print(f'Valor minimo: {min}, Valor maximo: {max}')

#regresar la suma de una tupla
resultado = sum((1,2,3,4,5)) #sum utiliza un iterable
print(resultado)

def sumar(*args):
    return  sum(args)

resultado = sumar(1,2,3,4,5,6,7)
print(resultado)
