# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mySentResponses.ui'
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

class Ui_MySentResponsesWindow(object):
    def setupUi(self, MySentResponsesWindow):
        if not MySentResponsesWindow.objectName():
            MySentResponsesWindow.setObjectName(u"MySentResponsesWindow")
        MySentResponsesWindow.resize(800, 600)
        self.verticalLayout = QVBoxLayout(MySentResponsesWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.responseListWidget = QListWidget(MySentResponsesWindow)
        self.responseListWidget.setObjectName(u"responseListWidget")

        self.verticalLayout.addWidget(self.responseListWidget)

        self.detailsButton = QPushButton(MySentResponsesWindow)
        self.detailsButton.setObjectName(u"detailsButton")

        self.verticalLayout.addWidget(self.detailsButton)

        self.submitButton = QPushButton(MySentResponsesWindow)
        self.submitButton.setObjectName(u"submitButton")

        self.verticalLayout.addWidget(self.submitButton)

        self.backButton = QPushButton(MySentResponsesWindow)
        self.backButton.setObjectName(u"backButton")

        self.verticalLayout.addWidget(self.backButton)


        self.retranslateUi(MySentResponsesWindow)

        QMetaObject.connectSlotsByName(MySentResponsesWindow)
    # setupUi

    def retranslateUi(self, MySentResponsesWindow):
        MySentResponsesWindow.setWindowTitle(QCoreApplication.translate("MySentResponsesWindow", u"\u041c\u043e\u0438 \u043e\u0442\u043a\u043b\u0438\u043a\u0438", None))
        self.detailsButton.setText(QCoreApplication.translate("MySentResponsesWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.submitButton.setText(QCoreApplication.translate("MySentResponsesWindow", u"\u0421\u0434\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443", None))
        self.backButton.setText(QCoreApplication.translate("MySentResponsesWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

