from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user=""
password = ""
host = ""
dbname = "kontrol"
env = "local"

if env == "local":
    user = "root"
    host = "localhost"

if env == "container":
    user = "root"
    host = "host.docker.internal"


engine = create_engine(f'mysql://{user}:{password}@{host}:3306/{dbname}',pool_recycle=3600,pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autoflush=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
