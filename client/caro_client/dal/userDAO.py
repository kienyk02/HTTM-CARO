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

def updateHighScore(data):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="update user set highScore = %s where user.ID=%s and user.highScore > %s"
    myCursor.execute(sql,(data['score'],data['userID'],data['score']))
    db.commit()

def getUserById(id):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    myCursor.execute("SELECT * FROM caro.user where ID="+str(id))
    record=None
    for item in myCursor:
        record=User(item[0],item[1],item[2],item[3],item[4])
    return record