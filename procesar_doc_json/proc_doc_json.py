
'''
JSON = JavaScrip Object Notation
Se utiliza para enviar información entre sistemas cuando se esta trabajando con el concepto de web services o API's

personas": [
    { "nombre": "Juan Perez","edad": "28"},
    {"nombre": "Karla Gomez", "edad": "32"},
    {"nombre": "Carlos Lara", "edad": "35"},
    {"nombre": "María Esparza","edad": "22"},
    {"nombre": "Pedro Santos", "edad": "40"}
     ]
'''
import json
import urllib.request

#Leer el archivo de tipo JSON
respuesta = urllib.request.urlopen('https://www.urlencoder.org/es/enc/json/')
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)

#procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)
#imprimir solo los nombres
#Json se convierte a listas o diccionarios en python
for persona in json_respuesta['personas']:
    print(f'La persona:{persona["nombre"]}{persona["edad"]}')

#Accediendo a las variables independientes
print(f'Total de personas: {json_respuesta["Total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')
