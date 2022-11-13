import requests
import pandas as pd
from IPython.display import display
from datetime import date, timedelta
from setting.config import API_TOKEN, API_ENDPOINT, Parameter
from setting.database import get_db

params = Parameter(
    dataset="TaiwanStockPrice",
    # start_date=(date.today() - timedelta(days=5)).strftime("%Y-%m-%d"),
    start_date=(date.today() - timedelta(days=365)).strftime("%Y-%m-%d"),
    end_date=date.today().strftime("%Y-%m-%d"),
    data_id="2330",
    token=API_TOKEN,
)
table_name = "stock_price"


def get_stock_data():
    data = requests.get(API_ENDPOINT, params=params.get_param()).json()
    return data


def store_stock_csv(data):
    df = pd.DataFrame(data["data"])
    df.to_csv(f"{params.data_id}_price.csv", index=False)
    return df


def store_stock_data_to_db(dataframe):
    dataframe.to_sql(name=table_name, con=get_db(), index=False, if_exists="append")
