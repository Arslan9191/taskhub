# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
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

class Ui_ChatDialog(object):
    def setupUi(self, ChatDialog):
        if not ChatDialog.objectName():
            ChatDialog.setObjectName(u"ChatDialog")
        ChatDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ChatDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chatHistory = QTextEdit(ChatDialog)
        self.chatHistory.setObjectName(u"chatHistory")
        self.chatHistory.setReadOnly(True)

        self.verticalLayout.addWidget(self.chatHistory)

        self.messageEdit = QTextEdit(ChatDialog)
        self.messageEdit.setObjectName(u"messageEdit")

        self.verticalLayout.addWidget(self.messageEdit)

        self.sendButton = QPushButton(ChatDialog)
        self.sendButton.setObjectName(u"sendButton")

        self.verticalLayout.addWidget(self.sendButton)


        self.retranslateUi(ChatDialog)

        QMetaObject.connectSlotsByName(ChatDialog)
    # setupUi

    def retranslateUi(self, ChatDialog):
        ChatDialog.setWindowTitle(QCoreApplication.translate("ChatDialog", u"\u0427\u0430\u0442", None))
        self.sendButton.setText(QCoreApplication.translate("ChatDialog", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

