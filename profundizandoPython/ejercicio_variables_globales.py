'''definimos una variable global '''

contador = 0

def mostrar_contador():
    print(contador)

def modificar_contador(c):
    '''si no utilizamos global la variable se queda en gris, ya que ahi una funcion antes, si no usamos global solo aplica modo lectura'''
    global contador #para modificar una variable global se debe de usar global, caso contrario no aplicaran los cambios
    contador = c

modificar_contador(5)
mostrar_contador()


'''Al terminar cada bloque la variable se destuye, al momento de mandar a llamar la funcion'''
