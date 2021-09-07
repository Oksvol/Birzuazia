from sqlalchemy import Column, BigInteger, String, sql, Numeric, DateTime

from utils.db_api.db_gino import TimedBaseModel


class Operation(TimedBaseModel):
    __tablename__ = 'operations'
    user_id = Column(BigInteger, primary_key=True)
    tiker = Column(String(10))
    quantity = Column(BigInteger)
    industry_id = Column(String(100))
    price = Column(Numeric(10, 2))
    last_pay = Column(DateTime(True))

    query: sql.Select