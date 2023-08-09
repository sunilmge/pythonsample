import flask
from flask import request, jsonify
from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields
from datetime import date, datetime
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Blueprint
import csv 
from pathlib import Path
import pandas as pd 


app = flask.Flask(__name__)
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT  = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config = {'app_name' : 'promptanalyzer'})
app.register_blueprint(SWAGGER_BLUEPRINT, URL_PREFIX = SWAGGER_URL)


#app.config['CSV_FILE'] = 'sqlite:////Path(__file__).parent/file.csv'
#db = SQLAlchemy(app)
file = Path(__file__).parent / "WatsonXAdapitveMockSimpleAllRiskProdMasked.csv"




@app.route('/')
def index():
    return 'Hello welcome to analyzer!'

@app.route('/greet')
def say_hello():
  return 'Hello from analyzer'
    
@app.route('/analyze', methods=['GET'])
def get_analyzer():
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    args = request.args
    error = "abcerror"
    error = args.get('error')
    # with file.open("r", encoding="utf-8") as data_file:
    #     csv_data = csv.reader(data_file)
    #     print(list(csv_data))
    data = pd.read_csv(file) 
    print(data.head)

    print(error);
    output = "12345678"

    return {'correlationid': output}

    
@app.errorhandler(404)
def resource_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404








