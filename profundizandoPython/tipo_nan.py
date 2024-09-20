#contiene un modulo para preguntar si es un nan
import math
from decimal import Decimal #tmbien nos permite trabajar con nan

#NaN not a number es un valor indefinido de tipo numerico, podmeos utilizar el constructor float, etc
#nan no es sensible a mayusculas o minusculas
#nan es un tipo de dato numero indefinido

a = float('Nan')
print(f'a: {a}')
print(f'Es nan?: {math.isnan(a)}')

