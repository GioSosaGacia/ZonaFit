'''
generadores: es una funcion que permite regresar una secuencia de valores poco a poco
En vez de usar return utiliza yiel = rendimiento / producir
'''

def generador():
    yield 1
    yield 2
    yield 3
#Cosumimos el generador a demanda
gen = generador()
#con cada llamada consumimos un valor
try:
    print(next(gen))
    print('Se reanuda la ejecución')
    print(next(gen))
    print('Se reanuda la ejecución')
    print(next(gen))
    print('Se reanuda la ejecución')
    print(next(gen))
#si tratamos de consumir mas valores de lo que produce el generador arrojara error StopIteration
except Exception as e:
    print(f'''Se terminaron los recursos: {e}
        Genera más''')

#CONSUMINEDO los valores del generador con un ciclo for
for valor in generador():
    print(f'Numero generado: {valor}')
    print('Se reanuda la ejecución')
