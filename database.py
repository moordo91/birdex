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
    data = pd.concat([df['k_name'], df['get_switch']], axis=1)
    con.close()
    return data


def birdex(id_num):
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
    con.close()
    return df.loc[id_num]
