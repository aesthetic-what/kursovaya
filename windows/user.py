from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt, QSize
from windows.ui.shop_win import Ui_ShopWindow
from sqlalchemy import select, func
from db.models.products import Products
from db.db_core import local_session
from db.query.users import get_books


class ShopWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShopWindow()
        self.ui.setupUi(self)
        
        self.items_per_page = 20
        self.current_page = 0
        
        self.ui.searcn_button.clicked.connect(self.search_prod)
        self.ui.sort_box.currentIndexChanged.connect(self.sort_products)
        self.ui.prev_button.clicked.connect(self.prev_page)
        self.ui.next_button.clicked.connect(self.next_page)
    
        self.load_products()
        
        
        
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
        search_term = self.ui.searchbar.text()
        products = get_books(search_term)

        self.ui.listWidget.clear()  # Очищаем список перед добавлением новых элементов

        for product in products:
            item = QListWidgetItem(f"Название: {product.name}\nОписание: {product.description}\nКоличество: {product.quantity}")  # Используем первый элемент из кортежа как текст
            item.setData(Qt.UserRole, product)  # Сохраняем всю информацию о книге
            self.ui.listWidget.addItem(item)
            item.setSizeHint(QSize(600, 100))
            
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
            self.load_products()

    def next_page(self):
        """Переход на следующую страницу"""
        self.current_page += 1
        self.ui.label.setText(f"Страница: {self.current_page + 1}")
        self.load_products()