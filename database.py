import pymysql
import pandas as pd

def update(sql):
    con = pymysql.connect(host='localhost', user='root', password='0000',
                        db='birdex', charset='utf8',
                        autocommit=True,
                        cursorclass=pymysql.cursors.DictCursor
                        )
    cur = con.cursor()
    cur.execute(sql)
    con.close()
    
def get_switch():
    con = pymysql.connect(host='localhost', user='root', password='0000',
                        db='birdex', charset='utf8',
                        autocommit=True,
                        cursorclass=pymysql.cursors.DictCursor
                        )
    cursor = con.cursor()
    sql = "SELECT * FROM birdex"
    cursor.execute(sql)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    data = df['get_switch']
    print(data)
    con.close()
    return data