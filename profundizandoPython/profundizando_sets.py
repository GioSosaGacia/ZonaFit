#profundizando en sets
#Un set es una coleccion de elementos unicos y ademas es mutable, y no contiene objetos repetido
#Los elementos de un set deden de ser inmutable, por lo cual soportaria un str, float, int etc
#Las listas son mutables [] por los cual no las soportan los sets

#los sets no soportan listas []
'''conjunto1 = {[1,2,3],[12,13,14]}
print(conjunto1)'''


'''Para crear un conjunto vacio es de la siguiente manera'''
conjunto = set()
print(conjunto)

'''si lo creamos asi, no se crea un conjunto si no un diccionario'''
conjunto = {}
print(conjunto)
print(type(conjunto))

conjunto = {'Juan', True, 18.0}
print(conjunto)
print(type(conjunto))

'''Un set es mutable'''
conjunto.add('Marcos')
print(conjunto)
'''Un set contiene valores unicos'''
conjunto.add('Juan')
print(conjunto)
'''crear un set a partir de un iterable'''
conjunto = set([1,2,3,4,1,2,8])
print(conjunto)
'''podemos agregar mas elementos o incluso otro set a un set'''
conjunto2  = {200,300,400,500,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,50,20])
print(conjunto)

'''copiar de un set a otro set de maner poco profunda, copiando solo las referencias'''
conjunto_copia = conjunto.copy()
print(conjunto_copia)
#verificar la igualdad en contenido
print(f'Es igual en contenido: {conjunto ==conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')





'''Operaciones algebraicas con set'''
#personas con distintas caracteristicas
pelo_negro = {'Juan','karla', 'Pedro','Maria'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'karla','Laura'}
menores_30 = {'karla','Juan','Maria'}
#Union: de 2 o mas sets para que quede más completo
#Todos con ojos cafe y pelo rubio (Union, No se repiten elementos) y se agregan los datos de ambos sets
print(ojos_cafe.union(pelo_rubio))
#invertir el orden con el mismo resultado = operacion comuntativa
print(pelo_rubio.union(ojos_cafe))
print(ojos_cafe.union(pelo_rubio))

#interseccion: Union de dos conjuntos pero solo los que se tengan en comun y los diferentes no se agregan, tienen que estar en ambos sets
#tambien es una operacion conmutativa
print(ojos_cafe.intersection(pelo_rubio))

#difference: retorna los elementos que se encuentren en un conjunto y los que esten iguales en el otro conjunto no
#las personas que esten en el primer set pero no en el segundo
print(pelo_negro.difference(ojos_cafe))#nota se tomara el set de lado izquierdo
print(ojos_cafe.difference(pelo_negro))

#symmetric difference: retorna elementos del conjunto a o b pero que no esten en comun en ambos
#pelo negro u ojos cafes pero no ambos y es una operacion conmutativa ya que, el resultado no es inervenido por el orden
print(pelo_negro.symmetric_difference(ojos_cafe))
print(ojos_cafe.symmetric_difference(pelo_negro))


'''Preguntas con sets'''
#subset, tenemos 2 conjunto a y b, preguntar si el subconjunto b es parte del a
#preguntar si un set esta conenido en otro set, true ya que ambos comparten casi los mismos elementos
print(menores_30.issubset(pelo_negro))

#superset, si el conjunto a es un conjunto del b
#si un set contiene a otro set
#si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))#falso ya que no contienen los mismos elementos a diferencia de uno

#disjoint, si no tiene nada que ver el conjunto b con el a, nada en comun
#preguntar si los de pelo negro no tienen pelo rubio(disjoin: dos conjuntos que no tienen nada en comun
print(pelo_negro.isdisjoint(pelo_rubio))
