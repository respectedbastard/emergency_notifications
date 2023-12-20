from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.auth.config import DB_HOST, DB_PORT, DB_NAME, DB_PASSWORD, DB_USER
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()


