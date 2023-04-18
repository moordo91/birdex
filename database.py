import pymysql

db = pymysql.connect(host='localhost', user='root', password='0000',
                      db='birdex', charset='utf8',
                      autocommit=True,
                      cursorclass=pymysql.cursors.DictCursor
                     )
cur = db.cursor(pymysql.cursors.DictCursor)

def get_target(date, num_id):
    sql = f"UPDATE `birdex`.`birdex` SET `date` = '{date}', `get_switch` = '1' WHERE (`no` = '{num_id}');"
    cur.execute(sql)
    rows = cur.fetchall()
    db.close()

sql = "SELECT * FROM birdex;"
cur.execute(sql)
rows = cur.fetchall()
db.close()