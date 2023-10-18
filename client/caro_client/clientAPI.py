from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=False, methods=["GET", "POST", "PUT", "DELETE"])
# Định nghĩa route cho API
# match result
@app.route('/getmatchbyuserid/<uid>', methods=['GET'])
def getMatchbyUserID(uid):
    try:
        from dal import matchhistoryDAO
        matchs=matchhistoryDAO.getMatchbyUserID(uid)
        matchs=[match.to_dict() for match in matchs]
        return jsonify(matchs)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/insertmatch', methods=['POST'])
def insertMatch():
    try:
        data=request.json
        from dal import matchhistoryDAO
        matchhistoryDAO.insertMatch((data['userID'],data['score'],data['status']))
        return jsonify("success")
    except Exception as e:
        return jsonify({"error": str(e)})
    
#user
@app.route('/getallusers', methods=['GET'])
def getAllUsers():
    try:
        from dal import userDAO
        users=userDAO.getAllUsers()
        users=[user.to_dict() for user in users]
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/saveuser', methods=['POST'])
def saveUser():
    try:
        data=request.json
        from dal import userDAO
        userDAO.saveUser((data['username'],data['password'], data['email'],data['highscore'],data['id']))
        return jsonify("success")
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/getranking', methods=['GET'])
def getRanking():
    try:
        from dal import userDAO
        users=userDAO.getRanking()
        users=[user.to_dict() for user in users]
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})    
    
@app.route('/updatehighscore', methods=['POST'])
def updateHighScore():
    try:
        data=request.json
        from dal import userDAO
        userDAO.updateHighScore((data['score'],data['userID'],data['score']))
        return jsonify("Success")
    except Exception as e:
        return jsonify({"error": str(e)})  

@app.route('/insertuser', methods=['POST'])
def insertUser():
    try:
        data=request.json
        from dal import userDAO
        userDAO.insertUser((data['username'],data['password'],data['email']))
        return jsonify("Success")
    except Exception as e:
        return jsonify({"error": str(e)})
        
if __name__ == '__main__':
    app.run(debug=True,port=5001)