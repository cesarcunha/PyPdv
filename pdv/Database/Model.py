from sqlalchemy import Column, Integer, String, inspect
from pdv.Database.database import Base


def object_as_dict(obj):
    if isinstance(obj, list):
        return [{c.key: getattr(item, c.key) for c in inspect(item).mapper.column_attrs} for item in obj]
    else:
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

    def as_dict(self):
        return object_as_dict(self)
