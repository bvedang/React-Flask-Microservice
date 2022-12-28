import pandas as pd
from pandas import DataFrame
from helper import convertdfTodictforIssues
import json
import github3

githubToken = "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"
github = github3.login(token=githubToken)


class Repository:
    def __init__(self, owner, name) -> None:
        self.owner = owner
        self.name = name
        self.repo_df = self.getRepodf()
        self.createdIssue = self.getCreatedIssue()
        self.closedIssues = self.getClosedIssue()
        self.createdIssuesMonth = self.getcreatedIssuesMonth()
        self.closedIssuesWeek = self.getClosedIssueweek()
        self.createdClosed = self.getCreatedClosed()
        self.createdIssueForecast = []
        self.closedIssueForecast = []
        self.commits = []
        self.branches = []
        self.contiributor = []
        self.release = []

    def getRepodf(self):
        fileName = "./jsonFiles/"+self.name + "_issues.json"
        issuesCreated = [json.loads(line) for line in open(fileName)]
        issuesCreated = DataFrame(issuesCreated)
        return issuesCreated

    def getCreatedIssue(self):
        df1 = self.repo_df.copy()
        df1 = df1.groupby(['created_at'], as_index=False).count()
        df1 = df1[['created_at', 'issue_number']]
        return df1

    def getClosedIssue(self):
        df1 = self.repo_df.copy()
        df1 = df1.groupby(['closed_at'], as_index=False).count()
        df1 = df1[['closed_at', 'issue_number']]
        return df1

    def getCreatedClosed(self):
        temp = {}
        temp['created'] = int(self.repo_df['created_at'].notnull().sum())
        temp['closed'] = int(self.repo_df['closed_at'].notnull().sum())
        return temp

    def getcreatedIssuesMonth(self):
        df = self.createdIssue.copy()
        repo_df = pd.to_datetime(df['created_at'], format='%Y/%m/%d')
        repo_df.index = repo_df.dt.to_period('m')
        repo_df = repo_df.groupby(level=0).size()
        repo_df = repo_df.reindex(pd.period_range(
            repo_df.index.min(), repo_df.index.max(), freq='m'), fill_value=0)
        repo_df = DataFrame(repo_df)
        repo_df.reset_index(inplace=True)
        repo_df.columns = ['ds', 'y']
        repo_df['ds'] = repo_df['ds'].dt.to_timestamp('s').dt.strftime('%Y-%m')
        return convertdfTodictforIssues(repo_df)

    def getClosedIssueweek(self):
        df = self.closedIssues.copy()
        repo_df = pd.to_datetime(df['closed_at'], format='%Y/%m/%d')
        repo_df.index = repo_df.dt.to_period('w')
        repo_df = repo_df.groupby(level=0).size()
        repo_df = repo_df.reindex(pd.period_range(
            repo_df.index.min(), repo_df.index.max(), freq='w'), fill_value=0)
        repo_df = DataFrame(repo_df)
        repo_df.reset_index(inplace=True)
        repo_df.columns = ['ds', 'y']
        repo_df.ds = repo_df.ds.astype(str)
        return convertdfTodictforIssues(repo_df)
