import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

nba = pd.read_csv("stats/my_nba.csv")
nba_cat = pd.read_csv("stats/my_nba_categorical.csv")

fig, axs = plt.subplots(3, 2, figsize=(10, 10))

sns.histplot(data=nba, x="PTS", kde=True, color="skyblue", ax=axs[0, 0])
sns.histplot(data=nba, x="Salary", kde=True, color="olive", ax=axs[0, 1])
sns.histplot(data=nba, x="MP", kde=True, color="gold", ax=axs[1, 0])
sns.histplot(data=nba, x="3P", kde=True, color="teal", ax=axs[1, 1])
sns.histplot(data=nba, x="Pos", kde=True, color="teal", ax=axs[2, 0])
sns.histplot(data=nba, x="Age", kde=True, color="teal", ax=axs[2, 1])

plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

sns.boxplot(x=nba_cat["Salary"], y=nba_cat["PTS"], ax=axs[0,0])
sns.boxplot(x=nba_cat["Salary"], y=nba_cat["3P"], ax=axs[0,1])
sns.boxplot(x=nba_cat["Salary"], y=nba_cat["FG"], ax=axs[1,0])
sns.boxplot(x=nba_cat["Salary"], y=nba_cat["AST"], ax=axs[1,1])

plt.show()

ast = nba_cat.AST > 10
print(nba_cat[ast])

sns.lmplot(x="PTS", y="MP", data=nba_cat, fit_reg=False, hue='Salary', legend=True)
plt.show()

inf = nba_cat.PTS < 5
nba_cat = nba_cat[inf]
mns = nba_cat.MP > 25
print(nba_cat[mns])

