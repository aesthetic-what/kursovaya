# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_product.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_EditorProductWindow(object):
    def setupUi(self, EditorProductWindow):
        if not EditorProductWindow.objectName():
            EditorProductWindow.setObjectName(u"EditorProductWindow")
        EditorProductWindow.resize(469, 564)
        self.centralwidget = QWidget(EditorProductWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 30, 421, 441))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name = QLineEdit(self.horizontalLayoutWidget)
        self.name.setObjectName(u"name")
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.name)

        self.description = QLineEdit(self.horizontalLayoutWidget)
        self.description.setObjectName(u"description")
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.description)

        self.type = QLineEdit(self.horizontalLayoutWidget)
        self.type.setObjectName(u"type")
        sizePolicy.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.type)

        self.importer = QLineEdit(self.horizontalLayoutWidget)
        self.importer.setObjectName(u"importer")
        sizePolicy.setHeightForWidth(self.importer.sizePolicy().hasHeightForWidth())
        self.importer.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.importer)

        self.quantity = QLineEdit(self.horizontalLayoutWidget)
        self.quantity.setObjectName(u"quantity")
        sizePolicy.setHeightForWidth(self.quantity.sizePolicy().hasHeightForWidth())
        self.quantity.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.quantity)

        self.date_added = QLineEdit(self.horizontalLayoutWidget)
        self.date_added.setObjectName(u"date_added")
        sizePolicy.setHeightForWidth(self.date_added.sizePolicy().hasHeightForWidth())
        self.date_added.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.date_added)

        self.price = QLineEdit(self.horizontalLayoutWidget)
        self.price.setObjectName(u"price")
        sizePolicy.setHeightForWidth(self.price.sizePolicy().hasHeightForWidth())
        self.price.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.price)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(120, 490, 211, 51))
        EditorProductWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditorProductWindow)

        QMetaObject.connectSlotsByName(EditorProductWindow)
    # setupUi

    def retranslateUi(self, EditorProductWindow):
        EditorProductWindow.setWindowTitle(QCoreApplication.translate("EditorProductWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("EditorProductWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("EditorProductWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("EditorProductWindow", u"\u0422\u0438\u043f \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("EditorProductWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_5.setText(QCoreApplication.translate("EditorProductWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_6.setText(QCoreApplication.translate("EditorProductWindow", u"\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("EditorProductWindow", u"\u0426\u0435\u043d\u0430", None))
        self.save_button.setText(QCoreApplication.translate("EditorProductWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

