import pandas as pd
from sklearn.linear_model import Ridge

import model

nba = pd.read_csv("stats/my_nba.csv", index_col="Player")
nba = nba.dropna()

correlation = nba.corr()
print(correlation)

rr = Ridge(alpha=0.1)

predictors = nba.columns[~nba.columns.isin(["Player", "Pos", "Tm", "Salary"])]

def backtest(nba, model, predictors, start=1, step=50):
    all_predictions=[]
    for i in range(start, nba.shape[0], step):
        train = nba.iloc[:i, :]
        test = nba.iloc[i:(i+step), :]

        model.fit(train[predictors], train["Salary"])

        preds = model.predict(test[predictors])

        preds = pd.Series(preds, index = test.index)
        combined = pd.concat([test["Salary"], preds], axis=1)

        combined.columns = ["actual", "prediction"]
        combined["difference"] = (combined["prediction"]-combined["actual"]).abs()

        all_predictions.append(combined)
    return pd.concat(all_predictions)

predictions = backtest(nba, rr, predictors)

from sklearn.metrics import mean_absolute_error

print(mean_absolute_error(predictions["actual"], predictions["prediction"]).__round__(ndigits=0))











