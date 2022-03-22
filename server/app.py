from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from flask import Flask,request, jsonify
from flask_cors import CORS,cross_origin

## Init app

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Filter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(100))
    lowPrice = db.Column(db.Integer)
    highPrice = db.Column(db.Integer)

    def __init__(self, area, lowPrice, highPrice):
        self.area = area
        self.lowPrice = lowPrice
        self.highPrice = highPrice

class FilterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'area', 'lowPrice', 'highPrice')

filter_schema = FilterSchema()

CORS(app,resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/search', methods=['POST','GET'])
@cross_origin(origin='http://localhost:8080',headers=['Content-Type'])
def add_filter():
    area = request.json['area']
    highPrice = request.json['highPrice']
    lowPrice = request.json['lowPrice']

    # Create an instance
    new_filter = Filter(area, highPrice, lowPrice)

    # Save the todo in the db
    db.session.add(new_filter)
    db.session.commit()

    response = filter_schema.jsonify(new_filter)
    # response.headers.add('Access-Control-Allow-Origin', '*')

# return the created todo
    return response

# Start the app
if __name__ == '__main__':
    app.run(debug=True)