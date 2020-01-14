from sqlalchemy import Column,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(30))

engine = create_engine('mysql+pymysql://root:123456@10.0.3.4:30306/testdb')
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
