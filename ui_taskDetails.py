# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskDetails.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TaskDetailsWindow(object):
    def setupUi(self, TaskDetailsWindow):
        if not TaskDetailsWindow.objectName():
            TaskDetailsWindow.setObjectName(u"TaskDetailsWindow")
        TaskDetailsWindow.resize(400, 300)
        self.verticalLayout = QVBoxLayout(TaskDetailsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(TaskDetailsWindow)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.descriptionLabel = QLabel(TaskDetailsWindow)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.createdAtLabel = QLabel(TaskDetailsWindow)
        self.createdAtLabel.setObjectName(u"createdAtLabel")

        self.verticalLayout.addWidget(self.createdAtLabel)

        self.startDateLabel = QLabel(TaskDetailsWindow)
        self.startDateLabel.setObjectName(u"startDateLabel")

        self.verticalLayout.addWidget(self.startDateLabel)

        self.deadlineLabel = QLabel(TaskDetailsWindow)
        self.deadlineLabel.setObjectName(u"deadlineLabel")

        self.verticalLayout.addWidget(self.deadlineLabel)

        self.completedAtLabel = QLabel(TaskDetailsWindow)
        self.completedAtLabel.setObjectName(u"completedAtLabel")

        self.verticalLayout.addWidget(self.completedAtLabel)

        self.closeButton = QPushButton(TaskDetailsWindow)
        self.closeButton.setObjectName(u"closeButton")

        self.verticalLayout.addWidget(self.closeButton)


        self.retranslateUi(TaskDetailsWindow)

        QMetaObject.connectSlotsByName(TaskDetailsWindow)
    # setupUi

    def retranslateUi(self, TaskDetailsWindow):
        TaskDetailsWindow.setWindowTitle(QCoreApplication.translate("TaskDetailsWindow", u"\u0414\u0435\u0442\u0430\u043b\u0438 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.closeButton.setText(QCoreApplication.translate("TaskDetailsWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

