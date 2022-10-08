import os
from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
from flask import send_from_directory

from screenshot import screenshot, init_screenshot, close_screenshot

basedir = os.path.abspath(os.path.dirname(__file__))
uploads_file_path = os.path.join(basedir, 'tmp')

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY = "secret"
)
cors = CORS(app, responses={r"/*": {"origins": "*"}})

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