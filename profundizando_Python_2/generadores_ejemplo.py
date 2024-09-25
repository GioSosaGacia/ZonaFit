#generador de números del 1 al 5
def generador_numeros():
     for numero in range(1,6):
         yield numero
         print('Se reanuda la ejecución.')

#Utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

#consumimos los valores del generador
for valor in generador:
    print(valor)

#consumir a demanda
gen = generador_numeros()
try:
    print(f'Consumimos a demanda el generador: {next(gen)}')
    print(f'Consumimos a demanda el generador: {next(gen)}')
    print(f'Consumimos a demanda el generador: {next(gen)}')
    print(f'Consumimos a demanda el generador: {next(gen)}')
    print(f'Consumimos a demanda el generador: {next(gen)}')
    print(f'Consumimos a demanda el generador: {next(gen)}')
except Exception as e:
    print(f'Error al consumir el generador: {e}')


#Otra forma de consumur un generador con while
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresion del valor generado: {valor}')
    except StopIteration as e:
        print(f'Se termino de iterar el generador: {e}')
        break

