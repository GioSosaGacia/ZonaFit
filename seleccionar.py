
import mysql.connector

personas_db = mysql.connector.connect(
    #host es la ip local que es 127.0.0.1 o localhost
    host='localhost',
    user='root',
    password='Uppercase1.',
    database='personas_db'
)

#creamos el objeto de tipo cursor el cual nos permite ejecutar sentencias
cursor = personas_db.cursor()
#ejecutar la consulta
cursor.execute('select * from personas')
resultado = cursor.fetchall() #para cargar todos los registros
for persona in resultado:
    print(persona) #como resultado nos arroja una tupla por registro

#Para cerrar la conexion a la base de datos
personas_db.close()
print('Se cerro la conexion...')
