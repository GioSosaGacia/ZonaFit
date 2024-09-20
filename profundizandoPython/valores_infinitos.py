import math
from decimal import Decimal

#manejo de valores infinitos
infinito_positivo = float('inf') #Para hacerlo negativo solo agregamos - antes de inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)}')
print('')

infinito_negativo = float('-inf') #Para hacerlo negativo solo agregamos - antes de inf
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito negativo?: {math.isinf(infinito_negativo)}')
print('')

#utilizando infinito desde la clase math, inf = infinito
'''Tambien podemos utilizar el modulo Decimal(infinity) como infinito, solo lo importamos import Decimal'''
infinito_positivo = math.inf #-math.inf infinito negativo
#infinito_positivon = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)}')

