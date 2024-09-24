
''' diccionarios en python '''
#funcionan con el consecto llave valor o key:value
#los diccionarios si guardan un orden a diferencia de un set
diccionario = {'nombre':'juan', 'apellido':'perez','edad':28}
print(diccionario)

#las llaves son inmutables, solos los valores son mutables
#diccionario ={[1,2]:valor} no acepta lista como llave ya que es mutable
#diccionario = {(1,2):'valor'} #acepta una tupla en la llave, ya que la tupla es inmutable
#print(diccionario)

#si agregamos una llave a un diccionario y si no existe se agrega y si ya existe se remplaza solo el valor
diccionario['Departamento'] = 'sistemas'
print(diccionario)

#los diccionario no tienen valores duplicados, si ya existe solo cambia el valor
diccionario['nombre'] = 'Giovanni' #es sensible a altas y bajas
print(diccionario)


'''como recuperar elementos de un diccionario indicando una llave'''
print(diccionario['nombre'])
'''Si no encuentra la llave lanza una exepción'''
#print(diccionario['Nombre'])
'''metodo get recupera una llave, y si no existe no mande exepción '''
#retorna un valor aunque no exista la llave
print(diccionario.get('Nombre','No se encontro la llave'))
print(diccionario)


'''set defaul si modifica el diccionario aunque no se encuentra la llaver, tambien se agrega un valor por default'''
#si no se agrega el varlor marcara None
nombre = diccionario.setdefault('Nombre','Valor por default')
print(nombre)
print(diccionario)


'''imprimir un diccionario con el metodo pprint'''
from pprint import pprint as pp #pprint agrega un orden de la impresion de manera ascendente
help(pp)
pp(diccionario,sort_dicts=False)#sort_dicts evita que se ordene el diccionario
