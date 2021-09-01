from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')  # Забираем значение типа str
ADMINS = env.list('ADMINS')  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста


banned_users = [2134876231, 237492138764]

allowed_users = []

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")