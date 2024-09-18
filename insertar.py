import mysql.connector

personas_db = mysql.connector.connect(
    #host es la ip local que es 127.0.0.1 o localhost
    host='localhost',
    user='root',
    password='Uppercase1.',
    database='personas_db'
)

cursor = personas_db.cursor()
semtemcia_sql = 'insert into personas(nombre,apellido,edad) values(%s,%s,%s)'
valores = ('Juan Carlos','Ramirez',48)
cursor.execute(semtemcia_sql,valores)
personas_db.commit() #nos permite guardar la informacion en la base de datos

personas_db.close()
