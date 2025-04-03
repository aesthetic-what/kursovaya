from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QWidget, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QSize, QByteArray
from PySide6.QtGui import QPixmap
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from windows.ui.shop_win import Ui_ShopWindow
from windows.edit_manager import EditProfile

from db.models.products import Products
from db.models.cart import Cart
from db.models.cart_item import CartItem
from db.models.users import Users
from db.db_core import local_session


class ListItemWidget(QWidget):
    """Кастомный элемент списка: картинка + текст + кнопка"""
    def __init__(self, image_data: bytes | None, text: str, parent_list, price: str):
        super().__init__()

        self.parent_list = parent_list  # Сохраняем ссылку на QListWidget
        self.setStyleSheet("""
                QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """)

        # Картинка (если нет данных, загружаем "default.png")
        self.image_label = QLabel()
        pixmap = QPixmap()
        if image_data:
            pixmap.loadFromData(QByteArray(image_data))
        else:
            pixmap.load("default.png")  # Файл-заглушка

        # Масштабируем картинку
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(pixmap)

        # Название товара
        self.text_label = QLabel(text)
        self.text_label.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 12px;
            }
        """)

        # Кнопка "Купить"
        self.button = QPushButton("В корзину")
        self.button.clicked.connect(self.buy_item)  # Привязываем функцию

        # Размещение элементов в строку
        layout = QHBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def buy_item(self):
        """
        Добавляет товар в корзину пользователя.
        
        Параметры:
            user_id (int): ID пользователя
            product_id (int): ID товара
            quantity (int): количество товара
            price (int): цена за единицу товара
        
        Возвращает:
            CartItem: добавленный товар в корзине
        """
        session = local_session()
        try:
            # Проверяем, есть ли у пользователя активная корзина
            корзина = session.query(Cart).filter(
                Cart.user_id == user_id,
                Cart.status == "awaiting payment"
            ).first()
            
            # Если нет активной корзины - создаем новую
            if not корзина:
                корзина = Cart(
                    user_id=user_id,
                    status="awaiting payment",
                    created_at=datetime.utcnow()
                )
                session.add(корзина)
                session.commit()
                session.refresh(корзина)
            
            # Проверяем, есть ли уже такой товар в корзине
            товар_в_корзине = session.query(CartItem).filter(
                CartItem.cart_id == корзина.id,
                CartItem.product_id == product_id
            ).first()
            
            if товар_в_корзине:
                # Если товар уже есть - обновляем количество и сумму
                товар_в_корзине.product_count += quantity
                товар_в_корзине.summary = товар_в_корзине.product_count * price
            else:
                # Если товара нет - создаем новую запись
                товар_в_корзине = CartItem(
                    cart_id=корзина.id,
                    product_id=product_id,
                    product_count=quantity,
                    summary=quantity * price
                )
                session.add(товар_в_корзине)
            
            session.commit()
            return товар_в_корзине
            
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Ошибка при добавлении товара в корзину: {str(e)}")
        finally:
            session.close()

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
        
        # Константы и инициализация просцессов при запуске
        self.login = login
        self.photo = photo
        self.load_products()
        self.ui.login.setText(login)
        self.user_info = self.get_info()
        if photo:
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(photo))
            label_size = self.ui.image_user.size()  # Получаем размеры QLabel
            pixmap = pixmap.scaled(label_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.ui.image_user.setPixmap(pixmap)
        
    
    def get_info(self) -> Users:
        session = local_session()
        try:
            user_info = session.scalar(select(Users).where(Users.login == self.login))
            return user_info
        except Exception as ex:
            QMessageBox(self, 'Ошибка', f'Произошла невиданная ошибка\n{ex}')
        finally:
            session.close()

    def logout(self):
        from windows.auth import LoginWindow
        self.login_win = LoginWindow()
        self.login_win.show()
        self.login_win.setFixedSize(362, 226)
        self.close()
        
    def edit_profile(self):
        self.edit_win = EditProfile(self.login, self.photo)
        self.edit_win.profileUpdated.connect(self.update_profile)
        self.edit_win.setFixedSize(879, 438)
        self.edit_win.show()
        # self.close()
        
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
            item_text = f"Название: {product.name}\nОписание: {product.description}\nКоличество: {product.quantity}"
            photo = self.get_info().photo
            widget = ListItemWidget(photo, item_text, self.ui.listWidget)
            item = QListWidgetItem()
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)
            item.setSizeHint(QSize(600, 100))
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