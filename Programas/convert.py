import pandas as pd

nba = pd.read_csv("stats/my_nba.csv")
media = nba.Salary.mean()

encMedia = nba.Salary > media
debMedia = nba.Salary <= media

nba.Salary[encMedia] = 'Above mean'
nba.Salary[debMedia] = 'Below mean'

nba.to_csv('stats/my_nba_categorical.csv', index=False)
