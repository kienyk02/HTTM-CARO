import mysql.connector
host="localhost"
username="root"
passwd="18082002"
database="caro_server"
class Model:
    def __init__(self, id, name, link, easy, medium, hard, action):
        self.id=id
        self.name = name
        self.name = name
        self.link=link
        self.easy=easy
        self.medium=medium
        self.hard=hard
        self.action=action
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "link": self.link,
            "easy": self.easy,
            "medium":self.medium,
            "hard":self.hard,
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
        records.append(Model(item[0],item[1],item[2],item[3],item[4],item[5],item[6]))
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
        record=Model(item[0],item[1],item[2],item[3],item[4],item[5],item[6])
    return record

def updateModel(model):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="update caro_server.model set name=%s, link= %s, easy=%s, medium=%s, hard=%s, status=%s where ID=%s"
    myCursor.execute(sql,(model["name"],model["link"],model["easy"],model["medium"],model["hard"],model["action"],model["id"]))
    db.commit()
    
def addModel(model):
    db=mysql.connector.connect(
        host=host,
        user=username,
        passwd=passwd,
        database=database
    )
    myCursor=db.cursor()
    sql="insert into caro_server.model(name,link,easy,medium,hard,status) values(%s,%s,%s,%s,%s,%s)"
    myCursor.execute(sql,(model["name"],model["link"],model["easy"],model["medium"],model["hard"],model["action"]))
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
    