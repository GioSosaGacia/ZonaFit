import math

#Profundizando en str
#concatenacion automatica no requiere del simbolo +
#no se puede concatenar una variable a un str a menos que utilizamos el simbolo +
variable = 'Python'
mensaje = 'Hola' ' ' 'Mundo' ' ' + variable
print(mensaje)

#solicitar ayuda
#help(str.capitalize)
#help(math)
#help(str)


'''
Uso de docString
Comentario de 
varias 
lineas

La cadena de documentación de Python, comúnmente conocida como docstring, es un literal de cadena y se utiliza en la 
definición de clases, módulos, funciones o métodos. Las docstrings son accesibles desde el atributo doc (__doc__) para
 cualquiera de los objetos Python y también con la función integrada help() .
'''

class MiClase:
    '''
    Este es un ejemplo de la documentacion de nuestra clase
    '''
    def __init__(self):
        '''
        Metodo de inicio de nuestra clase
        '''

    def mi_metodo(self,par1,par2):
        '''
        En automatico nos agrega los parametros o la documentacion de nuestro metodo
        :param par1:
        :param par2:
        :return: valor de retorno o de regreso
        '''

#podemos usar help(MiClase) dentro de otra clase y nosmostrara la descripcion de la misma
#solo se debe de importar la clase
'''
Se importo a la clase de sistemas numericos
'''

#solo nos envia la definicion de nuestra clase
#print(MiClase.__doc__)
#para mostrar el detalle del metodo init
#print(MiClase.__init__.__doc__)
#acceder a la documentacion del metodo definido
#print(MiClase.mi_metodo.__doc__)
#
#print(MiClase.mi_metodo)



'''
las cadenas en python son inmutables, solo se crea un nuevo objeto al concatenar 
'''
#help(str.capitalize()) convierte la primera letra en mayuscula
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(mensaje1,hex(id(mensaje1))) #id() representa la identificacion en memoria
print(mensaje2,id(mensaje2))
mensaje1 += 'adios'
print(mensaje1,hex(id(mensaje1)))

'''
Cada que se modifica una cadena no se sustitulle solo se crea un nuevo objeto
Hola Mundo Python
hola mundo 0x1cad6dd22b0
Hola mundo 1970699858928
hola mundoadios 0x1cad6dd74b0
'''




'''metodo join para cadenas'''
#metodo join une la cadena de un iterable como una tupla o una lista , las comillas son el espacio que dara entre cada str
#help(str.join)

tupla = ('Hola','Mundo','Universidad','Python')
mensaje3 = ' '.join(tupla)
#print(mensaje3)

lista_cursos = ['Java','Python','SQL','php','JS']
mensaje3 = ', '.join(lista_cursos)
#print(mensaje3)

cadena = 'Holamundo'
mensaje3 = '.'.join(cadena)
#rint(mensaje3)

