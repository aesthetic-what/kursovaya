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
from windows.ui.edit_product import Ui_EditorProductWindow
from windows.add_book import AddBookDialog
import sys



class EditProductsWindow(QMainWindow):
    def __init__(self, product_data: dict):
        super().__init__()
        self.setWindowTitle("Library Manager")
        self.ui = Ui_EditorProductWindow()
        self.ui.setupUi(self)
        self.product_data = product_data

    
    def update_prod(self):
        # Установка данных в поля формы
        self.ui.name.setText(self.product_data['name'])
        self.ui.description.setText(self.product_data['description'])
        self.ui.importer.setText(self.product_data['importer'])
        self.ui.quantity.setText(self.product_data['quantity'])
        self.ui.date_added.setText(self.product_data['date_add'])

        session = local_session()

        product = session.scalar(select(Products).where(Products.name == name))
        try:
            if product:
                product.date_add = date_added
                product.description = description
                product.importer = importer
                product.price = price
                product.quantity = quantity
                product.type = type_prod
            
                session.commit()
            else:
                QMessageBox.information(self, 'info', 'Продукт не найден')
        except Exception as e:
            session.rollback()
            print("Ошибка при обновлении продукта:", e)
        finally:
            session.close()