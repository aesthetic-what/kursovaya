from PySide6.QtWidgets import (QMainWindow, QListWidgetItem, QMessageBox, 
                               QWidget, QLabel, QPushButton, QHBoxLayout, 
                               QInputDialog)
from PySide6.QtCore import Qt, QSize, QByteArray
from PySide6.QtGui import QPixmap
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from windows.ui.shop_win import Ui_ShopWindow
from windows.edit_manager import EditProfile
from windows.cart import CartWindow
from windows.widgets import ListItemWidget

from db.query.users import add_to_cart

from db.models.products import Products
from db.models.cart import Cart
from db.models.cart_item import CartItem
from db.models.users import Users
from db.db_core import local_session
        

class ShopWindow(QMainWindow):
    def __init__(self, login: str, photo: bytes | None = None):
        super().__init__()
        self.ui = Ui_ShopWindow()
        self.ui.setupUi(self)
        
        # Пагинация
        self.items_per_page = 10
        self.current_page = 0
        print("-"*30, self.current_page + 1, "-"*30)
        
        # Кнопки управления
        self.ui.searcn_button.clicked.connect(self.search_prod)
        self.ui.sort_box.currentIndexChanged.connect(self.sort_products)
        self.ui.prev_button.clicked.connect(self.prev_page)
        self.ui.next_button.clicked.connect(self.next_page)
        self.ui.logout_button.clicked.connect(self.logout)
        self.ui.edit_profile_button.clicked.connect(self.edit_profile)
        self.ui.listWidget.itemDoubleClicked.connect(self.add_to_cart)
        self.ui.cart_button.clicked.connect(self.open_cart)
        
        # Константы и инициализация просцессов при запуске
        self.login = login
        self.load_products()
        self.ui.login.setText(login)
        self.user_info = self.get_info()
        
    
    def get_info(self) -> Users:
        session = local_session()
        try:
            user_info = session.scalar(select(Users).where(Users.login == self.login))
            return user_info
        except Exception as ex:
            QMessageBox(self, 'Ошибка', f'Произошла невиданная ошибка\n{ex}')
        finally:
            session.close()


    def open_cart(self):
        self.cart_win = CartWindow(self.user_info.id)
        self.cart_win.setFixedSize(959, 600)
        self.cart_win.show()


    def logout(self):
        from windows.auth import LoginWindow
        self.login_win = LoginWindow()
        self.login_win.show()
        self.login_win.setFixedSize(362, 226)
        self.close()
        
    def edit_profile(self):
        self.edit_win = EditProfile(self.login)
        self.edit_win.profileUpdated.connect(self.update_profile)
        self.edit_win.setFixedSize(879, 438)
        self.edit_win.show()
        
    def update_profile(self):
        """Обновляет данные профиля в главном окне"""
        session = local_session()
        try:
            # Получаем обновленные данные пользователя из базы
            user = session.query(Users).filter(Users.login == self.login).first()
            
            if user:
                # Обновляем UI (замените на свои элементы интерфейса)
                self.ui.login.setText(user.login)

                # Если есть фото, отображаем его
                if user.photo:
                    pixmap = QPixmap()
                    pixmap.loadFromData(user.photo)
                    self.ui.image_user.setPixmap(pixmap)
                
                print("Профиль обновлен в интерфейсе.")

        except Exception as ex:
            QMessageBox.warning(self, "Ошибка", f"Не удалось обновить профиль: {ex}")
            print(f"Ошибка при обновлении профиля: {ex}")

        finally:
            session.close()
    
    def load_products(self):
        self.ui.listWidget.clear()
        session = local_session()
        
        offset = self.current_page * self.items_per_page
        products = session.execute(
            select(Products).limit(self.items_per_page).offset(offset)
        ).scalars().all()
        
        # products = session.execute(select(Products)).scalars().all()
        for product in products:
            item_text = f"Название: {product.name}\nОписание: {product.description}\nТип: {product.type}\nЦена: {product.price}\nКоличество: {product.quantity}"
            widget = ListItemWidget(item_text, self.ui.listWidget, product.price)
            item = QListWidgetItem()
            item.setData(Qt.UserRole, {
            "name": product.name,
            "product_id": product.id,
            "price": product.price,
            "quantity": product.quantity,
            "type": product.type
            })
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)
            item.setSizeHint(QSize(600, 200))
        session.close()
        
        self.update_navigation_buttons()
        
    def search_prod(self):
        # print('search prod')
        self.ui.listWidget.clear()
        search_term = self.ui.searchbar.text()

        session = local_session()
        offset = self.current_page * self.items_per_page

        # Фильтруем товары по `name` или `description` с учетом лимита и оффсета
        products = session.execute(
            select(Products)
            .where(Products.name.ilike(f"%{search_term}%"))
            .limit(self.items_per_page)
            .offset(offset)
        ).scalars().all()

        for product in products:
            item_text = f"Название: {product.name}\nОписание: {product.description}\nКоличество: {product.quantity}"
            print(f"{item_text}")
            print("="*50)
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, product)  # Сохраняем всю информацию о продукте
            self.ui.listWidget.addItem(item)
            item.setSizeHint(QSize(600, 100))

        session.close()
        # print('end search')
        self.update_navigation_buttons()  # Обновляем кнопки пагинации

            
    def sort_products(self, index: int):
        if index == 0:
            self.load_products()
        elif index == 1:
            self.ui.listWidget.sortItems(Qt.SortOrder.AscendingOrder)
        elif index == 2:
            self.ui.listWidget.sortItems(Qt.SortOrder.DescendingOrder)
    
    
    def add_to_cart(self, item):
        product_data = item.data(Qt.UserRole)  # Извлекаем данные о товаре
        
        if product_data:
            user_id = self.user_info.id  # ID текущего пользователя
            product_id = product_data["product_id"]
            name = product_data["name"]
            price = product_data["price"]
            available_quantity = product_data["quantity"]  # Доступное количество товара

            # Открываем диалог для ввода количества
            quantity, ok = QInputDialog.getInt(
                self,
                "Выбор количества",
                f"Введите количество товара (доступно {available_quantity} шт.):",
                minValue=1,  
                maxValue=available_quantity,  # Ограничение по количеству товара
            )

            if ok and quantity > 0:  # Проверяем, что пользователь не отменил ввод
                session = local_session()
                try:
                    # Проверяем, есть ли у пользователя активная корзина
                    cart = session.query(Cart).filter(
                        Cart.user_id == user_id,
                        Cart.status == "awaiting payment"
                    ).first()

                    if not cart:
                        # Создаём новую корзину
                        cart = Cart(
                            user_id=user_id,
                            status="awaiting payment",
                            created_at=datetime.utcnow()
                        )
                        session.add(cart)
                        session.commit()
                        session.refresh(cart)

                    # Проверяем, есть ли товар уже в корзине
                    cart_item = session.query(CartItem).filter(
                        CartItem.cart_id == cart.id,
                        CartItem.product_id == product_id
                    ).first()

                    if cart_item:
                        # Если товар уже есть в корзине - обновляем количество
                        cart_item.product_count += quantity
                        cart_item.summary = cart_item.product_count * price
                    else:
                        # Добавляем новый товар в корзину
                        cart_item = CartItem(
                            cart_id=cart.id,
                            product_id=product_id,
                            product_count=quantity,
                            summary=quantity * price
                        )
                        session.add(cart_item)

                    # Уменьшаем количество товара в базе
                    product = session.query(Products).filter(Products.id == product_id).first()
                    if product:
                        if product.quantity < quantity:
                            QMessageBox.warning(self, "Ошибка", f"Недостаточно товара на складе!")
                            return
                        
                        product.quantity -= quantity  # Уменьшаем количество на складе

                    session.commit()

                    # Обновляем список товаров в магазине
                    self.load_products()

                    QMessageBox.information(self, "Добавлено", f"{quantity} шт. товара '{name}' добавлено в корзину!")

                except SQLAlchemyError as e:
                    session.rollback()
                    QMessageBox.critical(self, "Ошибка", f"Ошибка при добавлении товара: {str(e)}")
                finally:
                    session.close()
    
    
    def update_navigation_buttons(self):
        """Обновление состояния кнопок навигации"""
        session = local_session()
        total_products = session.execute(select(func.count(Products.id))).scalar()  # Общее количество продуктов
        session.close()

        # Проверка для активации/деактивации кнопок
        self.ui.prev_button.setEnabled(self.current_page > 0)
        self.ui.next_button.setEnabled((self.current_page + 1) * self.items_per_page < total_products)

    def prev_page(self):
        """Переход на предыдущую страницу"""
        if self.current_page > 0:
            self.current_page -= 1
            self.ui.label.setText(f"Страница: {self.current_page + 1}")
            print("-"*30, self.current_page + 1, "-"*30)
            self.load_products()

    def next_page(self):
        """Переход на следующую страницу"""
        self.current_page += 1
        self.ui.label.setText(f"Страница: {self.current_page + 1}")
        print("-"*30, self.current_page + 1, "-"*30)
        self.load_products()
