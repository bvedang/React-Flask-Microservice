from pandas import DataFrame
import requests


def convertdfTodictforIssues(df):
    finalRes = []
    temp = df.to_dict()
    for i in range(len(temp['ds'])):
        res = {}
        res['date'] = temp['ds'][i]
        res['issues'] = temp['y'][i]
        finalRes.append(res)
    return finalRes


def convertdfTodictforcreatedIssues(df: DataFrame):
    finalRes = []
    temp = df.to_dict()
    for i in range(len(temp['created_at'])):
        res = {}
        res['created_at'] = temp['created_at'][i]
        res['issue_number'] = temp['issue_number'][i]
        finalRes.append(res)
    return finalRes


def getFBForecast(jsonData: dict) -> dict:
    issuesCreatedUrl = requests.post("http://127.0.0.1:5001/fbForecastforissuesCreated",
                                     json=jsonData)
    issuesClosedUrl = requests.post("http://127.0.0.1:5001/fbForecastforissuesClosed",
                                    json=jsonData)
    commitsUrl = requests.post("http://127.0.0.1:5001/fbForecastforcommits",
                               json=jsonData)
    pullUrl = requests.post("http://127.0.0.1:5001/fbForecastforpull",
                            json=jsonData)
    releaseUrl = requests.post("http://127.0.0.1:5001/fbForecastforrelease",
                               json=jsonData)
    return {"issuesCreatedUrl": issuesCreatedUrl.json()['url'], "issuesClosedUrl": issuesClosedUrl.json()['url'],
            "commitsUrl": commitsUrl.json()['url'], "pullUrl": pullUrl.json()['url'], "releaseUrl": releaseUrl.json()['url']}


def getLSTMForecast(jsonData: dict) -> dict:
    issuesCreatedUrl = requests.post("http://127.0.0.1:5002/lstmForecastIssueCreated",
                                     json=jsonData)
    issuesClosedUrl = requests.post("http://127.0.0.1:5002/lstmForecastIssueClosed",
                                    json=jsonData)
    commitsUrl = requests.post("http://127.0.0.1:5002/lstmForecastCommits",
                               json=jsonData)
    pullUrl = requests.post("http://127.0.0.1:5002/lstmForecastIssuePull",
                            json=jsonData)
    releaseUrl = requests.post("http://127.0.0.1:5002/lstmForecastIssueRelease",
                               json=jsonData)

    return {"issuesCreatedUrl": issuesCreatedUrl.json()['url'], "issuesClosedUrl": issuesClosedUrl.json()['url'],
            "commitsUrl": commitsUrl.json()['url'], "pullUrl": pullUrl.json()['url'], "releaseUrl": releaseUrl.json()['url']}


def getStatForecast(jsonData: dict) -> dict:
    issuesCreatedUrl = requests.post("http://127.0.0.1:5003/statForecastIssueCreated",
                                     json=jsonData)
    issuesClosedUrl = requests.post("http://127.0.0.1:5003/statForecastIssueClosed",
                                    json=jsonData)
    commitsUrl = requests.post("http://127.0.0.1:5003/statForecastCommits",
                               json=jsonData)
    pullUrl = requests.post("http://127.0.0.1:5003/statForecastIssuePull",
                            json=jsonData)
    releaseUrl = requests.post("http://127.0.0.1:5003/statForecastIssueRelease",
                               json=jsonData)
    return {"issuesCreatedUrl": issuesCreatedUrl.json()['url'], "issuesClosedUrl": issuesClosedUrl.json()['url'],
            "commitsUrl": commitsUrl.json()['url'], "pullUrl": pullUrl.json()['url'], "releaseUrl": releaseUrl.json()['url']}
