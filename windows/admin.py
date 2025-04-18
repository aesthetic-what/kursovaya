from PySide6.QtWidgets import (QMessageBox, 
                               QMainWindow,
                               QTableWidgetItem, 
                               QPushButton, 
                               QLineEdit, 
                               QTableWidget, 
                               QApplication)
from sqlalchemy import select
from db.models.users import Users
from db.db_core import local_session
from windows.ui.library import Ui_MainWindow
from windows.edit_manager import EditProfile
from windows.add_book import AddBookDialog
import sys

class AdminWindow(QMainWindow):
    def __init__(self, login: str):
        super().__init__()
        self.setWindowTitle("Админ панель")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.login = login
        
        self.ui.btn_add.clicked.connect(self.add_product)
        self.ui.btn_edit.clicked.connect(self.edit_profile)
        self.ui.btn_delete.clicked.connect(self.delete_product)
        
        self.ui.tableWidget.setColumnCount(9)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "login", "password", "first_name", "last_name", "number", "city", "balance", "role"])
        
        self.load_products()
    
    def get_session(self):
        return local_session()
    
    def load_products(self):
        session = self.get_session()
        users = session.execute(select(Users)).scalars().all()
        self.ui.tableWidget.setRowCount(len(users))
        for row, user in enumerate(users):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(user.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(user.login)),
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(user.password))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(user.first_name))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(user.last_name))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(user.number))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(user.city))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(user.balance))
            self.ui.tableWidget.setItem(row, 8, QTableWidgetItem(user.role))
        session.close()
    
    def add_product(self):
        """Открывает диалоговое окно для добавления книги."""
        dialog = AddBookDialog()
        if dialog.exec_():  # Ожидаем закрытия диалога
            self.search_products()    
            
            
    def delete_product(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            product_id = int(self.tableWidget.item(selected_row, 0).text())
            session = self.get_session()
            session.query(Users).filter_by(id=product_id).delete()
            session.commit()
            session.close()
            self.load_products()
    
    def edit_profile(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите продукт для редактирования.")
            return

        # Получаем данные из таблицы
        product_data = {
            'id': int(self.ui.tableWidget.item(selected_row, 0).text()),
            'name': self.ui.tableWidget.item(selected_row, 1).text(),
            'description': self.ui.tableWidget.item(selected_row, 2).text(),
            'importer': self.ui.tableWidget.item(selected_row, 3).text(),
            'quantity': self.ui.tableWidget.item(selected_row, 4).text(),
            'date_add': self.ui.tableWidget.item(selected_row, 5).text(),
        }

        # Передаём в окно редактирования
        self.edit_prod_win = EditProductsWindow(product_data)
        self.edit_prod_win.show()
    
    def search_products(self):
        search_term = self.lineEdit_search.text()
        session = self.get_session()
        products = session.execute(select(Users).filter(Users.name.ilike(f"%{search_term}%"))).scalars().all()
        self.tableWidget.setRowCount(len(products))
        for row, product in enumerate(products):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(product.name))
            self.ui.tableWidget.setItem()
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(product.importer))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(product.quantity)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(product.date_add)))
        session.close()