from sqlalchemy import Column, String, sql

from utils.db_api.db_gino import BaseModel


class Industry(BaseModel):
    __tablename__ = 'industries'
    code = Column(String(100))
    title = Column(String(100))

    query: sql.Select