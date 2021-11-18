from sqlalchemy import Text, Column, BigInteger, String, sql, Numeric, DateTime, SmallInteger

from utils.db_api.db_gino import BaseModel


class Bond(BaseModel):
    __tablename__ = 'bonds'
    id = Column(BigInteger, primary_key=True)
    tiker = Column(String(10))
    title = Column(String(100))
    description = Column(Text)
    body = Column(Numeric(10, 2))
    coupon = Column(Numeric(10, 2))
    price = Column(Numeric(10, 2))
    industry_id = Column(String(100))
    quantity = Column(BigInteger)

    query: sql.Select
