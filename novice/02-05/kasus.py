import pymysql

try:
    db = pymysql.connect(host='localhost',
                                user='root',
                                password='gybjc111z',
                                db='tutorial',
                                charset='utf8mb4')
except Exception as error:
    print('gagal connect')
    print()

# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print ("Database version : %s " % data)

cursor = db.cursor()

sql = """select t1.full_names,t2.movies_rented
from table1 t1, table2 t2
where t1.membership_id=t2.membership_id
AND t1.membership_id=1"""

try:
    num = 0
    cursor.execute(sql)
# row count
# rcount = cursor.rowcount
    results = cursor.fetchall()
    print('Janet Jones Rents :')
    for row in results:
        # Now print fetched result
        num += 1
        print("{}. {}".format(num, row[1]))
except Exception as e:
    print("Error reading data from MySQL table", e)