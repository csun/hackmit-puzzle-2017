import json
import requests
import pandas as pd

username = 'jackcbrown89'
solutions = []

df = pd.read_pickle('solved.pkl')
for (name, answer) in zip(df['name'], df['answer']):
    solutions.append({'name': name, 'solution': answer})

resp = requests.post('https://captcha.delorean.codes/u/' + username + '/solution',
        data=json.dumps({'solutions': solutions}))

print(resp.text)