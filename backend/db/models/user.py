from db.base import Base
from sqlalchemy import Column, Integer, TEXT


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(TEXT, unique=True, index=True, nullable=False)
    name = Column(TEXT, nullable=False)
    cognito_sub = Column(TEXT, unique=True, index=True, nullable=False)
