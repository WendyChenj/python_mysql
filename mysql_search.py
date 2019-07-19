import pymysql

class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            #connect
            self.conn = pymysql.connect(
                host ='127.0.0.1',
                user='root',
                password='1234',
                db='myFirst',
                port=3306,
                charset='utf8'
            )
        except Exception as e:
            print(e)

    def close_conn(self):
        try:
            if self.conn:
                #close connection
                self.conn.close()

        except Exception as e:
            print(e)

    def get_one(self):
        #sql
        sql = "SELECT * FROM customers;"
        #find cursor
        cursor = self.conn.cursor()
        #execute sql
        cursor.execute(sql)
        #get results
        #-rest = cursor.fetchall() #fetch all data, fetchone(): fetch a piece of data
        #-print(cursor.rowcount) #print how many rows in the database
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        #process results
        #print(rest)
        #close cursor
        cursor.close()
        #close connection
        self.close_conn()
        return rest
    
    def get_more(self):
        # sql
        sql = "SELECT * FROM customers;"
        # find cursor
        cursor = self.conn.cursor()
        # execute sql
        cursor.execute(sql)
        # get results
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()] #transfer to a list
        #close cursor
        cursor.close()
        #close connection
        self.close_conn()
        return rest
    
     def add_one(self):
        try:
           # sql
           sql = "INSERT INTO customers(id, address, phone, name) values(%s, %s, %s, %s);"
           # create cursor
           cursor = self.conn.cursor()
           # execute sql
           # submit date to database(提交数据到数据库)
           cursor.execute(sql, (16, 'zhao', 555, 'hhh'))
           cursor.execute(sql, (17, 'hhh', 666, 'cao', 'wang'))
           # commit(提交事务）
           self.conn.commit()
        except:
           print('error')
           self.conn.commit()   #part of sql has been submitted: sql(16,...) success
           #self.conn.rollback() #回滚事务
        row_count = cursor.rowcount
        # close cursor/connection
        cursor.close()
        self.close_conn()
        # row_count > 0: success
        return row_count > 0

def main():
    obj = MysqlSearch()
    #obj.get_one()
    #result = obj.get_one()
    #print(result['name'])
    #result = obj.get_more()
    #print(result)
    obj.add_one()

if __name__ == '__main__':
    main()
