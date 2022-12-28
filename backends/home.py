from flask import jsonify
from flask_restful import Resource
import json
from helper import convertdfTodictforcreatedIssues
from pandas import DataFrame
from repositories import Repository
import github3

githubToken = "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"
github = github3.login(token=githubToken)


class Home(Resource):
    def get(self):
        stars = [json.loads(line)
                 for line in open('./jsonFiles/repostars.json')]
        forks = [json.loads(line)
                 for line in open('./jsonFiles/repoforks.json')]
        stackedCreatedClosed = []
        repositories = ["golang:go", "google:go-github", "angular:material", "angular:angular-cli",
                        "sebholstein:angular-google-maps", "d3:d3", "facebook:react", "tensorflow:tensorflow", "keras-team:keras", "pallets:flask"]
        for repoInfo in repositories:
            temp = repoInfo.split(':')
            repoName = temp[-1]
            repoOwner = temp[0]
            repoObj = Repository(owner=repoOwner, name=repoName)
            stackedCreatedClosedDict = {}
            stackedCreatedClosedDict['name'] = repoObj.name
            stackedCreatedClosedDict['created'] = repoObj.createdClosed['created']
            stackedCreatedClosedDict['closed'] = repoObj.createdClosed['closed']
            stackedCreatedClosed.append(stackedCreatedClosedDict)
        return jsonify({'stars': stars, 'forks': forks, 'stackedCreatedClosed': stackedCreatedClosed})


def getRepoStars():
    filename = './jsonFiles/repostars.json'
    inputfile = open(filename, 'w')
    inputfile.close()
    repositories = ["golang:go", "google:go-github", "angular:material", "angular:angular-cli",
                    "sebholstein:angular-google-maps", "d3:d3", "facebook:react", "tensorflow:tensorflow", "keras-team:keras", "pallets:flask"]
    for repoInfo in repositories:
        temp = repoInfo.split(':')
        data = {}
        inputFile = open(filename, 'a')
        repo = github.repository(temp[0], temp[-1])
        data['name'] = repo.name
        data['starcount'] = int(repo.stargazers_count)
        outstars = json.dumps(data)
        inputFile.write(outstars+'\n')
    inputFile.close()


def getRepoForks():
    filename = './jsonFiles/repoforks.json'
    inputfile = open(filename, 'w')
    inputfile.close()
    repositories = ["golang:go", "google:go-github", "angular:material", "angular:angular-cli",
                    "sebholstein:angular-google-maps", "d3:d3", "facebook:react", "tensorflow:tensorflow", "keras-team:keras", "pallets:flask"]
    for repoInfo in repositories:
        temp = repoInfo.split(':')
        data = {}
        inputFile = open(filename, 'a')
        repo = github.repository(temp[0], temp[-1])
        data['name'] = temp[-1]
        data['forkcount'] = int(repo.forks_count)
        outstars = json.dumps(data)
        inputFile.write(outstars+'\n')
    inputFile.close()
