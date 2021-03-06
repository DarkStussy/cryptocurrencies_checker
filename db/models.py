from sqlalchemy import Column, Float, BigInteger, Boolean

from .base import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True, unique=True)
    btc_value = Column(Float, nullable=True)
    eth_value = Column(Float, nullable=True)
    bnb_value = Column(Float, nullable=True)
    dot_value = Column(Float, nullable=True)
    difference_btc = Column(Float, nullable=True)
    difference_eth = Column(Float, nullable=True)
    difference_bnb = Column(Float, nullable=True)
    difference_dot = Column(Float, nullable=True)
    is_checked_btc = Column(Boolean, default=False)
    is_checked_eth = Column(Boolean, default=False)
    is_checked_bnb = Column(Boolean, default=False)
    is_checked_dot = Column(Boolean, default=False)
