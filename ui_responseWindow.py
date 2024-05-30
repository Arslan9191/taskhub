# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responseWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_ResponseWindow(object):
    def setupUi(self, ResponseWindow):
        if not ResponseWindow.objectName():
            ResponseWindow.setObjectName(u"ResponseWindow")
        ResponseWindow.resize(800, 600)
        self.verticalLayout = QVBoxLayout(ResponseWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.responseTextEdit = QTextEdit(ResponseWindow)
        self.responseTextEdit.setObjectName(u"responseTextEdit")

        self.verticalLayout.addWidget(self.responseTextEdit)

        self.sendResponseButton = QPushButton(ResponseWindow)
        self.sendResponseButton.setObjectName(u"sendResponseButton")

        self.verticalLayout.addWidget(self.sendResponseButton)

        self.cancelButton = QPushButton(ResponseWindow)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.retranslateUi(ResponseWindow)

        QMetaObject.connectSlotsByName(ResponseWindow)
    # setupUi

    def retranslateUi(self, ResponseWindow):
        ResponseWindow.setWindowTitle(QCoreApplication.translate("ResponseWindow", u"TaskHub", None))
        ResponseWindow.setProperty("TaskHub", QCoreApplication.translate("ResponseWindow", u"\u041e\u0442\u043a\u043b\u0438\u043a \u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.responseTextEdit.setPlaceholderText(QCoreApplication.translate("ResponseWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u043e\u0442\u043a\u043b\u0438\u043a...", None))
        self.sendResponseButton.setText(QCoreApplication.translate("ResponseWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u043a\u043b\u0438\u043a", None))
        self.cancelButton.setText(QCoreApplication.translate("ResponseWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

