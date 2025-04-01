from db.db_core import init_db
from PySide6.QtWidgets import QApplication
# from windows.manager import ManagerWindow
from windows.auth import LoginWindow
from windows.user import ShopWindow
import sys

# Инициалзация таблиц
from db.models.cart import Cart
from db.models.cart_item import CartItem
from db.models.products import Products
from db.models.users import Users

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.setFixedSize(362, 226)
    login.show()
    app.exec()
    