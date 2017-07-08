import hashlib, pprint, recognize_patterns
import binascii
from collections import Counter
import pandas as pd, numpy as np

df = pd.read_pickle('data/merged.pkl')
names = df['name'].tolist()
answers = []
for name in names:
    seed = str.encode("jackcbrown89" + name)

    h = hashlib.md5(seed).hexdigest()
    h = str(h)[:(len(h) // 2)]

    j = 0
    groups = []
    
    for i in range(len(s) + 1):
        if i % 16 == 0 and i != 0:
            groups.append(s[j:i])
            j = i
    print(groups)

    alpha_dict = {'00': 'aeimquy26', '01': 'bfjnrvz37', 
                 '10': 'cgkosw048', '11': 'dhlptx159'}
    
    answer = ''
    for i in groups:
        charset = alpha_dict.get(i[-2:])
        offset = int(i[:-2], 2)
        offset %= 9
        answer += list(charset)[offset]
    answers.append(str(answer))
df['answer'] = answers
print(df.head())
df.to_pickle('solved.pkl')
print('Solved :P')