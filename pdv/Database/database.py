from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:Sys%40dmin@localhost:5432/otmapdv', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
