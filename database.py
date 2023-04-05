import pymysql

con = pymysql.connect(host='localhost', user='root', password='0000',
                      db='birdex', charset='utf8',
                      autocommit=True,
                      cursorclass=pymysql.cursors.DictCursor
                     )
cur = con.cursor()
sql = "SELECT * FROM birdex"
cur.execute(sql)
rows = cur.fetchall()
con.close()