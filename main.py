from data_func.api_getter import get_stock_data, store_stock_csv, store_stock_data_to_db

if __name__ == "__main__":
    data = get_stock_data()
    df = store_stock_csv(data)
    store_stock_data_to_db(df)
