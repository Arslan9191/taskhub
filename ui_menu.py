# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.viewCreateTaskButton = QPushButton(Dialog)
        self.viewCreateTaskButton.setObjectName(u"viewCreateTaskButton")
        self.viewCreateTaskButton.setGeometry(QRect(270, 260, 101, 24))
        self.viewCreateTaskButton.setFlat(False)
        self.viewTaskButton = QPushButton(Dialog)
        self.viewTaskButton.setObjectName(u"viewTaskButton")
        self.viewTaskButton.setGeometry(QRect(110, 260, 101, 24))
        self.viewMyTaskButton = QPushButton(Dialog)
        self.viewMyTaskButton.setObjectName(u"viewMyTaskButton")
        self.viewMyTaskButton.setGeometry(QRect(430, 260, 101, 24))
        self.goToMySentResponcesButton = QPushButton(Dialog)
        self.goToMySentResponcesButton.setObjectName(u"goToMySentResponcesButton")
        self.goToMySentResponcesButton.setGeometry(QRect(590, 260, 101, 24))

        self.retranslateUi(Dialog)

        self.viewCreateTaskButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"TaskHub", None))
        self.viewCreateTaskButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.viewTaskButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u0434\u0430\u0447", None))
        self.viewMyTaskButton.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0438 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.goToMySentResponcesButton.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0438 \u043e\u0442\u043a\u043b\u0438\u043a\u0438", None))
    # retranslateUi

