# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createTask.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_CreateTaskWindow(object):
    def setupUi(self, CreateTaskWindow):
        if not CreateTaskWindow.objectName():
            CreateTaskWindow.setObjectName(u"CreateTaskWindow")
        CreateTaskWindow.resize(400, 316)
        self.verticalLayout = QVBoxLayout(CreateTaskWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleTaskEdit = QTextEdit(CreateTaskWindow)
        self.titleTaskEdit.setObjectName(u"titleTaskEdit")

        self.verticalLayout.addWidget(self.titleTaskEdit)

        self.descriptionTaskEdit = QTextEdit(CreateTaskWindow)
        self.descriptionTaskEdit.setObjectName(u"descriptionTaskEdit")

        self.verticalLayout.addWidget(self.descriptionTaskEdit)

        self.deadlineEdit = QDateTimeEdit(CreateTaskWindow)
        self.deadlineEdit.setObjectName(u"deadlineEdit")
        self.deadlineEdit.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.deadlineEdit)

        self.createTaskButton = QPushButton(CreateTaskWindow)
        self.createTaskButton.setObjectName(u"createTaskButton")

        self.verticalLayout.addWidget(self.createTaskButton)

        self.exitCreateTaskButton = QPushButton(CreateTaskWindow)
        self.exitCreateTaskButton.setObjectName(u"exitCreateTaskButton")

        self.verticalLayout.addWidget(self.exitCreateTaskButton)


        self.retranslateUi(CreateTaskWindow)

        QMetaObject.connectSlotsByName(CreateTaskWindow)
    # setupUi

    def retranslateUi(self, CreateTaskWindow):
        CreateTaskWindow.setWindowTitle(QCoreApplication.translate("CreateTaskWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.deadlineEdit.setDisplayFormat(QCoreApplication.translate("CreateTaskWindow", u"yyyy-MM-dd HH:mm:ss", None))
        self.createTaskButton.setText(QCoreApplication.translate("CreateTaskWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.exitCreateTaskButton.setText(QCoreApplication.translate("CreateTaskWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

