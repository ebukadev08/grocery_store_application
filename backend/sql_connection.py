from mysql.connector import (connection)
__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = connection.MySQLConnection(user='root', password='victor',
                                           host='127.0.0.1',
                                           database='grocery_store')
    return __cnx


