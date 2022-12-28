from pandas import DataFrame
import json
from flask import request


def getRepoName() -> str:
    data = request.get_json()
    repoName = data["repoName"]
    return repoName


def loadCreatedIssueJsontoDataframe(fileName: str) -> DataFrame:
    issuesCreated = [json.loads(line) for line in open(fileName)]
    issuesCreated = DataFrame(issuesCreated)
    df1 = issuesCreated.copy()
    df1 = df1.groupby(['created_at'], as_index=False).count()
    df1 = df1[['created_at', 'issue_number']]
    return df1


def loadClosedIssueJsontoDataframe(fileName: str) -> DataFrame:
    issuesClosed = [json.loads(line) for line in open(fileName)]
    issuesClosed = DataFrame(issuesClosed)
    df1 = issuesClosed.copy()
    df1 = df1.groupby(['closed_at'], as_index=False).count()
    df1 = df1[['closed_at', 'issue_number']]
    return df1
