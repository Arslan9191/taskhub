# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'responseDetails.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_ResponseDetailsWindow(object):
    def setupUi(self, ResponseDetailsWindow):
        if not ResponseDetailsWindow.objectName():
            ResponseDetailsWindow.setObjectName(u"ResponseDetailsWindow")
        ResponseDetailsWindow.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ResponseDetailsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.taskDetailsButton = QPushButton(ResponseDetailsWindow)
        self.taskDetailsButton.setObjectName(u"taskDetailsButton")

        self.verticalLayout.addWidget(self.taskDetailsButton)

        self.responseDetailsButton = QPushButton(ResponseDetailsWindow)
        self.responseDetailsButton.setObjectName(u"responseDetailsButton")

        self.verticalLayout.addWidget(self.responseDetailsButton)

        self.deadlineLabel = QLabel(ResponseDetailsWindow)
        self.deadlineLabel.setObjectName(u"deadlineLabel")

        self.verticalLayout.addWidget(self.deadlineLabel)

        self.detailsTextEdit = QTextEdit(ResponseDetailsWindow)
        self.detailsTextEdit.setObjectName(u"detailsTextEdit")
        self.detailsTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.detailsTextEdit)

        self.closeButton = QPushButton(ResponseDetailsWindow)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout.addWidget(self.closeButton)


        self.retranslateUi(ResponseDetailsWindow)

        QMetaObject.connectSlotsByName(ResponseDetailsWindow)
    # setupUi

    def retranslateUi(self, ResponseDetailsWindow):
        ResponseDetailsWindow.setWindowTitle(QCoreApplication.translate("ResponseDetailsWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438 \u043e\u0442\u043a\u043b\u0438\u043a\u0430", None))
        self.taskDetailsButton.setText(QCoreApplication.translate("ResponseDetailsWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.responseDetailsButton.setText(QCoreApplication.translate("ResponseDetailsWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438 \u043e\u0442\u043a\u043b\u0438\u043a\u0430", None))
        self.deadlineLabel.setText(QCoreApplication.translate("ResponseDetailsWindow", u"\u0414\u0435\u0434\u043b\u0430\u0439\u043d: ", None))
        self.closeButton.setText(QCoreApplication.translate("ResponseDetailsWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

