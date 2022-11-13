API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMi0xMS0xMiAyMzo1MjozMyIsInVzZXJfaWQiOiJ6eGM5NDE2MTUiLCJpcCI6IjI3LjEyMi4xNC43NiJ9.y6sapGn3hC9wbvzRHa1NDcn4wRpN76oi6qPxuRk6hyI"
API_ENDPOINT = "https://api.finmindtrade.com/api/v4/data?"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_DATABASE = "stock_data"


class Parameter:
    def __init__(self, dataset, data_id, start_date, end_date, token):
        self.dataset = dataset
        self.data_id = data_id
        self.start_date = start_date
        self.end_date = end_date
        self.token = token

    def get_param(self):
        return {
            "dataset": self.dataset,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "data_id": self.data_id,
            "token": self.token,
        }


# API Parameter Descriptions
# dataset	資料集名稱
# data_id	資料代碼，例如股票、期貨、選擇權代碼
# start_date	起始時間
# end_date	結束時間
# token	金鑰
