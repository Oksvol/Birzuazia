from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')  # Забираем значение типа str
ADMINS = env.list('ADMINS')  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

allowed_users = []

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")

PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
PGNAME = env.str("PGNAME")

POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"