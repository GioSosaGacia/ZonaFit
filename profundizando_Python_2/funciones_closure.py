'''Una funcion closure es una función que a su vez encapsula otra funcion y puede retornarla '''
#una funcion closure mantiene un estado, donde las variables locales creadas,
#en la funcion pincipal serán accedidas por otras funciones anidas o mas internas
#Estado se refiere a la informacion que pueden almacenar las variables

#funcion principal:
#def operacion(a,b):
    #Definimos la funcion interna o anidada
 #   def sumar():
  #      return a + b
    #retornar la funcion
   # return sumar #sin parentesis ya que solo queremos regresar la funcion no mandarla a llamar


'''utilizando una fucnion lambda'''
def operacion(a,b):
#definir una función landa interna o anidada y la retornamos
    return lambda:  a + b


mi_funcion_closure = operacion(4,5)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')

#otra forma de llamar la funcion al vuelo,al momento de mandar a llamar la funcion y sin declarar una variable
print(f'Resultado de la funcion closure al vuelo: {operacion(2,2)()}')#los () indican la llamada a la funcion sumar


