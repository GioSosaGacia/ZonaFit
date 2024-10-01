'''Herencia Multiple

'''

class ListaSimple:
    def __init__(self,elementos):
        self._elementos = list(elementos) #creamos una lista vacia

    def agregar(self,elementos):
        self._elementos.append(elementos)

    def __getitem__(self,indice): #permite recuperar un elemento de una lista
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort() #ordenar elementos de nuestra lista

    def __len__(self):
        return len(self._elementos)#mide la longitud de la lista

    def __repr__(self):#formato de impresion de la cadena
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self,elementos=[]):#si no recibe una lista, crea una
        super().__init__(elementos)
        #ordenamos siempre los elementos una vez incializados
        self.ordenar()

    def agregar(self,elemento):
        super().agregar(elemento)
        #ordenamos el nuevo elemento
        self.ordenar()

class ListaEnteros(ListaSimple):#esta lista solo acepta numeros...
    def __init__(self,elementos=[]):
        #valida que los elementos de la lista sean numeros
        for elemento in elementos:
            self._validar(elemento)
        #Una vez validados los elementos los agregamos
        super().__init__(elementos)

    def _validar(self,elemento):
        #validamos si el elemento es de tipo entero
        if not isinstance(elemento, int): #si no es una instancia de tipo entero, lanza error
            raise ValueError(f'No es un valor entero: {elemento}')

    #agregar el metodo agregar de la clase padre
    def agregar(self,elemento):
        self._validar(elemento)
        #Una vez validado lo agregamos a la lista
        super().agregar(elemento)

#Creamos una clase que combinara las dos clases hijas
#dependiendo el orden ser'a la prioridad
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

#creacion del objeto lista simple de tipo list
print('Lista simple'.center(50,'-'))
lista_simple = ListaSimple([10,1,5,3,6,8])
print(lista_simple)


#lista ordenada
print('Lista ordenada'.center(50,'-'))
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(1)
print(lista_ordenada)
print(len(lista_ordenada))
print(repr(lista_ordenada))

#Lista de enteros
print('Lista enteros'.center(50,'-'))
lista_enteros = ListaEnteros([1,4,6,-15])
print(lista_enteros)

#lista de enteros ordenada
print('Lista de enteros ordenada'.center(50,'-'))
lista_emteros_ordenada = ListaEnterosOrdenada([4,5,-1,10,14,-5])
print(lista_emteros_ordenada)
lista_emteros_ordenada.agregar(-20)
print(lista_emteros_ordenada)
#Saber las clases  padre y su orden usando MRO
print(ListaEnterosOrdenada.__bases__)
#MRO methond resolution Order
print(ListaEnterosOrdenada.__mro__)



#isinstance
#The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
print('Es Entero?', isinstance(10,int))
print('Es un STR?',isinstance('Hola',str))
print('Es una lista ent?', isinstance(lista_emteros_ordenada, ListaEnteros))
print('Es una lista ent, ord?', isinstance(lista_emteros_ordenada, ListaEnterosOrdenada))
print('Es una lista simple?', isinstance(lista_emteros_ordenada, ListaSimple))
#Tambien podemos pregunstar si la misma es una instancia de varios tipos
print('Es de varios tipos?', isinstance(lista_emteros_ordenada,(ListaSimple,ListaOrdenada,ListaEnterosOrdenada)))
