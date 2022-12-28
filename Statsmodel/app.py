from flask import Flask, jsonify
from flask_cors import CORS
import os
from helper import getRepoName, loadClosedIssueJsontoDataframe, loadCreatedIssueJsontoDataframe
from forecasting import statsForecast, statsForecastCommitsPullsRelease


app = Flask(__name__, static_folder='assests', static_url_path='/static')
CORS(app)


repositories = ["golang:go", "google:go-github", "angular:material", "angular:angular-cli",
                "sebholstein:angular-google-maps", "d3:d3", "facebook:react", "tensorflow:tensorflow", "keras-team:keras", "pallets:flask"]


@app.route("/statForecastIssueCreated", methods=["POST"])
def issueCreated():
    try:
        repoName = getRepoName()
        fileName = "./jsonfiles/" + repoName + "_issues.json"
        df = loadCreatedIssueJsontoDataframe(fileName)
        url = statsForecast("createdIssue", repoName, df)
        return jsonify({"url": url})

    except:
        return jsonify({"url": "URL_NOTFOUND"})


@app.route("/statForecastIssueClosed", methods=["POST"])
def issueClosed():
    try:
        repoName = getRepoName()
        fileName = "./jsonfiles/" + repoName + "_issues.json"
        df = loadClosedIssueJsontoDataframe(fileName)
        url = statsForecast("closedIssue", repoName, df)
        return jsonify({"url": url})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


@app.route("/statForecastCommits", methods=["POST"])
def commits():
    try:
        repoName = getRepoName()
        commits_file_exist = os.path.exists(
            "./csvfiles/" + repoName+'commits.csv')
        commits_url = ""
        if commits_file_exist:
            commits_url = statsForecastCommitsPullsRelease("commits", repoName)
            return jsonify({"url": commits_url})
        return jsonify({"url": "URL_NOTFOUND"})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


@app.route("/statForecastIssuePull", methods=["POST"])
def pull():
    try:
        repoName = getRepoName()
        pull_file_exist = os.path.exists("./csvfiles/" + repoName+'pull.csv')
        pull_url = ""
        if pull_file_exist:
            pull_url = statsForecastCommitsPullsRelease("pull", repoName)
            return jsonify({"url": pull_url})
        return jsonify({"url": "URL_NOTFOUND"})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


@app.route("/statForecastIssueRelease", methods=["POST"])
def release():
    try:
        repoName = getRepoName()
        release_file_exist = os.path.exists(
            "./csvfiles/" + repoName+'release.csv')
        release_url = ""
        if release_file_exist:
            release_url = statsForecastCommitsPullsRelease("release", repoName)
            return jsonify({"url": release_url})
        return jsonify({"url": "URL_NOTFOUND"})
    except:
        return jsonify({"url": "URL_NOTFOUND"})


if __name__ == '__main__':
    app.run(debug=True, port=5003)
