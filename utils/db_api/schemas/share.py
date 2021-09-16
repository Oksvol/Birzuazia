from sqlalchemy import Text, Column, BigInteger, String, sql, Numeric, DateTime, SmallInteger

from utils.db_api.db_gino import BaseModel


class Share(BaseModel):
    __tablename__ = 'shares'
    id = Column(BigInteger, primary_key=True)
    tiker = Column(String(10))
    title = Column(String(100))
    description = Column(Text)
    price = Column(Numeric(10, 2))
    industry_id = Column(String(100))
    quantity = Column(BigInteger)

    query: sql.Select
    def __repr__(self):
        return f"""
        Тикер: {self.tiker}
        Цена: {self.price}
        ''
        {self.description}"""