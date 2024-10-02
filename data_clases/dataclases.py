'''
Para hacer el uso de dataclass debemos de importar dataclass from dataclasses
Maneja el metodo repr y init por defecto con usar @dataclass
'''

from dataclasses import dataclass
from typing import ClassVar



@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0



#dataclass es recomendado para clases que no contienen muchos metodos o valores
#frozen o congelado no modificable/inmutable
@dataclass(eq=True, frozen=True)
class Persona:
    #al agregar o declarar las variables se debe de asiganar el tipo de dato que este recibira e incluso ahi mismo se puede agreagar el valor
    nombre: str
    apellido: str
    domicilio: Domicilio
    #Para agregar variables de clase utilizamos ClassVar, indicamos el tipo de dato y el valor segun sea el caso, e importar el ClassVar from typing
    contador_personas: ClassVar[int] = 0

    #post_init permite hacer validaciones despues de que se ejecuta el metodo init
    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacio: {self.nombre}')


domicilio1 = Domicilio('Teodomiro Manzano',3692)
persona1 = Persona('Giovanni','Sosa',domicilio1)
print(f'{persona1!r}')
#Variable de clase
print(f'Variable de clase: {Persona.contador_personas}')
#Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
#variable con valores vacios
persona_vacia = Persona('Karla','',Domicilio('Carlos A. Carrillo',34))
print(f'Persona vacia: {persona_vacia}')


#Revisar igualdad entre objetos (__eq__) = equal
persona2 = Persona('Giovanni','Sosa', Domicilio('Longinos Cadena',18))
print(f'Objetos iguales?: {persona1 == persona2}')


#aGREGAR esta clase a una coleccion-> las colecciones no permiten valores mutables
coleccion = {persona1,persona2}
print(coleccion)
#frozen = True al utilizar frozen no permite modificar valores
#coleccion[0].nombre = 'Juan Carlos'
#persona1.nombre = 'Juan Carlos'
