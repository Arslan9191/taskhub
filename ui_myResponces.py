# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myResponces.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MyResponsesWindow(object):
    def setupUi(self, MyResponsesWindow):
        if not MyResponsesWindow.objectName():
            MyResponsesWindow.setObjectName(u"MyResponsesWindow")
        MyResponsesWindow.resize(800, 600)
        self.verticalLayout = QVBoxLayout(MyResponsesWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.responseListWidget = QListWidget(MyResponsesWindow)
        self.responseListWidget.setObjectName(u"responseListWidget")

        self.verticalLayout.addWidget(self.responseListWidget)

        self.closeButton = QPushButton(MyResponsesWindow)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout.addWidget(self.closeButton)


        self.retranslateUi(MyResponsesWindow)

        QMetaObject.connectSlotsByName(MyResponsesWindow)
    # setupUi

    def retranslateUi(self, MyResponsesWindow):
        MyResponsesWindow.setWindowTitle(QCoreApplication.translate("MyResponsesWindow", u"\u041c\u043e\u0438 \u041e\u0442\u043a\u043b\u0438\u043a\u0438", None))
        self.closeButton.setText(QCoreApplication.translate("MyResponsesWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