diccionario = {'nombre':'Giovanni','apellido':'Garcia'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
#print(llaves,type(llaves))
#print(valores)




'''metodo split separar o dividir'''
'''
#retorna una lista de cada una de la palabras dentro de un str
help(str.split)
cursos = 'java python angular excel js'
listado_cursos = cursos.split()
print(listado_cursos)
print(type(listado_cursos))

cursos_separados_por_coma = 'java,Python,Excel'
listar_cursos = cursos_separados_por_coma.split(',') #dentro de split va el separador, caso contrario no separara  la lista y solo habra un objeto
#listar_cursos = cursos_separados_por_coma.split()
print(listar_cursos)
print(len(listar_cursos))

#split delimiter que es el numero de veces que se separa la cadena y los restantes como una sola cadena
listar_cursos = cursos_separados_por_coma.split(',',1)
print(listar_cursos)
print(len(listar_cursos))

'''





'''Formato str con parametros posicionales: '''
#con el uso de f-str
#%s = quiere decir que vamos a sustituir un str, nombre se sustutuye en el parametro %S
# %d para un entero
#%.2f para float
nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es: %s y tengo %d años ' %(nombre, edad)
#print((mensaje_con_formato))

persona = ('Karla','Gomez',5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es: %.2f pesos x mes ' #%(persona)
#print(mensaje_con_formato)
#print(mensaje_con_formato%persona) #tambien se puede de esta forma







'''Metodo format: sirve para dar formato a las cadenas de txto
placeholder {}'''
sueldo = 3000
mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
#print(mensaje)

#dependiendo de como este el comodo del indice, es como se imprimiran los valores {} por posicion dentro de las llaves
mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
#print(mensaje)
#Tambien podemos utilizar argumentos o nombres con el metodo format
mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
#print(mensaje)
#con un diccionario
diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre {persona[nombre]} Edad  {persona[edad]} Sueldo {persona[sueldo]:.2f}'.format(persona=diccionario) #persona solo se uso para renombrar el diccionario [nombre] es el parametro posicional que deseamos obtener
print(mensaje)

'''uso de f.string o template literal: este es el mas recomendable y mas utilizado'''
nombre = 'Giovanni'
edad = 31
sueldo = 12000
mensaje = f'Nombre {nombre} Edad  {edad} Sueldo {sueldo:.2f}' #a esto se le conoce como interpolacion
print(mensaje)

#metodo print
print(nombre,edad,sueldo, sep=', ')



#multiplicacion de cadenas ' ', tuplas (), listas[]
resultado = 3*'Hola, '
print(resultado)



'''Caracteres de scape, son caracteres que pueden crear error o problema al imprimir la informacion'''
resultado = 'Hola \' mundo' #la \ inversa nos sirve como un caracter de escape 'hola' ' Mundo' asi marcaria error el str
print(resultado)
resultado = 'se va a eliminar un punto.\b' # \b = backspace y quita o elimina un caracter en este caso el .
print(resultado)

#Caracter \ si lo queremos utilizar solo lo debemos colocar 2 veces
resultado = 'c:carpeta\\estado\\r'
print(resultado)

#row string permite usar caracteres especiales/escape y se aplica utilizando la r al inicio de la cadena
resultado = r'cadena con salto \nde linea sin aplicar el salto de linea'
print(resultado)
resultado = 'cadena con salto \n de linea sin aplicar el salto de linea'
print(resultado)


#caracteres Unicode = set de caracteres universales, ASCII STANDAR para la representacion de caracteres en cualquier dispositivo electronico
print('Hola\u0020Mundo') #unicode \u0020 representa un espacio en blanco
print('Notación simple de unicode: ','\u0041') #notacion extendida \U00000041 = A,  \x41 = hexadecimal A
print('\u2665')

#Caracateres ASCII
caracter = chr(65)
print(caracter)
caracter = chr(97)
print(caracter)





'''Carcater Byte = es un conjunto de 8 bits y constituye el minimo elelemnto de memoria 
direccionable en una computadora, se utiliza con archivos en internet que vienen en bites y con ascii y unicode los podemos traducir'''
caracteres_en_bytes = b'Hola mundo' #la b indica que contiene bits
print(caracteres_en_bytes)
mensaje = b'Univeridad Python'
print(mensaje[0]) #resultado es = 85 y corresponde en ascii a la leta U
#utilizamos la tabla asscii para ver que parametro es utilizando chr
print(chr(85))
lista_de_caracteres = mensaje.split()
print(lista_de_caracteres)


'''Convertir de str a bites and biceversa'''
string = 'Programación con Python'
print(f'string original: ',string)
bytes = string.encode('UTF-8')#ENCODE de str LO TRANSFORMA A BITES
print('Bytes codificado:', bytes)
#decodificando de bytes a str
string2 = bytes.decode('UTF-8') #decode de bytes a str
print('String decodificado', string2)
#ver si la cadena original es = a la cadena decodificada
print(string == string2)

