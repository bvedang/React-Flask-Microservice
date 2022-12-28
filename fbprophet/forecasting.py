import pandas as pd
from pandas import  DataFrame
# from repositories import Repository
import prophet
from prophet import Prophet

csvfileLocation = "./csvfiles/"

def commitPullsReleaseForecast(type:str,name:str):
    model = Prophet(yearly_seasonality=True, daily_seasonality=True)
    df = pd.read_csv(csvfileLocation+ name+type+".csv",names=["ds","y"])
    df["ds"] = pd.to_datetime(df["ds"])
    df["ds"] = pd.Series([val.date() for val in df["ds"]])
    df = df.dropna()
    if df.shape[0]<2:
        return None
    model.fit(df)
    future_prediction = model.make_future_dataframe(periods=365)
    forecast = model.predict(future_prediction)
    model.plot(forecast).savefig("./assests/"+name+type+'_forecast.png')
    return name+type+'_forecast.png'


def forecast(type:str,name:str,repo:DataFrame):
    model = Prophet(yearly_seasonality=True, daily_seasonality=True)
    df = repo.copy()
    df.columns = ['ds', 'y']
    model.fit(df)
    future_prediction = model.make_future_dataframe(periods=365)
    forecast = model.predict(future_prediction)
    model.plot_components(forecast).savefig("./assests/"+name+type+'_forecast.png')
    return name+type+'_forecast.png'