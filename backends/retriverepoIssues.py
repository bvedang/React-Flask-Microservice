import json
from datetime import date
import github3
# from datetime import datetime, timedelta
import time
import dateutil.relativedelta
# repositories = ["golang:go","google:go-github","angular:material","angular:angular-cli","sebholstein:angular-google-maps","d3:d3","facebook:react","tensorflow:tensorflow","keras-team:keras","pallets:flask"]
repositories = ["sebholstein:angular-google-maps","facebook:react","tensorflow:tensorflow","keras-team:keras","pallets:flask"]
githubToken = "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"
github = github3.login(token=githubToken)
def generateIssuesData(repositories,github):
    today = date.today()
    for reposaddress in repositories:
        filename = reposaddress.split(':')[-1]+"_issues.json"
        inputfile = open(filename,'w')
        inputfile.close()
        for i in range(24):
            inputFile = open(filename, 'a')
            last_month = today + dateutil.relativedelta.relativedelta(months = -1)
            types = 'type:issue'
            repo = 'repo:'+reposaddress.replace(":","/")
            ranges = 'created:' + str(last_month) + '..' + str(today)
            search_query = types + ' ' + repo + ' ' + ranges
            for issue in github.search_issues(search_query):
                label_name=[]
                data={}
                current_issue = issue.as_json()
                current_issue = json.loads(current_issue)
                data['issue_number']=current_issue["number"]                          # Get issue number              
                data['created_at']= current_issue["created_at"][0:10]                 # Get created date of issue
                if current_issue["closed_at"] == None:
                    data['closed_at']= current_issue["closed_at"]
                else:
                    data['closed_at']= current_issue["closed_at"][0:10]               # Get closed date of issue
                for label in current_issue["labels"]:
                    label_name.append(label["name"])                                  # Get label name of issue
                data['labels']= label_name
                data['State'] = current_issue["state"]                                # It gives state of issue like closed or open
                data['Author'] = current_issue["user"]["login"]                       # Get Author of issue
                out=json.dumps(data)                                                  # save this all information to a JSON file
                inputFile.write(out+ '\n')
                
            inputFile.close()
            today = last_month
            time.sleep(10)


generateIssuesData(repositories,github)
        



