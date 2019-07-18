import pymysql

try:
    conn = pymysql.connect(host='127.0.0.1',user='root', password = '1234', db = 'myFirst', port = 3306, charset = 'utf8')
    print('connect with: {}'.format(conn))
    cur = conn.cursor()
    sql = "insert into customers(id, address, phone, name) values('11','we','222','michael')"
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()

    cur.close()
    conn.close()
except Exception as e:
    print(e)
