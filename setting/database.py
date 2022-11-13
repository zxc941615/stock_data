import psycopg2
from sqlalchemy import create_engine
from setting.config import DB_USER, DB_PASSWORD, DB_PORT, DB_HOST, DB_DATABASE

db = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
)


def get_db():
    try:
        return db
    except Exception as e:
        print(e)
        return e
