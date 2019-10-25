# libreria para conectar a MySQL
import pymysql


class Bd():
    def __init__(self, host, usuario, password, basedatos):
        self.conexion = pymysql.connect(
            host=host, user=usuario, password=password, db=basedatos)

    # metodo de busqueda
    def query(self, sql):
        with self.conexion.cursor() as cursor:
            cursor.execute(sql)
            self.conexion.commit()
            self.conexion.close()
            return cursor.fetchall()
    # metodo de alternativas

