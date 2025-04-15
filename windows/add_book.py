from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from windows.ui.add_product import Ui_Dialog
from db.db_core import local_session
from db.models.products import Products
from datetime import datetime

class AddBookDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Настройка интерфейса
        self.ui.add_button.clicked.connect(self.add_book)  # Привязываем кнопку

    def add_book(self):
        """Добавляет новый товар в базу данных"""
        name = self.ui.name_line.text().strip()
        description = self.ui.desc_line.text()
        price = self.ui.price_line.text()
        importer = self.ui.importer_line.text().strip()
        quantity = self.ui.quantity_line.text().strip()
        
        if not (name and importer and quantity.isdigit()):
            QMessageBox.warning(self, "Ошибка", "Введите корректные данные!")
            return
        session = local_session()
        try:
            new_product = Products(
                name=name,
                description=description,
                importer=importer,
                price=price,
                quantity=int(quantity),
                date_add=datetime.now()
            )
            session.add(new_product)
            session.commit()
            QMessageBox.information(self, "Успех", "Товар успешно добавлен!")
            self.accept()
        except Exception as ex:
            session.rollback()
            QMessageBox.critical(self, "Ошибка", f"Ошибка добавления товара: {ex}")
        finally:
            session.close()
