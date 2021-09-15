from sqlalchemy import Column, BigInteger, String, sql, Numeric, DateTime

from utils.db_api.db_gino import TimedBaseModel


class Operation(TimedBaseModel):
    __tablename__ = 'operations'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(String(255))
    tiker = Column(String(10))
    type = Column(String(10))
    quantity = Column(BigInteger)
    industry_id = Column(String(100))
    price = Column(Numeric(10, 2))

    query: sql.Select