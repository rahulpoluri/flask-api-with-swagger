from flask import Flask, jsonify, request, Response, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

data = [{"name": "Rahul", "Age": 25, "gender": "Male"},
        {"name": "Rahul2", "Age": 25, "gender": "Male"},
        {"name": "sana", "Age": 23, "gender": "female"},
        {"name": "Rahul4", "Age": 28, "gender": "Male"},
        {"name": "Rahul5", "Age": 25, "gender": "Male"}]

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask Swagger Experiment"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT)


@app.route("/", methods=["GET"])
def items_get():
    try:
        return jsonify(data), 200
    except:
        return {"detials": "Encountered server error"}, 500

@app.route("/", methods=["POST"])
def items_post():
    item = request.json
    print(item)
    try:
        print(item.keys())
        if list(item.keys()) != ["name", "Age", "gender"] or len(list(item.keys())) !=3:
            return {"detials": "params are not right"}, 400
        else:
            data.append(item)
            return {"detials": "Record added"}, 200
    except:
        return {"details": "Encountered server error"}, 500


if __name__ == "__main__":
    app.run(debug=True)
