import connection
import csv
import codecs

conn = connection.connection
cur=conn.cursor()

cur.execute('USE data;')

cur.execute('CREATE TABLE department(code VARCHAR(255),'
            '             name VARCHAR(255)'
           )

with codecs.open(filename= "/Users/wenjiechen/Downloads/canDev/selecteddata.csv", mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    head = next(reader)
    print(head)
    for item in reader:
        args = tuple(item)

        sql = "INSERT INTO department VALUES(%s,%s);"

        connection.insert(cur, sql=sql, args=args)

        conn.commit()

cur.close()
conn.close()
