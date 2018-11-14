import os
import requests
import pandas as pd

#Loading ionosphere data from UCI repository
#Can be replaced by any other URL whose dataset is to be obtained
files = os.listdir()
if 'ionosphere.txt' in files:
    with open('ionosphere.txt','r') as f:
        raw_data = f.read()
else:
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data'
    response = requests.get(url)
    raw_data = response.text
    with open('ionosphere.txt','w') as f:
        f.write(raw_data)

#Process data into csv file
rows = raw_data.strip('\n').split('\n')
rows = [row.split(',') for row in rows]
df = pd.DataFrame(rows)
df.rename(columns={df.columns.values[-1]: 'target'},inplace=True)
df.to_csv('ionosphere_processed.csv')
