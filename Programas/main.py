from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.basketball-reference.com/leagues/NBA_2023_per_game.html'
URL2 = 'https://www.basketball-reference.com/contracts/players.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1", "Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)
page2 = requests.get(URL2, headers=headers)

info = BeautifulSoup(page.content, 'html.parser')
info2 = BeautifulSoup(page2.content, 'html.parser')

data = info.find_all(class_='full_table')
data2 = info2.find_all('tr', class_=None)

players=[]
for player in range(len(data)):
    player_stats=[]
    for stat in data[player].find_all('td'):
        player_stats.append(stat.text)
    players.append(player_stats)

salaries=[]
for salary in range(len(data2)):
    salary_info=[]
    for stat in data2[salary].find_all('td'):
        salary_info.append(stat.text)
    salaries.append(salary_info)

firstrow = info.find(class_='thead')

names=[]

for i in firstrow:
    names.append(firstrow.text)
st = names[0]

firstrow2=info2.find('tr', class_=None)

names2=[]

for i in firstrow2:
    names2.append(firstrow2.text)
st2 = names2[0]

clean_st = st.split('\n')

clean_st = clean_st[2:-1]

clean_st2 = st2.split('\n')
clean_st2 = clean_st2[2:-1]

full_stats = pd.DataFrame(players, columns=clean_st)
full_salaries = pd.DataFrame(salaries, columns=clean_st2)
del clean_st2[3:9]
del clean_st2[1]

#Tomamos sólo las variables necesarias y ordenamos el dataframe
salaries2023 = full_salaries.loc[:, ["Player", "2022-23"]]
final_salaries = pd.DataFrame(salaries2023, columns=clean_st2)
final_salaries.rename(columns = {'2022-23':'Salary'}, inplace = True)
final_salaries = final_salaries[1:]
final_salaries=final_salaries.sort_values(by=['Player'])
final_salaries=final_salaries.reset_index(drop=True)

#Cambiamos el formato de Salary
final_salaries['Salary']=final_salaries['Salary'].str.replace(r'\D', '',regex=True)

#Ordenamos el dataframe de estadísticas
full_stats_sorted=full_stats.sort_values(by=['Player'])
full_stats_sorted=full_stats_sorted.reset_index(drop=True)

#Dataframe final combinando los dos anteriores
final_df=pd.merge(full_stats_sorted, final_salaries, on='Player', how='left')

final_df.to_csv('stats/my_nba.csv', index=False)

