'''
Herencia Multiple Parte 1 y 2
La herencia multiple siempre inicia de izquierda a derecha
Cuando utilizamos super() se mandan a llamar todos los metodos en el orden del mro


Uso de super()
En pocas palabras, la función super() nos permite acceder a los métodos de la clase padre desde una de sus hijas.
'''


class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('metodo clase1.')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()


    def metodo(self):
        print('metodo clase2.')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('metodo clase3.')
        super().metodo()

#Al crera el objeto de la clase4, si esta no tienen metodo __init__ toma el de la clase2
#ya que empieza de izquierda a derecha
class Clase4(Clase2,Clase3):
    #si no estuviera definido el metodo en esta clase se llamaria el de la clase 2
    def metodo(self):
        print('metodo clase4.')
        super().metodo()


#Creamos objeto de la clase 4
clase4 = Clase4()
#Para saber cuales son las clases Padre de la clase4 podemos utilizar __base__ (Clases que usa de manera directa
print(Clase4.__bases__)
#Para saber todas las clases que utiliza hasta llegar a la clase padre mro
#nos muestra todas las clases involucradas
print(Clase4.__mro__)
#cual metodo se ejecuta, se manda a llamar el metodo de la clase 4 ya que es el primero que encuentra
#pero si lo tiene, por orden se va a la clase 2, despues en la 3 y al final de la clase uno
#siempre busca el elememnto o la funcion mas sercana, y para verlo podemos utilizar el mro
clase4.metodo()


