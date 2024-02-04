# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Selecter.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(253, 294)
        Dialog.setMinimumSize(QSize(253, 294))
        Dialog.setMaximumSize(QSize(253, 294))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 156), stop:0.00 rgba(240, 150, 80, 210), stop:0.9999 rgba(0, 0, 0, 240), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.node_button = QPushButton(Dialog)
        self.node_button.setObjectName(u"node_button")
        self.node_button.setGeometry(QRect(50, 20, 151, 51))
        self.node_button.setStyleSheet(u"QPushButton{\n"
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
        self.miners_button = QPushButton(Dialog)
        self.miners_button.setObjectName(u"miners_button")
        self.miners_button.setGeometry(QRect(50, 80, 151, 51))
        self.miners_button.setStyleSheet(u"QPushButton{\n"
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
        self.trans_button = QPushButton(Dialog)
        self.trans_button.setObjectName(u"trans_button")
        self.trans_button.setGeometry(QRect(50, 140, 151, 51))
        self.trans_button.setStyleSheet(u"QPushButton{\n"
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
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 210, 131, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border-radius: 10px;\n"
"font-size: 24px;\n"
"background-color: rgba(255,255,255,80);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"font-weight: bold;\n"
"color: #DCDCDC;")
        self.blocks = QLineEdit(Dialog)
        self.blocks.setObjectName(u"blocks")
        self.blocks.setGeometry(QRect(160, 210, 71, 51))
        self.blocks.setStyleSheet(u"border-radius: 15px;\n"
"font-size: 24px;\n"
"background-color: rgba(255,255,255,70);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"color:black;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Select function", None))
        self.node_button.setText(QCoreApplication.translate("Dialog", u"Node list", None))
        self.miners_button.setText(QCoreApplication.translate("Dialog", u"Miners", None))
        self.trans_button.setText(QCoreApplication.translate("Dialog", u"Transactions", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Blocks:", None))
    # retranslateUi

