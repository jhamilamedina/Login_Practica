import mysql.connector
from mysql.connector import Error
from os import getenv


class Storage:
    _connection = ''

    def __init__(self) -> None:
        pass

    def connect(self):
        connection = mysql.connector.connect(
            host='localhost',
            database='login_db',
            user='root',
            password=getenv('mysql_pass'))
        self._connection = connection
        print('Conexión abierta.')

    def disconect(self):
        print('Conexión cerrada')
        self._connection.close()

    def read(self):
        sql = 'select * from login_table;'
        cursor = self._connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        self.disconect()
        return records


# cnn = Storage()
# cnn.connect()
# records = (cnn.read())
# for r in records:
#     print(r)
