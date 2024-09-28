class Persona:
    #variable de clase
    contador_personas = 0

    #constructor de la clase es el metodo inicilizador permite inicializar los atributos
    #atributos de instancia
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

#mostrar los atributos de un objeto
persona1 = Persona('Giovanni','Sosa')
print(persona1.__dict__)# dict es un diccionario que despliega los atributos asociados al objeto creado
print(persona1) # si no se agrega el metodo str al momento de imprimir el objeto solo mostrara el objeto en memoria

#crear un atributo al vuelo(en ese momento)
print(persona1.contador_personas)#accediendo al atributo de clase
#No es posible modificarlo con el objeto, si no con la clase
persona1.contador_personas = 10
print(persona1.__dict__)
#el atributo anterior oculta el atributo de clase
print(Persona.contador_personas)#Aceedemos al atributo de clase
print(persona1.contador_personas)#accedemos al atributo del objeto


'''Cuando se crean atributos al vuelo en el objeto no se comparten entre los objetos solo se comparten los del metodo init
    los demas atributos creados al vuelo seran independientes para cada objeto
    '''
#un segundo objeto
persona2 = Persona('Angelica','Jaimes')
print(persona2.__dict__)
print(persona2.contador_personas)

#asociar un atributo de clase al vuelo
Persona.contador2 = 20 #Este nuevo atributo de clase se puede acceder ahora desde persona1 y persona2.contador2
print(Persona.contador2)
print(persona2.__dict__)



