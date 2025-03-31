from db.models.users import Users
from db.models.products import Products
from db.models.cart import Cart
from sqlalchemy import or_
from db.db_core import local_session



def get_books(search_term=None):
    """Получает список товаров из базы данных, поддерживает поиск по названию, автору и жанру."""
    session = local_session()
    try:
        query = session.query(Products)
        
        if search_term:
            search_pattern = f"%{search_term}%"
            query = query.filter(
                or_(Products.name.like(search_pattern),
                    Products.importer.like(search_pattern))
            )
        
        products = query.all()
        return products
    except Exception as ex:
        print(f"Ошибка получения товаров: {ex}")
        return []
    finally:
        session.close()