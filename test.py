from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QWidget, QPushButton, QLabel, QHBoxLayout

class ListItemWidget(QWidget):
    """Кастомный элемент списка с текстом и кнопкой"""
    def __init__(self, text, parent_list):
        super().__init__()

        self.parent_list = parent_list  # Сохраняем ссылку на QListWidget

        # Текст элемента
        self.label = QLabel(text)

        # Кнопка
        self.button = QPushButton("Удалить")
        self.button.clicked.connect(self.remove_item)  # Удаляем при клике

        # Расположение элементов
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def remove_item(self):
        """Удаляет элемент списка"""
        for i in range(self.parent_list.count()):
            item = self.parent_list.item(i)
            widget = self.parent_list.itemWidget(item)
            if widget == self:
                self.parent_list.takeItem(i)  # Удаляем элемент списка
                break


class MyApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = QListWidget()

        # Добавляем элементы с кнопками
        for i in range(5):
            item = QListWidgetItem()
            widget = ListItemWidget(f"Товар {i+1}", self.window)

            item.setSizeHint(widget.sizeHint())  # Устанавливаем размер
            self.window.addItem(item)
            self.window.setItemWidget(item, widget)  # Привязываем виджет

        self.window.show()


app = MyApp([])
app.exec()
