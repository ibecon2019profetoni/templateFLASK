import pymysql


def conexion_MYSQL(libro):
    conexion = pymysql.connect('localhost', 'root', 'root', 'OLD_libreriaToni')

    cursor = conexion.cursor()

    cursor.execute(f'''
        SELECT
        b.title,
        b.price,
        a.name 
        FROM 
        books AS b
        INNER JOIN authors AS a
        ON a.author_id = b.author_id 
        WHERE b.title 
        LIKE "%{libro}%"
        LIMIT 5
    ''')

    conexion.commit()

    datos = cursor.fetchall()

    conexion.close()

    return datos
