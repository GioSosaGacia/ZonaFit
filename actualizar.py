import mysql.connector

personas_db = mysql.connector.connect(
    #host es la ip local que es 127.0.0.1 o localhost
    host='localhost',
    user='root',
    password='Uppercase1.',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'update personas set nombre=%s,apellido=%s,edad=%s where id=%s' #placeholder nos permite sustituir parametros
valores = ('Victoria','Ramos',28,5)
cursor.execute(sentencia_sql,valores)
print('Se ha modificado la informacion')
personas_db.commit()

personas_db.close()
