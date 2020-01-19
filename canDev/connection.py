import pymysql

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '12345678',
                             db = 'data'
                             )

cur=connection.cursor()

def insert(cur, sql, args):
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(e)
        connection.rollback()

