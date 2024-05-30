# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewPublicTask.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_ViewPublicTaskWindow(object):
    def setupUi(self, ViewPublicTaskWindow):
        if not ViewPublicTaskWindow.objectName():
            ViewPublicTaskWindow.setObjectName(u"ViewPublicTaskWindow")
        ViewPublicTaskWindow.resize(800, 600)
        self.backToMenuButton = QPushButton(ViewPublicTaskWindow)
        self.backToMenuButton.setObjectName(u"backToMenuButton")
        self.backToMenuButton.setGeometry(QRect(50, 30, 80, 24))
        self.taskListWidget = QListWidget(ViewPublicTaskWindow)
        self.taskListWidget.setObjectName(u"taskListWidget")
        self.taskListWidget.setGeometry(QRect(50, 70, 691, 441))

        self.retranslateUi(ViewPublicTaskWindow)

        QMetaObject.connectSlotsByName(ViewPublicTaskWindow)
    # setupUi

    def retranslateUi(self, ViewPublicTaskWindow):
        ViewPublicTaskWindow.setWindowTitle(QCoreApplication.translate("ViewPublicTaskWindow", u"TaskHub", None))
        self.backToMenuButton.setText(QCoreApplication.translate("ViewPublicTaskWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

