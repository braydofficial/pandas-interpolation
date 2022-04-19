import pandas as pd

df = pd.read_csv('./data.csv', sep=';')

df['Jan'] = df['Jan'].interpolate(method='linear', axis=0)
print('\n\nJan: \n')
print(df['Jan'])

df['Feb'] = df['Feb'].interpolate(method='linear', axis=0)
print('\n\nFeb: \n')
print(df['Feb'])

df['Mar'] = df['Mar'].interpolate(method='linear', axis=0)
print('\n\nMar: \n')
print(df['Mar'])