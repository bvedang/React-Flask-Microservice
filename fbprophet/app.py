from flask import Flask, jsonify, request
from flask_cors import CORS
from helper import getRepoName
from helper import loadCreatedIssueJsontoDataframe, loadClosedIssueJsontoDataframe
from forecasting import forecast, commitPullsReleaseForecast
import os

app = Flask(__name__, static_folder='assests', static_url_path='/static')
CORS(app)

repositories = ["golang:go", "google:go-github", "angular:material", "angular:angular-cli",
                "sebholstein:angular-google-maps", "d3:d3", "facebook:react", "tensorflow:tensorflow", "keras-team:keras", "pallets:flask"]


@app.route("/fbForecastforissuesCreated", methods=["POST"])
def issuesCreated():
    try:
        repoName = getRepoName()
        fileName = "./jsonfiles/" + repoName + "_issues.json"
        df = loadCreatedIssueJsontoDataframe(fileName)
        url = forecast("createdIssue", repoName, df)
        return jsonify({"url": url})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


@app.route("/fbForecastforissuesClosed", methods=["POST"])
def closedIssue():
    try:
        repoName = getRepoName()
        fileName = "./jsonfiles/" + repoName + "_issues.json"
        df = loadClosedIssueJsontoDataframe(fileName)
        url = forecast("closedIssue", repoName, df)
        return jsonify({"url": url})
    except:
        return jsonify({"url": "URL_NOTFOUND"})

# find out a way to handle if the csv file is no there on the main flask server side


@app.route("/fbForecastforcommits", methods=["POST"])
def commits():
    try:
        repoName = getRepoName()
        commits_file_exist = os.path.exists(
            "./csvfiles/" + repoName+'commits.csv')
        commits_url = ""
        if commits_file_exist:
            commits_url = commitPullsReleaseForecast("commits", repoName)
            return jsonify({"url": commits_url})
        return jsonify({"url": "URL_NOTFOUND"})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


@app.route("/fbForecastforpull", methods=["POST"])
def pulls():
    try:
        repoName = getRepoName()
        pull_file_exist = os.path.exists("./csvfiles/" + repoName+'pull.csv')
        pull_url = ""
        if pull_file_exist:
            pull_url = commitPullsReleaseForecast("pull", repoName)
            return jsonify({"url": pull_url})
        return jsonify({"url": "URL_NOTFOUND"})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


@app.route("/fbForecastforrelease", methods=["POST"])
def release():
    try:
        repoName = getRepoName()
        release_file_exist = os.path.exists(
            "./csvfiles/" + repoName+'release.csv')
        release_url = ""
        if release_file_exist:
            release_url = commitPullsReleaseForecast("release", repoName)
            return jsonify({"url": release_url})
        return jsonify({"url": "URL_NOTFOUND"})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
