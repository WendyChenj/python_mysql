import connection
import csv
import codecs


conn = connection.connection
cur=conn.cursor()

cur.execute('USE data;')
# cur.execute('CREATE TABLE grants(program VARCHAR(255),'
#             '             department VARCHAR(255),'
#             '             agreementTitle VARCHAR(255),'
#             '             agreementValue VARCHAR(255),'
#             '             startDate VARCHAR(255),'
#             '             endDate VARCHAR(255),'
#             '             area VARCHAR(255))')


with codecs.open(filename= "/Users/wenjiechen/Desktop/grants.csv", mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    head = next(reader)
    print(head)
    for item in reader:

      args=tuple(item)

      sql="INSERT INTO grants VALUES(%s,%s,%s,%s,%s,%s,%s);"

      connection.insert(cur, sql=sql, args=args)

      conn.commit()

cur.close()
conn.close()


