from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app, supports_credentials=False, methods=["GET", "POST", "PUT", "DELETE"])
# Định nghĩa route cho API
@app.route('/getmove/<level>', methods=['POST'])
def get_move(level):
    try:
        # Lấy dữ liệu đầu vào từ request dưới dạng JSON
        board={
            "boardSquares":request.json,
            "depth":1 if level == "Easy" else (2 if level == "Medium" else 1)
        }
        # Xử lý dữ liệu
        from dal import modelDAO
        models=modelDAO.getAllModels()
        for model in models:
            if model.action=="enable" and model.level==level:
                result = subprocess.run(['python', model.link], input=json.dumps(board), text=True, capture_output=True)
                move = result.stdout
                # Trả về tuple
                return move
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/getmodels', methods=['GET'])
def get_models():
    try:
        from dal import modelDAO
        models=modelDAO.getAllModels()
        model_list=[model.to_dict() for model in models]
        return jsonify(model_list)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/getmodel/<id>', methods=['GET'])
def get_modelbyid(id):
    try:
        from dal import modelDAO
        model={
            "id": "",
            "name": "",
            "link": "",
            "level": "",
            "action": ""
        }
        if int(id)>0:
            model=modelDAO.getModelbyId(id).to_dict()
        return jsonify(model)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/savemodel/<id>', methods=['POST'])
def saveModel(id):
    try:
        data=request.json
        from dal import modelDAO
        if int(id)>0:
            modelDAO.updateModel((data["name"],data["link"],data["level"],data["action"],data["id"]))
        else:
            modelDAO.addModel((data["name"],data["link"],data["level"],data["action"]))
        return jsonify("success")
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/deletemodel/<id>', methods=['DELETE'])
def deleteModel(id):
    try:
        from dal import modelDAO
        modelDAO.deleteModel(id)
        return jsonify("success")
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)
    