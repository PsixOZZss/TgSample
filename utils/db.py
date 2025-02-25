from peewee import SqliteDatabase, Model, IntegerField, CharField

# Подключение к базе данных
db = SqliteDatabase("database.db")


# Определение базовой модели
class BaseModel(Model):
    class Meta:
        database = db


# Модель пользователя
class User(BaseModel):
    user_id = IntegerField(unique=True)  # Уникальный идентификатор пользователя
    username = CharField()  # Имя пользователя


# Класс для работы с базой данных
class Database:
    def __init__(self, db_name="database.db"):
        # Инициализация базы данных
        self.db = SqliteDatabase(db_name)
        self.create_table()

    def create_table(self):
        # Создание таблицы, если она не существует
        self.db.connect()
        self.db.create_tables([User])

    def add_user(self, user_id, username):
        # Добавление пользователя в базу данных
        try:
            User.create(user_id=user_id, username=username)
        except Exception:
            # Если пользователь уже существует (например, нарушение уникальности),
            # исключение будет проигнорировано
            pass


# Пример использования
if __name__ == "__main__":
    db_manager = Database()
    db_manager.add_user(12345, "john_doe")
