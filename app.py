from flask import Flask, send_from_directory
from flask_restful import Api
from api.Handler import Handler

app = Flask(__name__, static_url_path = '')
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(Handler, '/flask/home')