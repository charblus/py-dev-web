import pymysql
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='root', db='meizi_db')
cur = db.cursor()
cur.execute('select * from user_info')
data = cur.fetchall()
print(data)
cur.close()
db.close()

