from PySide6.QtWidgets import (QMessageBox, 
                               QMainWindow,
                               QTableWidgetItem, 
                               QPushButton, 
                               QLineEdit, 
                               QTableWidget, 
                               QApplication)
from sqlalchemy import select, update
from db.models.products import Products
from db.db_core import local_session
from windows.ui.edit_product import Ui_EditorProductWindow
from windows.add_book import AddBookDialog
import sys



class EditProductsWindow(QMainWindow):
    def __init__(self, name: str):
        super().__init__()
        self.setWindowTitle("Library Manager")
        self.ui = Ui_EditorProductWindow()
        self.ui.setupUi(self)
        self.name = name

    
    def update_prod(self):
        # Установка данных в поля формы
        session = local_session()
        product = session.scalar(select(Products).where(Products.name == self.name))
        try:
            if product:
                print(product.importer)
                name = self.ui.name.setText(product.name)
                description = self.ui.description.setText(product.description)
                price = self.ui.price.setText(product.price)
                importer = self.ui.importer.setText(product.importer)
                quantity = self.ui.quantity.setText(product.quantity)
                prod_type = self.ui.type.setText(product.type)
                
                session.execute(update(Products).
                                where(Products.name == self.name).
                                values(name=name,
                                       description=description,
                                       price=price,
                                       importer=importer,
                                       quantity=quantity,
                                       type=prod_type))
            
                session.commit()
            else:
                QMessageBox.information(self, 'info', 'Продукт не найден')
        except Exception as e:
            session.rollback()
            print("Ошибка при обновлении продукта:", e)
        finally:
            session.close()