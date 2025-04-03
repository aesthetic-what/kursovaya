from db.models.users import Users
from db.models.products import Products
from db.models.cart import Cart
from db.models.cart_item import CartItem
from db.db_core import local_session
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


def add_to_cart(user_id: int, product_id: int, quantity: int, price: int):
    """
    Добавляет товар в корзину пользователя.
    
    Аргументы:
        user_id (int): ID пользователя.
        product_id (int): ID товара.
        quantity (int): Количество товара.
        price (int): Цена за единицу товара.

    Возвращает:
        CartItem: добавленный или обновленный товар в корзине.
    """
    session = local_session()
    try:
        # Проверяем, есть ли у пользователя активная корзина
        cart = session.query(Cart).filter(
            Cart.user_id == user_id,
            Cart.status == "awaiting payment"
        ).first()

        # Если корзины нет, создаём новую
        if not cart:
            cart = Cart(
                user_id=user_id,
                status="awaiting payment",
                created_at=datetime.utcnow()
            )
            session.add(cart)
            session.commit()  # Сохраняем, чтобы получить ID корзины
            session.refresh(cart)

        # Проверяем, есть ли этот товар уже в корзине
        cart_item = session.query(CartItem).filter(
            CartItem.cart_id == cart.id,
            CartItem.product_id == product_id
        ).first()

        if cart_item:
            # Если товар уже есть, увеличиваем его количество и обновляем сумму
            cart_item.product_count += quantity
            cart_item.summary = cart_item.product_count * price
        else:
            # Если товара нет в корзине, создаем новую запись
            cart_item = CartItem(
                cart_id=cart.id,
                product_id=product_id,
                product_count=quantity,
                summary=quantity * price
            )
            session.add(cart_item)

        session.commit()
        return cart_item

    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Ошибка при добавлении товара в корзину: {str(e)}")
    finally:
        session.close()
