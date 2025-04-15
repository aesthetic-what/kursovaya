from PySide6.QtWidgets import (QMessageBox, 
                               QMainWindow,
                               QTableWidgetItem, 
                               QPushButton, 
                               QLineEdit, 
                               QTableWidget, 
                               QApplication)
from sqlalchemy import select
from db.models.products import Products
from db.db_core import local_session
from windows.ui.library import Ui_MainWindow
from windows.edit_product import EditProductsWindow
from windows.add_book import AddBookDialog
import sys

class ManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Manager")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_add.clicked.connect(self.add_product)
        self.ui.btn_edit.clicked.connect(self.edit_product)
        self.ui.btn_delete.clicked.connect(self.delete_product)
        
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Описание", "Поставщик", "Количество", "Дата добавления\обновления"])
        
        self.load_products()
    
    def get_session(self):
        return local_session()
    
    def load_products(self):
        session = self.get_session()
        products = session.execute(select(Products)).scalars().all()
        self.ui.tableWidget.setRowCount(len(products))
        for row, product in enumerate(products):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(product.name)),
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(product.description))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(product.type))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(product.importer))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(product.quantity)))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(str(product.date_add)))
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
            session.query(Products).filter_by(id=product_id).delete()
            session.commit()
            session.close()
            self.load_products()
    
    def edit_product(self):
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
        products = session.execute(select(Products).filter(Products.name.ilike(f"%{search_term}%"))).scalars().all()
        self.tableWidget.setRowCount(len(products))
        for row, product in enumerate(products):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(product.name))
            self.ui.tableWidget.setItem()
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(product.importer))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(product.quantity)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(product.date_add)))
        session.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManagerWindow()
    window.show()
    sys.exit(app.exec())
