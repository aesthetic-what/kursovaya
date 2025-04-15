from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import QByteArray, Qt
from PySide6.QtGui import QPixmap


class ListItemWidget(QWidget):
    """Кастомный элемент списка: картинка + текст"""
    def __init__(self, text: str, parent_list, price: str, image_data: bytes | None = None):
        super().__init__()

        self.parent_list = parent_list  # Сохраняем ссылку на QListWidget
        self.setStyleSheet("""
                QListWidget {
                    background-color: #B0B0B0; /* Цвет фона */
                    border: 1px solid #ccc; /* Граница */
                    border-radius: 25px; /* Скругление углов */
                    padding: 15px;
                }

                QListWidget::item {
                    /*background-color: white; /* Фон элементов */
                    color: black /* Цвет текста */
                    padding: 12px 15px;
                    border: 1px solid;
                    border-radius: 3px;
                }

                QListWidget::item:hover {
                    background-color: #d0d0d0;
                }

                QListWidget::item:selected {
                    background-color: #005a9e; /* Темно-синий фон */
                    color: white; /* Белый текст */
                    font-weight: bold; /* Жирный текст для выделенного элемента */
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
        layout.setSpacing(0)  # Убирает промежуток между элементами
        self.setLayout(layout)