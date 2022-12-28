import json
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

d3 = [json.loads(line) for line in open("go.json")]
d3_df = DataFrame(d3)
# DailyIssue = d3_df.groupby(['created_at']).created_at.count()
# fig = DailyIssue.plot.line(figsize= (25, 10)).get_figure()
# fig.savefig("go.png")
DailyIssue = d3_df.groupby(['created_at'],as_index = False).count()
df1 = DailyIssue[['created_at','issue_number']]
df1.columns = ['ds', 'y']
final = []
temp = df1.to_dict()
for i in range(len(temp['ds'])):
    res = {}
    res['date'] = temp['ds'][i]
    res['issues'] = temp['y'][i]
    final.append(res)

jsonString = json.dumps(final)
jsonfile = open('test.json','w')
jsonfile.write(jsonString)
jsonfile.close()
print(final)