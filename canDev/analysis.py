import connection

conn = connection.connection
cur=conn.cursor()

cur.execute('USE data;')

#actual total count for every year

sql="SELECT year, SUM(agrg_pymt_amt) FROM `actual` GROUP BY year"

cur.execute(sql)
count = cur.fetchall()

print(count)

#actual amount for every department and every year

# sql_amount="SELECT year, mine, SUM(agrg_pymt_amt) FROM data.actual GROUP BY mine, year;"
#
# cur.execute(sql_amount)
# amount=cur.fetchall()
#
# print(amount)


#grants from dtat
# cur.execute("SELECT * FROM grants;")
# a = cur.fetchall()
# print(total_grants(a)[0])
# print(total_grants(a)[1])


conn.commit()
cur.close()
conn.close()

def total_grants(grants):
    start_ind = 4
    end_ind = 5
    arg_value = 3
    start_year_after_2019 = 0
    end_year_before_2019 = 0
    end_year_after_2019 = 0
    end_year_null = 0
    for gr in grants:
        st_year = int(gr[start_ind][0:4])
        if st_year<2020:
            if gr[end_ind] == '':
                end_year_null += float(gr[arg_value])*(2019-st_year)/(2031-2019)
            elif int(gr[end_ind][0:4]) < 2020:
                end_year_before_2019 += float(gr[arg_value])
            elif int(gr[end_ind][0:4])>2020:
                end_year_after_2019+= float(gr[arg_value])*(2019-st_year)/(2031-2019)
        else:
            start_year_after_2019 += float(gr[arg_value])

    return [end_year_before_2019+end_year_after_2019+end_year_null, start_year_after_2019]

