from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import QByteArray, Qt
from PySide6.QtGui import QPixmap


class ListItemWidget(QWidget):
    """Кастомный элемент списка: картинка + текст"""
    def __init__(self, text: str, parent_list, price: str, image_data: bytes | None = None):
        super().__init__()

        self.parent_list = parent_list  # Сохраняем ссылку на QListWidget
        self.setStyleSheet("""
                QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """)

        # Картинка (если нет данных, загружаем "default.png")
        self.image_label = QLabel()
        pixmap = QPixmap()
        if image_data:
            pixmap.loadFromData(QByteArray(image_data))
        else:
            pixmap.load("windows/ui/images.png")  # Файл-заглушка

        # Масштабируем картинку
        pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(pixmap)

        # Название товара
        self.text_label = QLabel(text)
        self.text_label.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 12px;
            }
        """) # Привязываем функцию

        # Размещение элементов в строку
        layout = QHBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)
        self.setLayout(layout)