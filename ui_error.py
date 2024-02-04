# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog_Err(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 116)
        Dialog.setMinimumSize(QSize(400, 116))
        Dialog.setMaximumSize(QSize(400, 116))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 156), stop:0.00 rgba(240, 150, 80, 210), stop:0.9999 rgba(0, 0, 0, 240), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 30, 231, 61))
        font = QFont()
        font.setFamilies([u"SimSun"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-radius: 10px;\n"
"font-size: 24px;\n"
"background-color: rgba(255,255,255,80);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"font-weight: bold;\n"
"color: #DCDCDC;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Error", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Connection error", None))
    # retranslateUi

