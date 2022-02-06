
from sqlalchemy import Text, Column, BigInteger, String, sql, Numeric, Date

from utils.db_api.db_gino import TimedBaseModel


class News_Exchange(TimedBaseModel):
    __tablename__ = 'news_exchange'
    id = Column(BigInteger, primary_key=True)
    tiker = Column(String(10))
    change = Column(Numeric(3, 2))
    text = Column(Text)
    public_date = Column(Date)
    status = Column(String(15))

    query: sql.Select