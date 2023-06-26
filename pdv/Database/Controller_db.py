from pdv.Database.database import Base, Session, engine
from pdv.Database.Model import User

# sBase.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)
session = Session()


def get_user(data):
    user = session.query(User).filter_by(username=data['username']).first()
    if user:
        print("olha ai o user", user.as_dict())
        return True
    return False
