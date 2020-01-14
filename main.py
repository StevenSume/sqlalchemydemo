from sqlalchemy import Column,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(30))

engine = create_engine('mysql+mysqlconnector://root:123456@10.0.3.4:30306/testdb')
DBSession = sessionmaker(bind=engine)
count = 0
while(True):
    session = DBSession()
    new_user = User(id=String(count),name=String('james' + count))
    session.add(new_user)
    session.commit()
    user = session.query(User).filter(User.id==String(count)).one()
    print(user.name)
    session.close()
    count=count+1