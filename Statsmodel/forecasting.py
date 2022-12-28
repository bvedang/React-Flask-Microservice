from pandas import DataFrame
import pandas as pd
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.tsa.seasonal import seasonal_decompose

csvfileLocation = "./csvfiles/"


def statsForecast(forecastOf: str, name: str, repo: DataFrame) -> str:
    df = repo.copy()
    df.columns = ['ds', 'y']
    df.set_index('y')
    predict = sm.tsa.seasonal_decompose(df.index, period=15)
    figure = predict.plot()
    figure.set_size_inches(15, 8)
    figure.savefig("./assests/"+"statsObserved" +
                   name+forecastOf+'_forecast.png')
    df2 = df
    model = sm.tsa.ARIMA(df2['y'].iloc[1:], order=(1, 0, 0))
    results = model.fit()
    df2['forecast'] = results.fittedvalues
    fig = df2[['y', 'forecast']].plot(figsize=(16, 12)).get_figure()
    fig.savefig("./assests/"+"stat"+name+forecastOf+'_forecast.png')
    return +"stat"+name+forecastOf+'_forecast.png'


def statsForecastCommitsPullsRelease(forecastOf: str, name: str) -> str:
    df = pd.read_csv(csvfileLocation+name+forecastOf+".csv", names=["ds", "y"])
    df["ds"] = pd.to_datetime(df["ds"])
    df["ds"] = pd.Series([val.date() for val in df["ds"]])
    df = df.dropna()
    df.set_index('y')
    predict = sm.tsa.seasonal_decompose(df.index, period=15)
    figure = predict.plot()
    figure.set_size_inches(15, 8)
    figure.savefig("./assests/"+"statsObserved" +
                   name+forecastOf+'_forecast.png')
    df2 = df
    model = sm.tsa.ARIMA(df2['y'].iloc[1:], order=(1, 0, 0))
    results = model.fit()
    df2['forecast'] = results.fittedvalues
    fig = df2[['y', 'forecast']].plot(figsize=(16, 12)).get_figure()
    fig.savefig("./assests/"+"stat"+name+forecastOf+'_forecast.png')
    return "stat"+name+forecastOf+'_forecast.png'
