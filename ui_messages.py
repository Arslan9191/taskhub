# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messages.ui'
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

class Ui_MessagesWindow(object):
    def setupUi(self, MessagesWindow):
        if not MessagesWindow.objectName():
            MessagesWindow.setObjectName(u"MessagesWindow")
        MessagesWindow.resize(800, 600)
        self.verticalLayout = QVBoxLayout(MessagesWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.messageListWidget = QListWidget(MessagesWindow)
        self.messageListWidget.setObjectName(u"messageListWidget")

        self.verticalLayout.addWidget(self.messageListWidget)

        self.backButton = QPushButton(MessagesWindow)
        self.backButton.setObjectName(u"backButton")

        self.verticalLayout.addWidget(self.backButton)


        self.retranslateUi(MessagesWindow)

        QMetaObject.connectSlotsByName(MessagesWindow)
    # setupUi

    def retranslateUi(self, MessagesWindow):
        MessagesWindow.setWindowTitle(QCoreApplication.translate("MessagesWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.backButton.setText(QCoreApplication.translate("MessagesWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

