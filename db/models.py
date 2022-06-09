from sqlalchemy import Column, Float, BigInteger

from .base import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True, unique=True)
    btc_value = Column(Float, nullable=True)
    eth_value = Column(Float, nullable=True)
