import pymysql

conexion = pymysql.connect('localhost', 'root', 'root', 'OLD_libreriaToni')

cursor = conexion.cursor()

cursor.execute('''
    SELECT
    b.title,
    b.price,
    a.name 
    FROM 
    books AS b
    INNER JOIN authors AS a
    ON a.author_id = b.author_id
''')

conexion.commit()

datos = cursor.fetchall()

conexion.close()