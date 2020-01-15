import random
import pymysql


def getConnect():
    db = pymysql.connect(host="10.0.3.4",port=30306,user="root",passwd="123456",db="testdb" )
    return db

def createTable():
    db = getConnect()
    cursor = db.cursor()
    sql = """DROP TABLE IF EXISTS testtable ;CREATE TABLE `testtable` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `mydata` varchar(50) NOT NULL,
            PRIMARY KEY (`id`)
            )"""
    cursor.execute(sql)
    db.commit()
    db.close()

def insertData():
    try:
        db = getConnect()
        cursor = db.cursor()
        data = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        print('insert into testtable (mydata) values (\'' + data + '\')')
        cursor.execute('insert into testtable (mydata) values (\'' + data + '\')')
        db.commit()
        db.close()
    except Exception as e:
        print("no problem")

if __name__ == '__main__':
    while(True):
        insertData()