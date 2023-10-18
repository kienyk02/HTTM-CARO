import mysql.connector
from dal.DBContext import host,username,passwd,database
    
class User:
    def __init__(self, id, username, password, email, highscore):
        self.id=id
        self.username=username
        self.password=password
        self.email=email
        self.highscore=highscore
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email":self.email,
            "highScore": self.highscore,
        }

def getAllUsers():
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    myCursor.execute("SELECT * FROM caro.user")
    records=[]
    for item in myCursor:
        records.append(User(item[0],item[1],item[2],item[3],item[4]))
    return records

def saveUser(data):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="update caro.user set username=%s, password= %s, email=%s, highScore=%s, where ID=%s"
    myCursor.execute(sql,data)
    db.commit()    

def getRanking():
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    myCursor.execute("SELECT * FROM caro.user where highScore!=10000 order by highScore asc")
    records=[]
    for item in myCursor:
        records.append(User(item[0],item[1],item[2],item[3],item[4]))
    return records

def updateHighScore(data):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="update user set highScore = %s where user.ID=%s and user.highScore > %s"
    myCursor.execute(sql,data)
    db.commit()

def insertUser(data):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="insert into user(username, password, email) values (%s,%s,%s)"
    myCursor.execute(sql,data)
    db.commit()
