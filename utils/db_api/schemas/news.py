from sqlalchemy import Column, BigInteger, String, sql, Numeric, DateTime, Text

from utils.db_api.db_gino import TimedBaseModel


class News(TimedBaseModel):
    __tablename__ = 'news'
    id = Column(BigInteger, primary_key=True)
    tiker = Column(String(10))
    type = Column(String(25))
    industry_id = Column(String(100))
    text = Column(Text())

    query: sql.Select