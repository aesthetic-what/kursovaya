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
import sys

class ManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Manager")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.setGeometry(100, 100, 800, 600)

        # self.tableWidget = QTableWidget(self)
        # self.tableWidget.setGeometry(50, 50, 700, 400)
        # self.tableWidget.setColumnCount(5)
        # self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Импортер", "Количество", "Дата добавления"])
        
        # self.btn_add = QPushButton("Добавить", self)
        # self.btn_add.setGeometry(50, 500, 100, 30)
        # self.btn_add.clicked.connect(self.add_product)
        
        # self.btn_delete = QPushButton("Удалить", self)
        # self.btn_delete.setGeometry(200, 500, 100, 30)
        # self.btn_delete.clicked.connect(self.delete_product)
        
        # self.btn_edit = QPushButton("Изменить", self)
        # self.btn_edit.setGeometry(350, 500, 100, 30)
        # self.btn_edit.clicked.connect(self.edit_product)
        
        # self.btn_search = QPushButton("Поиск", self)
        # self.btn_search.setGeometry(500, 500, 100, 30)
        # self.btn_search.clicked.connect(self.search_products)
        
        # self.lineEdit_search = QLineEdit(self)
        # self.lineEdit_search.setGeometry(50, 460, 200, 30)
        
        self.load_products()
    
    def get_session(self):
        return local_session()
    
    def load_products(self):
        session = self.get_session()
        products = session.execute(select(Products)).scalars().all()
        self.ui.tableWidget.setRowCount(len(products))
        for row, product in enumerate(products):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(product.name))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(product.importer))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(product.quantity)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(product.date_add)))
        session.close()
    
    def add_product(self):
        session = self.get_session()
        new_product = Products(name="Новый товар", importer="Импортер", quantity=10)
        session.add(new_product)
        session.commit()
        session.close()
        self.load_products()
    
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
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            product_id = int(self.tableWidget.item(selected_row, 0).text())
            session = self.get_session()
            product = session.query(Products).filter_by(id=product_id).first()
            if product:
                product.name = "Обновленный товар"
                product.importer = "Обновленный импортер"
                product.quantity = 20
                session.commit()
            session.close()
            self.load_products()
    
    def search_products(self):
        search_term = self.lineEdit_search.text()
        session = self.get_session()
        products = session.execute(select(Products).filter(Products.name.ilike(f"%{search_term}%"))).scalars().all()
        self.tableWidget.setRowCount(len(products))
        for row, product in enumerate(products):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(product.name))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(product.importer))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(product.quantity)))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(product.date_add)))
        session.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManagerWindow()
    window.show()
    sys.exit(app.exec())
