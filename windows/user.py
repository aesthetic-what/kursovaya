from PySide6.QtWidgets import QMainWindow
from windows.ui.shop_win import Ui_ShopWindow


class ShopWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShopWindow()
        self.ui.setupUi(self)