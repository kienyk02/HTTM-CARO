from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=False, methods=["GET", "POST", "PUT", "DELETE"])
# Định nghĩa route cho API
# match result
@app.route('/insertmatch', methods=['POST'])
def insertMatch():
    try:
        matchresult=request.json
        from dal import MatchResultDAO
        MatchResultDAO.insertMatch(matchresult)
        return jsonify("success")
    except Exception as e:
        return jsonify({"error": str(e)})
    
#user
@app.route('/updatehighscore', methods=['POST'])
def updateHighScore():
    try:
        data=request.json
        from dal import UserDAO
        UserDAO.updateHighScore(data)
        return jsonify("Success")
    except Exception as e:
        return jsonify({"error": str(e)})  
    
@app.route('/getUser/<id>', methods=['GET'])
def getUserByID(id):
    try:
        from dal import UserDAO
        user={
            "id": "",
            "email": "",
            "username": "",
            "password": "",
            "highScore": ""
        }
        user = UserDAO.getUserById(id).to_dict()
        return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    app.run(debug=True,port=5001)