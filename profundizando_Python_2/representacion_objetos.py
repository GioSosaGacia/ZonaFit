
'''Representacion de objetos: significa crear una cadena para mandar a imprimir los atributos de nuesto objeto
    1. con el metodo __str__
    2. repr
    3. format
    Se encuentran dentro de la clase object
    '''

#print(dir(object))

class Persona:

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    #repr, esta mas enfocado a los programadores, para ver los objetos y valores del mismo
    def __repr__(self):
        #return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'
        #{self.__class__.__name__} nos permite ver el nombre de la clase padre e hijas segun sea el caso
        return f'Persona(nombre:{self.nombre}, apellido:{self.apellido})'

    #str esta orientado al usuario final u otros sistemas
    #la implementacion por default llama al metodo repr
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    #format su implemetación por default es el metodo str y se manda al usar un f-string
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Giovanni','Sosa')
#repr
print(f'Mi objeto persona1: {persona1!r}') #!r con esto no aseguramos que se mande ha llamar el metodo repr
#str, print() utiliza por defecto al metodo str
print(persona1.__repr__()) #podemos llamar a los metodos: repr, str, format dentro de print para usar el formato deseacdo
print(persona1)
#format manda a llamar al metodo str, al utilizar f' en automatico se manda a llamar al metodo format
print(f'{persona1}')
