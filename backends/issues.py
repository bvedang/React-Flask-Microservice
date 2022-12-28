from flask import jsonify
from flask_restful import Resource
import csv
from repositories import Repository
from helper import getFBForecast, getLSTMForecast, getStatForecast, convertdfTodictforcreatedIssues
import github3
githubToken = "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"
github = github3.login(token=githubToken)


def repoReleasecsv(reponame: str, repoowner: str):
    releases = {}
    uritemplate = github.repository(repoowner, reponame)
    verison = (set(uritemplate.releases()))
    for k in verison:
        temp = k.as_dict()
        if temp["author"]:
            if temp["author"]["id"]:
                releases[k.created_at] = temp["author"]["id"]
    with open(reponame+'release.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in releases.items():
            writer.writerow([key, value])


def repoPullscsv(reponame: str, repoowner: str):
    pull_dict = {}
    uritemplate = github.repository(repoowner, reponame)
    pull_requests = (set(uritemplate.pull_requests()))
    for req in pull_requests:
        pull_dict[req.created_at] = req.number
    with open(reponame+'pull.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in pull_dict.items():
            writer.writerow([key, value])


def repoCommitcsv(reponame, repoowner):
    dict_1 = {}
    uritemplate = github.repository(repoowner, reponame)
    commits = (set(uritemplate.commits()))
    for commit in commits:
        commit = commit.as_dict()
        if commit["commit"] is not None:
            if commit["author"]:
                if commit["commit"]["author"]["date"]:
                    if commit["author"]["id"]:
                        dict_1[commit["commit"]["author"]
                               ["date"]] = commit["author"]["id"]

    with open(reponame+'commits.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict_1.items():
            writer.writerow([key, value])


class Issues(Resource):
    def get(self, repo):
        repositories = ["golang:go", "google:go-github", "angular:material", "angular:angular-cli",
                        "sebholstein:angular-google-maps", "d3:d3", "facebook:react", "tensorflow:tensorflow", "keras-team:keras", "pallets:flask"]
        repoInfo = ""
        for i in repositories:
            temp = i
            if repo == temp.split(':')[-1]:
                repoInfo = i
        repoInfoList = repoInfo.split(":")
        repoOwner = repoInfoList[0]
        repoName = repoInfoList[-1]
        jsonData = {"repoName": repoName, "repoOwner": repoOwner}
        fbForecastResult = getFBForecast(jsonData)
        lstmForecastResult = getLSTMForecast(jsonData)
        statForecastResult = getStatForecast(jsonData)
        repository = Repository(owner=repoOwner, name=repoName)

        return jsonify({'issues': convertdfTodictforcreatedIssues(repository.createdIssue),
                        'createdMonth': repository.createdIssuesMonth,
                        'closedWeekly': repository.closedIssuesWeek,
                        'fbForecast': fbForecastResult, 'lstmForecast': lstmForecastResult,
                        'statForecast': statForecastResult})
