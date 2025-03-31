# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shop_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import windows.ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 682)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(350, 40, 651, 571))
        self.scrollArea.setStyleSheet(u"border-radius: 2px")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 651, 571))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 0, 651, 571))
        self.listWidget.setLayoutDirection(Qt.LeftToRight)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"    background-color: #f5f5f5; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    border: 1px solid #ccc; /* \u0413\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 25px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    /*background-color: white; /* \u0424\u043e\u043d \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"    color: #333; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    padding: 12px 15px;\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"	margin: 5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #005a9e; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-weig"
                        "ht: bold; /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 */\n"
"}")
        self.listWidget.setSortingEnabled(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(350, 620, 651, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.prev_button = QPushButton(self.horizontalLayoutWidget)
        self.prev_button.setObjectName(u"prev_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_button.sizePolicy().hasHeightForWidth())
        self.prev_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.prev_button)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.next_button = QPushButton(self.horizontalLayoutWidget)
        self.next_button.setObjectName(u"next_button")
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.next_button)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 20, 200, 200))
        self.label_2.setPixmap(QPixmap(u":/images/2e2ecb46a9db18b8f47baf6f849195eb.jpg"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 230, 201, 31))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 260, 201, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(350, 10, 651, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.searcn_button = QPushButton(self.horizontalLayoutWidget_3)
        self.searcn_button.setObjectName(u"searcn_button")

        self.horizontalLayout_4.addWidget(self.searcn_button)

        self.searchbar = QLineEdit(self.horizontalLayoutWidget_3)
        self.searchbar.setObjectName(u"searchbar")

        self.horizontalLayout_4.addWidget(self.searchbar)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(80, 400, 181, 71))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sort = QLabel(self.verticalLayoutWidget_2)
        self.sort.setObjectName(u"sort")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sort.sizePolicy().hasHeightForWidth())
        self.sort.setSizePolicy(sizePolicy1)
        self.sort.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.sort)

        self.sort_box = QComboBox(self.verticalLayoutWidget_2)
        self.sort_box.addItem("")
        self.sort_box.addItem("")
        self.sort_box.addItem("")
        self.sort_box.setObjectName(u"sort_box")

        self.verticalLayout_2.addWidget(self.sort_box)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.prev_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"username1312", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.searcn_button.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0438\u0441\u043a", None))
        self.sort.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e:", None))
        self.sort_box.setItemText(0, "")
        self.sort_box.setItemText(1, QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.sort_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Z-A", None))

    # retranslateUi

