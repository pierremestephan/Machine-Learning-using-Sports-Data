import numpy as np
import pandas as pd
import requests
import json

def metrics(df, y_pred):
    df.loc[:, 'HomeWinPerc'] = y_pred[0]
    df.loc[:, 'DrawPerc'] = y_pred[1]
    df.loc[:, 'AwayPerc'] = y_pred[2]

    df = df.dropna()

    conditions = [
        (df['HomeWinPerc'] >= df['DrawPerc']) & (df['HomeWinPerc'] >= df['AwayPerc']), #Home Condition
        (df['HomeWinPerc'] <= df['DrawPerc']) & (df['DrawPerc'] >= df['AwayPerc']), #Draw Condition
        (df['HomeWinPerc'] <= df['AwayPerc']) & (df['DrawPerc'] <= df['AwayPerc']) #Away Condition
    ]

    values = [0,1,2]

    df["PredResult"] = np.select(conditions, values)
    df['Comparison'] = np.where(df["FTR"] == df["PredResult"], True, False)

    print((df['Comparison'].value_counts()/df['Comparison'].count())*100)
    print((df['FTR'].value_counts()/df['FTR'].count())*100)
    print((df['PredResult'].value_counts()/df['PredResult'].count())*100)

    