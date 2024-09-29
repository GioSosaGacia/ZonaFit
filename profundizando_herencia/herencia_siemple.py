'''Herencia Simple

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


