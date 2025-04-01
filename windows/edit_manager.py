from windows.ui.edit_win import Ui_Dialog
from db.models.users import Users
from db.db_core import local_session
from sqlalchemy import select, update

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
from PySide6.QtCore import Signal


class EditProfile(QDialog):
    profileUpdated = Signal()
    def __init__(self, login: str):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Кнопки
        self.ui.save_button.clicked.connect(self.save_changes)
        self.ui.take_photo_btn.clicked.connect(self.take_photo)
        
        # Константы
        self.login = login
        self.user_info = self.get_info()
        
        # Поля для редактирования
        self.ui.login.setText(self.user_info.login)
        self.ui.firstname.setText(self.user_info.first_name)
        self.ui.lastname.setText(self.user_info.last_name)
        self.ui.number.setText(self.user_info.number)
        self.ui.city.setText(self.user_info.city)
        
    def take_photo(self):
        """Открывает диалог выбора файла и загружает фото"""
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите фото", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        
        if file_path:
            try:
                with open(file_path, "rb") as file:
                    self.photo_data = file.read()

                # Отобразить фото в QLabel
                pixmap = QPixmap(file_path)
                self.ui.user_image.setPixmap(pixmap)

            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить фото: {e}")
        
    def get_info(self) -> Users:
        session = local_session()
        try:
            user_info = session.scalar(select(Users).where(Users.login == self.login))
            return user_info
        except Exception as ex:
            QMessageBox(self, 'Ошибка', f'Произошла невиданная ошибка\n{ex}')
        finally:
            session.close()
            
    def save_changes(self):
        login = self.ui.login.text()
        firstname = self.ui.firstname.text()
        lastname = self.ui.lastname.text()
        number = self.ui.number.text()
        city = self.ui.city.text()
        
        # Открываем диалог выбора файла
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите фото", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")

        photo_data = None  # По умолчанию фото отсутствует

        if file_path:
            try:
                with open(file_path, "rb") as file:
                    photo_data = file.read()  # Читаем изображение в бинарном формате
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить фото: {e}")
                return

        session = local_session()
        try:
            # Выполнение запроса на обновление
            result = session.execute(
                update(Users)
                .where(Users.login == self.login)  # Используйте self.login, если это корректно
                .values(login=login,
                        first_name=firstname,
                        last_name=lastname,
                        number=number,
                        city=city)
            )
            
            # Добавляем фото только если оно выбрано
            if photo_data:
                update_query = update_query.values(photo=photo_data)

            result = session.execute(update_query)
            
            # Проверка, были ли изменения
            if result.rowcount > 0:
                session.commit()
                QMessageBox.information(self, 'Успешно', 'Профиль успешно обновлен')
                self.profileUpdated.emit()
                self.close()
            else:
                QMessageBox.warning(self, "Предупреждение", "Профиль не был изменен")
                return

        except Exception as ex:
            QMessageBox.warning(self, "Ошибка", "Произошла ошибка при обновлении пользователя")
            print(f"Ошибка: {ex}")  # Можно добавить больше контекста для отладки
        finally:
            session.close()