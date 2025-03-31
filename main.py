from db.db_core import init_db
from PySide6.QtWidgets import QApplication
# from windows.auth import LoginWindow
from windows.user import ShopWindow
from windows.manager import ManagerWindow
import sys

# Инициалзация таблиц
from db.models.cart import Cart
from db.models.cart_item import CartItem
from db.models.products import Products
from db.models.users import Users

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    shop = ShopWindow()
    shop.show()
    app.exec()
    