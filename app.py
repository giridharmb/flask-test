from flask import Flask
from flask import render_template
from flask import jsonify
from flask.globals import request
import requests
import json

app = Flask(__name__)

@app.route('/main', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit_handler', methods=['POST'])
def submit_handler():
    request_json = request.get_json()
    print("/submit_handler : submit_handler() : request_json : {}".format(request_json))
    data1 = ""
    data2 = ""
    cloud = ""
    
    if "data1" in request_json:
        data1 = request_json["data1"]

    if "data2" in request_json:
        data2 = request_json["data2"]
        
    if "cloud" in request_json:
        cloud = request_json["cloud"]

    print("data1 : {}".format(data1))
    print("data2 : {}".format(data2))
    print("cloud : {}".format(cloud))

    return jsonify({"data":"successful"})

if __name__ == '__main__':
    app.run(port=7000, debug=True)
