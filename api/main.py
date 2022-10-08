from multiprocessing.dummy import Array
import os,json
from unicodedata import category
from flask import Flask,jsonify,request
from datetime import datetime, timedelta, timezone
from sqlalchemy import func
from flask_jwt_extended import get_current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,JWTManager \
    ,get_jwt,get_jwt_identity,current_user,create_refresh_token
import random
from flask import send_from_directory
from werkzeug.utils import secure_filename
from sqlalchemy import desc
from sqlalchemy import and_
from typing import Any

from screenshot import screenshot, init_screenshot, close_screenshot

basedir = os.path.abspath(os.path.dirname(__file__))
uploads_file_path = os.path.join(basedir, 'tmp')

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    ,SQLALCHEMY_TRACK_MODIFICATIONS = False
    ,SECRET_KEY = "secret"
    ,JWT_SECRET_KEY = "secret"
    ,JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=20)
    ,JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    ,JWT_TOKEN_LOCATION = ["headers", "query_string"]
    ,JSON_AS_ASCII = False
)
cors = CORS(app, responses={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

init_screenshot()

@app.route('/get/',methods=["GET"])
@cross_origin()
def send_image():
    url = request.args.get("url")
    if url:
        name = screenshot(url)
        return send_from_directory(uploads_file_path,name)
    return jsonify("error"), 403
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)
close_screenshot()