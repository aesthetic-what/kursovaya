from db.db_core import local_session, init_db
from db.models.products import Products
from faker import Faker
from random import randint

# Инициализация Faker
fake = Faker()

def generate_fake_products(n: int):
    """Генерирует n фейковых товаров и добавляет их в базу данных."""
    init_db()
    session = local_session()
    try:
        fake_products = [
            Products(
                name=fake.word(),
                description=fake.sentence(50),
                type=fake.word(),
                importer=fake.company(),
                quantity=fake.random_int(min=1, max=1000),
                price=randint(100, 99999),
                date_add=fake.date_this_year()
            )
            for _ in range(n)
        ]
        session.add_all(fake_products)
        session.commit()
        print(f"Добавлено {n} фейковых товаров.")
    except Exception as ex:
        session.rollback()
        print(f"Ошибка при добавлении товаров: {ex}")
    finally:
        session.close()

# Запуск генерации
if __name__ == "__main__":
    generate_fake_products(50)