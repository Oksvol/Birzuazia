from sqlalchemy import Integer, Column, BigInteger, String, sql, Numeric, DateTime, SmallInteger

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    full_name = Column(String(100))
    username = Column(String(100))
    balance = Column(Numeric(10, 2))
    last_pay = Column(DateTime(True))
    pay_mode = (SmallInteger)

    referral = Column(BigInteger)

    query: sql.Select