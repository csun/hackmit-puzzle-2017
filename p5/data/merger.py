import pandas as pd
df_merged = pd.DataFrame()
for i in range(1,14):
    df_merged = pd.concat([df_merged, pd.read_pickle('df%s.pkl' % i)])

df_merged = df_merged.reset_index().drop('index', axis=1)

df_merged.to_pickle('merged.pkl')