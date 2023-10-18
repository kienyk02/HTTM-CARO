import mysql.connector
host="localhost"
username="root"
passwd="18082002"
database="caro_server"
class Model:
    def __init__(self, id, name, link, level, action):
        self.id=id
        self.name = name
        self.name = name
        self.link=link
        self.level=level
        self.action=action
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link,
            "level": self.level,
            "action": self.action
        }

def getAllModels():
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    myCursor.execute("SELECT * FROM caro_server.model")
    records=[]
    for item in myCursor:
        records.append(Model(item[0],item[1],item[2],item[3],item[4]))
    return records

def getModelbyId(id):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    myCursor.execute("SELECT * FROM caro_server.model where ID="+str(id))
    record=None
    for item in myCursor:
        record=Model(item[0],item[1],item[2],item[3],item[4])
    return record

def updateModel(data):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="update caro_server.model set name=%s, link= %s, level=%s, status=%s where ID=%s"
    myCursor.execute(sql,data)
    db.commit()
    
def addModel(data):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="insert into caro_server.model(name,link,level,status) values(%s,%s,%s,%s)"
    myCursor.execute(sql,data)
    db.commit()

def deleteModel(id):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    myCursor.execute("delete from caro_server.model where ID="+str(id))
    db.commit()
    