
from sqlalchemy import Text, Column, BigInteger, String, sql, DateTime, Date

from utils.db_api.db_gino import TimedBaseModel


class News_Global(TimedBaseModel):
    __tablename__ = 'news_global'
    id = Column(BigInteger, primary_key=True)
    tiker = Column(String(10))
    type = Column(String(25))
    text = Column(Text)
    public_date = Column(Date)
    status = Column(String(15))

    query: sql.Select

