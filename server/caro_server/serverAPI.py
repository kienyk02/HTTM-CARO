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
            "depth":1
        }
        # Xử lý dữ liệu
        from dal import modelDAO
        models=modelDAO.getAllModels()
        for model in models:
            if model.action=="enable":
                board["depth"]=model.easy if level=="Easy" else model.medium if level=="Medium" else model.hard
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
            "easy": "",
            "medium":"",
            "hard":"",
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
        from dal import modelDAO
        modeljson=request.json
        model = modelDAO.Model(modeljson["id"],modeljson["name"],modeljson["link"],modeljson["easy"],modeljson["medium"],modeljson["hard"],modeljson["action"])
        if int(id)>0:
            modelDAO.updateModel(model)
        else:
            modelDAO.addModel(model)
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
    
@app.route('/activemodel/<id>', methods=['GET'])
def activeModel(id):
    try:
        from dal import modelDAO
        modelDAO.activeModel(id)
        return jsonify("delete success")
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
    