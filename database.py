from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import conf
from urllib.parse import quote_plus

database_url = (
    f"mysql+pymysql://{conf['MYSQL_USER']}:{quote_plus(conf['MYSQL_PASSWORD'])}"
    f"@{conf['MYSQL_HOST']}:{conf['MYSQL_PORT']}/{conf['MYSQL_DB']}?charset=utf8mb4"
)

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
