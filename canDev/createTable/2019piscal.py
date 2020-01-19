import connection
import csv
import codecs
import urllib.request

conn = connection.connection
cur=conn.cursor()

cur.execute('USE data;')

cur.execute('CREATE TABLE actual(year VARCHAR(255),'
            '             mine VARCHAR(255),'
            '             agrg_pymt_amt VARCHAR(255))'
            )

years = []
for i in range(2003,2020):
    years.append(str(i))
for year in years:
    url = 'http://donnees-data.tpsgc-pwgsc.gc.ca/ba1/pt-tp/pt-tp-'+year+'-eng.csv'

    ftpstream = urllib.request.urlopen(url)
    csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    head=next(csvfile)
    print(head)

    head[0]=head[0][1:]
    print(head)

    index_yr = head.index('FSCL_YR')
    index_mine = head.index('MINE')
    index_agrg_pymt = head.index('AGRG_PYMT_AMT')
    print(index_yr, index_mine, index_agrg_pymt)

    sql = "INSERT INTO actual VALUES (%s,%s,%s);"

    for line in csvfile:
        yr=line[index_yr]
        mine=line[index_mine]
        agrg_pymt=line[index_agrg_pymt]

        args = (yr, mine, agrg_pymt)

        connection.insert(cur, sql=sql, args=args)

        conn.commit()


cur.close()
conn.close()













