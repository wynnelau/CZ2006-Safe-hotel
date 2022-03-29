from flask import Flask, request, jsonify
from flask_cors import cross_origin
from server.utils import *
import json

app = Flask(__name__)

@app.route('/filter', methods=['POST', 'GET'])
@cross_origin(origin='http://localhost:8080',headers=['Content-Type'])
def filter():
    print("Receive POST/GET messages!")
    area = request.json['area']
    highPrice = request.json['highPrice']
    lowPrice = request.json['lowPrice']
    print("Area:", area, "Upper bound:", highPrice, "Lower bound:", lowPrice)

    hotel_data = None
    with open(hotel_data_json, 'r', encoding='utf-8') as f:
        hotel_data = json.load(f)

    response = []
    
    for item in hotel_data:
        if item['location'] == area and item['price'] >= lowPrice and item['price'] <= highPrice:
            response.append(item)
    
    print("Target:", response)
    
    response = jsonify(response)

    return response