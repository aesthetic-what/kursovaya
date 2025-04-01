from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from sqlalchemy import select, func

from windows.ui.shop_win import Ui_ShopWindow
from windows.edit_manager import EditProfile

from db.models.products import Products
from db.models.users import Users
from db.db_core import local_session


class ShopWindow(QMainWindow):
    def __init__(self, login: str):
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
        self.load_products()
        self.ui.login.setText(login)
    
    def logout(self):
        self.close()
        
    def edit_profile(self):
        self.edit_win = EditProfile(self.login)
        self.edit_win.profileUpdated.connect(self.update_profile)
        self.edit_win.setFixedSize(879, 438)
        self.edit_win.show()
        # self.close()
        
    def update_profile(self):
        """Обновляет данные профиля в главном окне"""
        session = local_session()
        try:
            # Получаем обновленные данные пользователя из базы
            user = session.query(Users).filter(Users.login == self.current_user_login).first()
            
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
            item = QListWidgetItem(item_text)
            self.ui.listWidget.addItem(item)
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