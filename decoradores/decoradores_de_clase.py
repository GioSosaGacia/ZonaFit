
#Creacion del metodo repr dinamicamente

'''
    Decoradores de clase: permite modificar la clase de manera programatica nuestra clase
    Es similar a los decoradores de funciones (es metaprogramacion)

    metodo repr de manera manual, este metodo regresa un str
    def __repr__():
        return f'Persona(nombre={self._nombre}, apellido={self._apellido})'

    1. se retorna el decorador
    2. la clase
'''
#este modulo nos ayuda a inspeccinar la firma del metodo __init__ y saber cuales son los parametros de la misma
import inspect


#un decorador recive como argumento otra funcion y retorna otra funcion
def decorador_repr(cls):#recibe el objeto de la clase cls
    print('1. Se ejecuta el decorador')
    print(f'Recibimos el objeto de la clase:  {cls.__name__}')#imprimimos que es lo que estamos recibiendo

    #Revisamos los atributos de la clase con el metodo vars, metodo built-in, vars retorna el atributo de dict de nuestra clase
    atributos = vars(cls)
    #iteramos cada uno de los atributos
    #for nombre, atributo in atributos.items():
     #   print(nombre,atributo)

    #Revisamos si se ha sobreescrito el metodo __init__, si no la ha sobreescrito nos arroja el error de tipo TypeError
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el metodo __init__')

#inspeccionar o recuperamos la firma(signature) del metodo __init__  inspect nos indica cuales son los parametros de nuestro metodo __init__
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma metodo __init__: {firma_init}') #la firma __init__ retorna una tupla

#recuperamos los  parametros, excepto self
    parametros_init = list(firma_init.parameters)[1:] #lo convertimos a una lista, e iniciamos a partir del parameto 1 : en adelante, descartando self
    print(f'Parametros init: {parametros_init}')

#Revisar si por cada parametro tiene un metodo property asociado
    for parametro in parametros_init:
        #property es un valor de tipo  built-in para preguntar si, se esta utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para el parametro: {parametro}')

    #Crear el metodo repr dinamicamente
    def metodo_repr(self):
        #obtenemos el nombre de la clase dinamicamnete
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        #Obtenemos los nombres de las propiedades y sus valore dinamicamente
        #expresion generadora para crear la cadena nombre_atriv = valor_atri
        generador_arg = (f'{nombre}={getattr(self,nombre)!r} ' for nombre in parametros_init)
        #lista del generador
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        #Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del metodo repr: {argumentos}')
        #Creamos la forma del metodo __repr__ a nuestra clase
        resultado_metodo_repr = f'{nombre_clase} ({argumentos})'
        print(f'Resultado metodo repr {resultado_metodo_repr}')
        return  resultado_metodo_repr

    #agregar dinamicamnete el metodo repr a nuestra clase
    setattr(cls,'__repr__', metodo_repr)

    return cls # retorna el objeto de la clase, para terminar de crear el objeto de la clase persona

@decorador_repr #este se puede reutilizar para otras clases
class Persona:

    def __init__(self,nombre, apellido,edad):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

persona1 = Persona('Juan','Medina',23)
print(persona1)
persona2 = Persona('Karla','Gomez',30)
print(persona2)

#Tiene los metodos de property nombre, apellido, repr
print(dir(Persona))
#Tiene el metodo repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)
