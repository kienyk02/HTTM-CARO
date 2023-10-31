import mysql.connector
from dal.DBContext import host,username,passwd,database

class Match:
    def __init__(self, id, userid, score, status,time):
        self.id=id
        self.userid=userid
        self.score=score
        self.status=status
        self.time=time
    def to_dict(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "score": self.score,
            "status": self.status,
            "time": self.time
        }

def getMatchbyUserID(uid):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="SELECT * FROM caro.match_result where userID="+str(uid)+" order by ID desc"
    myCursor.execute(sql)
    records=[]
    for item in myCursor:
        records.append(Match(item[0],item[1],item[2],item[3],item[4]))
    return records

def insertMatch(data):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="insert into match_result(userID,score,status) values(%s,%s,%s)"
    myCursor.execute(sql,(data['userID'],data['score'],data['status']))
    db.commit()