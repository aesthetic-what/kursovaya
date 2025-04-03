from PySide6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from PySide6.QtCore import QSize, Qt

from db.models.cart_item import CartItem
from db.models.cart import Cart
from db.db_core import local_session

from windows.ui.cart import Ui_MainWindow
from windows.widgets import ListItemWidget

from sqlalchemy.exc import SQLAlchemyError

class CartWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.buy_all.clicked.connect(self.buy_all)
        self.ui.cart_list.itemDoubleClicked.connect(self.purchase_item)
        
        self.load_cart_items(user_id)
        
        self.user_id = user_id
        
    def buy_all(self):
        """
        Покупает все товары в корзине пользователя, меняя статус корзины на 'paid'.
        
        Аргументы:
            user_id (int): ID пользователя.
        """
        session = local_session()
        
        try:
            # Получаем активную корзину пользователя
            cart = session.query(Cart).filter(
                Cart.user_id == self.user_id,
                Cart.status == "awaiting payment"
            ).first()

            if not cart or not cart.items:
                QMessageBox.information(self, "Покупка", "Ваша корзина пуста.")
                return

            # Меняем статус корзины на "paid"
            cart.status = "paid"
            session.commit()
            
            # Очищаем UI
            self.ui.cart_list.clear()
            QMessageBox.information(self, "Покупка", "Все товары успешно куплены!")

        except SQLAlchemyError as e:
            session.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка при покупке товаров: {str(e)}")

        finally:
            session.close()
        
        
    def purchase_item(self, item: QListWidgetItem):
        """
        Покупает выбранный товар из корзины (удаляет его).
        
        Аргументы:
            item (QListWidgetItem): Элемент списка, содержащий товар.
        """
        session = local_session()
        
        try:
            product_data = item.data(Qt.UserRole)  # Получаем данные товара
            if not product_data:
                return

            user_id = self.user_id
            product_id = product_data["product_id"]

            # Получаем активную корзину пользователя
            cart = session.query(Cart).filter(
                Cart.user_id == user_id,
                Cart.status == "awaiting payment"
            ).first()

            if not cart:
                QMessageBox.information(self, "Корзина", "Ошибка: корзина не найдена.")
                return

            # Ищем товар в корзине
            cart_item = session.query(CartItem).filter(
                CartItem.cart_id == cart.id,
                CartItem.product_id == product_id
            ).first()

            if not cart_item:
                QMessageBox.information(self, "Корзина", "Товар уже был удалён.")
                return

            # Удаляем товар
            session.delete(cart_item)
            session.commit()

            # Обновляем список
            self.load_cart_items(user_id)
            QMessageBox.information(self, "Покупка", "Товар успешно куплен!")

        except SQLAlchemyError as e:
            session.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка при покупке товара: {str(e)}")

        finally:
            session.close()

        
    def load_cart_items(self, user_id: int) -> QListWidgetItem:
        """
        Загружает список товаров из корзины пользователя и отображает их в QListWidget.

        Аргументы:
            user_id (int): ID пользователя.
        """
        self.ui.cart_list.clear()  # Очищаем список перед загрузкой
        session = local_session()
        
        try:
            # Получаем активную корзину пользователя
            cart = session.query(Cart).filter(
                Cart.user_id == user_id,
                Cart.status == "awaiting payment"
            ).first()

            if not cart:
                QMessageBox.information(self, "Корзина", "Ваша корзина пуста.")
                return

            # Получаем все товары из корзины
            cart_items = session.query(CartItem).filter(CartItem.cart_id == cart.id).all()

            if not cart_items:
                QMessageBox.information(self, "Корзина", "Ваша корзина пуста.")
                return

            # Добавляем товары в список
            for item in cart_items:
                product = item.product  # SQLAlchemy relationship
                item_text = (f"Название: {product.name}\n"
                            f"Количество: {item.product_count}\n"
                            f"Цена за шт: {product.price}\n"
                            f"Общая стоимость: {item.summary}")
                
                widget = ListItemWidget(item_text, self.ui.cart_list, product.price)
                list_item = QListWidgetItem()
                # Сохраняем данные о товаре
                list_item.setData(Qt.UserRole, {
                    "product_id": product.id,
                    "product_name": product.name,
                    "quantity": item.product_count,
                    "price": product.price,
                    "summary": item.summary
                })
                self.ui.cart_list.addItem(list_item)
                self.ui.cart_list.setItemWidget(list_item, widget)
                list_item.setSizeHint(QSize(600, 150))

        except SQLAlchemyError as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при загрузке корзины: {str(e)}")

        finally:
            session.close()