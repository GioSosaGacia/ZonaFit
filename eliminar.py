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
sentencia_sql = 'delete from personas where id=%s'
valores = (5,)
cursor.execute(sentencia_sql,valores)
personas_db.commit()
print('Se ha eliminado el registro de la base de datos')
personas_db.close()
