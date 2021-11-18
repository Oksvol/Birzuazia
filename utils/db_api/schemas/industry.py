from sqlalchemy import Column, String, sql, BigInteger

from utils.db_api.db_gino import BaseModel


class Industry(BaseModel):
    __tablename__ = 'industries'
    id = Column(BigInteger, primary_key=True)
    code = Column(String(100))
    title = Column(String(100))

    query: sql.Select