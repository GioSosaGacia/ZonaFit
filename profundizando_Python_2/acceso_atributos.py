
''' ejemplo atributos publicos, protegidos, privados'''

class MiClase:

    def __init__(self,publico, protegido, privado):
        self.publico = publico #publico
        self._protegido = protegido#_ solo se accede dentro de nuestra clase o subclase de la misma
        self.__privado = privado # privado con __ y no se va a modificar y solo se usara dentro de esta misma clase



objecto = MiClase('Valor_publico','Valor_protegido','Valor_privado')
#acceso al valor publico, al poner el . en automatico nos muestra el atributo publico
print(objecto.publico)
#modificar al valor publico
objecto.publico = 'Nuevo valor publico'
print(objecto.publico)


#valor protegido
#solo lo debemos de usar dentro de la misma clase o dentro de las clases hijas
print(objecto._protegido)
#modificar protegido si nos permite pero no es lo que se recomienda
objecto._protegido = 'Nuevo valor protegido'
print(objecto._protegido)


#valor privado, solo se accede dentro de la misma clase
#print(objecto.__privado)
'''se puede usar de esta manera convierte: objeto._clase__atributo_privado '''
print(objecto._MiClase__privado)
objecto._MiClase__privado = 'Nuevo valor privado'
print(objecto._MiClase__privado)
