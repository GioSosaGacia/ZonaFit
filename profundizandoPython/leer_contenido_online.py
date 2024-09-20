'''leer contenido online'''

#permite leer informacion de una url = Uniform Resource Locator
from urllib.request import urlopen #recupera la informacion de un archivo en internet

#palabras = []
#wit nos permite cerrar y abrir un archivo/recurso
with urlopen('https://ar.pinterest.com/pin/683210205984352904/') as mensaje:
    #3
    #contenido = mensaje.read().decode('utf-8')
    #print(contenido)

#contar ocurrencias dentro de una cadena
#print(contenido.count('head'))
#print(contenido.upper()) #convierte a mayusculas un str lower(minusculas)
#validar si existe x palabra en tal documento y es lo mismo para mayusculas
#print('Existe head? ', 'head'.lower() in contenido.lower())


#startswith  - inicia con
#print(contenido.startswith('<!DOCTYPE'))

#endswith termina con
#print(contenido.upper().endswith('</SCRIPT>'.upper()))





#2
#crea una lista  con las palabras por linea
    #for linea in mensaje:
     #   palabras_por_linea = linea.decode('utf-8').split()
      #  for palabra in palabras_por_linea:
       #     palabras.append(palabra)
#print(palabras)







#1
    #contenido = mensaje.read()
    #contenido = mensaje.read().decode('utf-8') #Para convertir bytes en cadenas en Python, podemos utilizar el método . decode()
    #print(contenido)

#guardar el archivo o url que se lee en un documento
#with open('nuevo_archivo', 'w', encoding='utf-8') as archivo:
 #   archivo.write(contenido)'''




#validar si una cadena contienen caracteres en minuscula o mayuscula
    mensaje = 'Hola Mundo'
    print(mensaje.lower().islower())
    print(mensaje.isupper())


#alinear cadenas en pythont

#centrar una cadena
titulo = 'Sitio Web de Global Mentoring'
print(len(titulo)) #para saber cuantos caracteres tenemos
print(titulo.center(50,'*'))
#otra manera de centrar el titulo:
print(titulo.center(len(titulo)+21,'-'))


#alineando a la izquierda y a la derecha ljust = left , justify
print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+21,'*'))
#rjust
print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo)+21,'*'))


#reemplazar contenido, espacios por comas
print(titulo.replace(' ',','))
#strip elimina caacteres al inicio y final de una cadena
titulo = '  *** Google Home ***  '
print(titulo)
print(len(titulo))
titulo = titulo.strip()
print(titulo)
print(len(titulo))
#tambien podemos eliminar caracteres a la izq y der
titulo = '*** Google Home ***'.strip('*') #tambien podemos usar lstrip y rstrip
print(titulo)



#REPL = Read Evaluete Print Loop, es una forma de ejecutar codigo mediante la consola
#python console
#solo se utiliza para hacer pequeñas pruebas y no guarda informacion

