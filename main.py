from flask import Flask, jsonify, render_template

from fetchData import get_data

app = Flask(__name__, static_url_path='/static')

trash1_value = -10

@app.route("/")
def index():
    return render_template("trash.html")

@app.route("/get_trash_value", methods=["GET"])
def get_trash_value():
    global trash1_value
    
    if trash1_value <= 100 :
        trash1_value = trash1_value + 10
    return jsonify({"trash1_value": trash1_value})


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)