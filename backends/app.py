from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from issues import Issues
from home import Home

app = Flask(__name__, static_folder='assests', static_url_path='/static')

CORS(app)
api = Api(app)

repositories = ["golang:go", "google:go-github", "angular:material", "angular:angular-cli",
                "sebholstein:angular-google-maps", "d3:d3", "facebook:react", "tensorflow:tensorflow", "keras-team:keras", "pallets:flask"]

api.add_resource(Home, '/home')
api.add_resource(Issues, '/<string:repo>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
