# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_profile.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(879, 438)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 421, 301))
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


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login = QLineEdit(self.horizontalLayoutWidget)
        self.login.setObjectName(u"login")
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.login)

        self.firstname = QLineEdit(self.horizontalLayoutWidget)
        self.firstname.setObjectName(u"firstname")
        sizePolicy.setHeightForWidth(self.firstname.sizePolicy().hasHeightForWidth())
        self.firstname.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.firstname)

        self.lastname = QLineEdit(self.horizontalLayoutWidget)
        self.lastname.setObjectName(u"lastname")
        sizePolicy.setHeightForWidth(self.lastname.sizePolicy().hasHeightForWidth())
        self.lastname.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.lastname)

        self.number = QLineEdit(self.horizontalLayoutWidget)
        self.number.setObjectName(u"number")
        sizePolicy.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.number)

        self.city = QLineEdit(self.horizontalLayoutWidget)
        self.city.setObjectName(u"city")
        sizePolicy.setHeightForWidth(self.city.sizePolicy().hasHeightForWidth())
        self.city.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.city)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.user_image = QLabel(Dialog)
        self.user_image.setObjectName(u"user_image")
        self.user_image.setGeometry(QRect(580, 20, 211, 221))
        self.user_image.setStyleSheet(u"border: 2px solid")
        self.take_photo_btn = QPushButton(Dialog)
        self.take_photo_btn.setObjectName(u"take_photo_btn")
        self.take_photo_btn.setGeometry(QRect(580, 250, 211, 31))
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(380, 350, 211, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u043b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0438\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0444\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0433\u043e\u0440\u043e\u0434", None))
        self.user_image.setText("")
        self.take_photo_btn.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u043e\u0442\u043e", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

