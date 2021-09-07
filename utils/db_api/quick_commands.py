from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.industry import Industry
from utils.db_api.schemas.operation import Operation
from utils.db_api.schemas.share import Share
from utils.db_api.schemas.user import User

#Пользователи
async def add_user(id: int, full_name: str, username: str = None, balance: float = None):
    try:
        user = User(id=id, full_name=full_name, username=username, balance=balance)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_username(id, username):
    user = await User.get(id)
    await user.update(username=username).apply()


#Отрасли
async def select_all_industries():
    industries = await Industry.query.gino.all()
    return industries

#Акции
async def select_all_shares():
    shares = await Share.query.gino.all()
    return shares


#Операции
async def select_all_operations():
    operations = await Operation.query.gino.all()
    return operations