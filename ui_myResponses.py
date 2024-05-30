# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myResponses.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MyResponsesWindow(object):
    def setupUi(self, MyResponsesWindow):
        if not MyResponsesWindow.objectName():
            MyResponsesWindow.setObjectName(u"MyResponsesWindow")
        MyResponsesWindow.resize(260, 258)
        self.centralWidget = QWidget(MyResponsesWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setGeometry(QRect(0, 0, 258, 254))
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.responseListWidget = QListWidget(self.centralWidget)
        self.responseListWidget.setObjectName(u"responseListWidget")
        self.responseListWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.responseListWidget.sizePolicy().hasHeightForWidth())
        self.responseListWidget.setSizePolicy(sizePolicy)
        self.responseListWidget.setMovement(QListView.Static)

        self.verticalLayout.addWidget(self.responseListWidget)

        self.assignTaskButton = QPushButton(self.centralWidget)
        self.assignTaskButton.setObjectName(u"assignTaskButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.assignTaskButton.sizePolicy().hasHeightForWidth())
        self.assignTaskButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.assignTaskButton)

        self.reportsButton = QPushButton(self.centralWidget)
        self.reportsButton.setObjectName(u"reportsButton")

        self.verticalLayout.addWidget(self.reportsButton)

        self.acceptWorkButton = QPushButton(self.centralWidget)
        self.acceptWorkButton.setObjectName(u"acceptWorkButton")
        sizePolicy1.setHeightForWidth(self.acceptWorkButton.sizePolicy().hasHeightForWidth())
        self.acceptWorkButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.acceptWorkButton)

        self.rejectWorkButton = QPushButton(self.centralWidget)
        self.rejectWorkButton.setObjectName(u"rejectWorkButton")
        sizePolicy1.setHeightForWidth(self.rejectWorkButton.sizePolicy().hasHeightForWidth())
        self.rejectWorkButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.rejectWorkButton)

        self.backButton = QPushButton(self.centralWidget)
        self.backButton.setObjectName(u"backButton")
        sizePolicy1.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.backButton)


        self.retranslateUi(MyResponsesWindow)

        QMetaObject.connectSlotsByName(MyResponsesWindow)
    # setupUi

    def retranslateUi(self, MyResponsesWindow):
        MyResponsesWindow.setWindowTitle(QCoreApplication.translate("MyResponsesWindow", u"TaskHub", None))
        self.assignTaskButton.setText(QCoreApplication.translate("MyResponsesWindow", u"\u041e\u0442\u0434\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443 \u0432 \u0440\u0430\u0431\u043e\u0442\u0443", None))
        self.reportsButton.setText(QCoreApplication.translate("MyResponsesWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043e\u0442\u0447\u0451\u0442\u044b", None))
        self.acceptWorkButton.setText(QCoreApplication.translate("MyResponsesWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.rejectWorkButton.setText(QCoreApplication.translate("MyResponsesWindow", u"\u041e\u0442\u043a\u043b\u043e\u043d\u0438\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0443", None))
        self.backButton.setText(QCoreApplication.translate("MyResponsesWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

