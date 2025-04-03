from PySide6.QtWidgets import QMainWindow, QMessageBox
from sqlalchemy import select, insert
from windows.ui.reg_win import Ui_RegWindow
from windows.ui.login_win import Ui_LoginWindow
from windows.user import ShopWindow
from db.models.users import Users
from db.db_core import local_session


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        
        self.ui.reg_btn.clicked.connect(self.go_to_reg)
        self.ui.login_btn.clicked.connect(self.login)
        
    def go_to_reg(self):
        self.reg_win = RegWindow()
        self.reg_win.setFixedSize(436, 365)
        self.reg_win.show()
        self.close()
        
    def login(self):
        login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        
        session = local_session()
        try:
            user = session.scalar(select(Users).where(Users.login == login))
            
            if user is None or password != user.password:
                QMessageBox.warning(self, 'Неверный логин или пароль', 'Проверьте правильность данные и попробуйте еще раз')
                return
        finally:
            session.close()
            
        self.shop_win = ShopWindow(login, user.photo)
        self.shop_win.setFixedSize(1013, 682)
        self.shop_win.show()
        self.close()
        
class RegWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegWindow()
        self.ui.setupUi(self)
        
        self.ui.login_btn.clicked.connect(self.go_to_login)
        self.ui.reg_btn.clicked.connect(self.register)
        
    def go_to_login(self):
        self.login_win = LoginWindow()
        self.login_win.show()
        self.login_win.setFixedSize(362, 226)
        self.close()
        
    def register(self):
        login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        conf_pass = self.ui.conf_password_line.text()
        
        session = local_session()
        
        try:
            if not login or not password or not conf_pass:
                QMessageBox.warning(self, 'Проверьте поля', 'Проверьте поля, возможно не все поля заполнены')
                return

            if password != conf_pass:
                QMessageBox.warning(self, 'Пароли не совпадают', 'Пароли не совпадают, проврьте еще раз пароли')
                return
            
            existing_user = session.scalar(select(Users).where(Users.login == login))
            if existing_user:
                QMessageBox.warning(self, 'Такой пользователь уже есть', f'Пользователь с именем {login} уже есть')
                return

            
            session.execute(insert(Users).values(login=login,
                                                password=password))
            session.commit()
        finally:
            session.close()

        self.shop_win = ShopWindow(login)
        self.shop_win.show()
        self.shop_win.setFixedSize(1013, 682)
        self.close()
    
            
            
        