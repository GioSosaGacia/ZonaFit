
'''
    Orden de inicializacion de objetos
    si la clase hija no define sus metodos se utilizaran los de la clase padre por medio del metodo super()
'''
class Padre:

    def __init__(self):
        print('Inicialización de la clase padre')

    def metodo(self):
        print('Método padre')

class Hijo(Padre):
    #se amnda a llamar el metodo __init__ de la clase padre siempre y cuando la clase hija no defina el metodo init
    def __init__(self):
        #de manera opcional podemos mandar a llamar el metodo init de la clase padre con (super)
        print('Inicializador hijo')
        super().__init__()

    #sobreescribimos el heredado de la clase padre
    def metodo(self):
        print('Método sobreescrito de la clase padre en la clase hijo...')
        super().metodo()


#padre1 = Padre()
#padre1.metodo()

hijo1 = Hijo()
hijo1.metodo()
