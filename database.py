from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import URL, create_engine

url = URL.create(
    drivername="mysql+pymysql",
    username="User_name",
    password="Your_mysql_password",
    host="Your_host",
    port=3306,
    database="Database_name",
)
print(url)

engine = create_engine(url)

SessionLocal = sessionmaker(bind=engine)

