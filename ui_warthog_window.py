# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Warthog_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 156), stop:0.00 rgba(240, 150, 80, 210), stop:0.9999 rgba(0, 0, 0, 240), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.select_button = QPushButton(self.centralwidget)
        self.select_button.setObjectName(u"select_button")
        self.select_button.setGeometry(QRect(540, 20, 141, 51))
        self.select_button.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"font-size: 24px;\n"
"background-color: rgba(255,255,255,80);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"font-weight: bold;\n"
"color: #DCDCDC;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,60);\n"
"}\n"
"")
        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(20, 21, 501, 51))
        self.input_text.setStyleSheet(u"border-radius: 15px;\n"
"font-size: 24px;\n"
"background-color: rgba(255,255,255,70);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"color:black;")
        self.items = QListWidget(self.centralwidget)
        self.items.setObjectName(u"items")
        self.items.setGeometry(QRect(20, 91, 661, 381))
        self.items.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"color:black;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Warthog Network", None))
        self.select_button.setText(QCoreApplication.translate("MainWindow", u"Select", None))
    # retranslateUi

