#REPL = Read Evaluete Print Loop, es una forma de ejecutar codigo mediante la consola
#python console
#solo se utiliza para hacer pequeñas pruebas y no guarda informacion

class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return  f'Nombre: {self.nombre}, Apellido: {self.apellido} Id:{hex(id(self)).upper()}'

if __name__ == '__main__':
    persona1 = Persona('Giovanni','Sosa')
    print(persona1)


''' esto se hizo desde la  consola de python 
Todo lo que se crea se debe de importar todo de manera individual o usando import *, como funciones, clases etc:

from profundizandoPython.persona_RELP import Persona
persona2 = Persona('Angelica','Jaimez')
persona2
<profundizandoPython.persona_RELP.Persona object at 0x000002375741FD00>
print(persona2)
Nombre: Angelica, Apellido: Jaimez Id:0X2375741FD00

'''
