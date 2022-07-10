# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_addFile.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_addFile(object):
    def setupUi(self, Form_addFile):
        if not Form_addFile.objectName():
            Form_addFile.setObjectName(u"Form_addFile")
        Form_addFile.resize(632, 233)
        self.horizontalLayoutWidget = QWidget(Form_addFile)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 611, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_name = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout.addWidget(self.lineEdit_name)

        self.label_fileName = QLabel(Form_addFile)
        self.label_fileName.setObjectName(u"label_fileName")
        self.label_fileName.setGeometry(QRect(100, 60, 511, 20))
        self.horizontalLayoutWidget_2 = QWidget(Form_addFile)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 90, 611, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_tags = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_tags.setObjectName(u"lineEdit_tags")

        self.horizontalLayout_2.addWidget(self.lineEdit_tags)

        self.label_3 = QLabel(Form_addFile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 130, 511, 16))
        self.label_4 = QLabel(Form_addFile)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 81, 16))
        self.label_5 = QLabel(Form_addFile)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 190, 81, 16))
        self.label_time = QLabel(Form_addFile)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(90, 170, 391, 16))
        self.label_sha1 = QLabel(Form_addFile)
        self.label_sha1.setObjectName(u"label_sha1")
        self.label_sha1.setGeometry(QRect(90, 190, 391, 16))
        self.pushButton_confirm = QPushButton(Form_addFile)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setGeometry(QRect(520, 160, 93, 28))
        self.pushButton_cancel = QPushButton(Form_addFile)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(520, 190, 93, 28))

        self.retranslateUi(Form_addFile)

        QMetaObject.connectSlotsByName(Form_addFile)
    # setupUi

    def retranslateUi(self, Form_addFile):
        Form_addFile.setWindowTitle(QCoreApplication.translate("Form_addFile", u"\u6dfb\u52a0\u5355\u4e2a\u9879\u76ee | \u5e06\u5f0f\u6587\u4ef6\u7ba1\u7406\u5668", None))
        self.label.setText(QCoreApplication.translate("Form_addFile", u"\u9879\u76ee\u8def\u5f84 |", None))
        self.label_fileName.setText(QCoreApplication.translate("Form_addFile", u"\u672a\u6307\u5b9a", None))
        self.label_2.setText(QCoreApplication.translate("Form_addFile", u"\u9879\u76ee\u6807\u7b7e |", None))
        self.label_3.setText(QCoreApplication.translate("Form_addFile", u"\u591a\u4e2a\u6807\u7b7e\u4e4b\u95f4\u4f7f\u7528\u534a\u89d2\u9017\u53f7\uff08,\uff09\u5206\u9694\uff0c\u5373\u82f1\u6587\u9017\u53f7\uff0c\u4e5f\u53ef\u4ee5\u4e0d\u6dfb\u52a0\u6807\u7b7e", None))
        self.label_4.setText(QCoreApplication.translate("Form_addFile", u"\u6dfb\u52a0\u65f6\u95f4 |", None))
        self.label_5.setText(QCoreApplication.translate("Form_addFile", u"\u6587\u4ef6\u54c8\u5e0c |", None))
        self.label_time.setText(QCoreApplication.translate("Form_addFile", u"\u8ba1\u7b97\u4e2d", None))
        self.label_sha1.setText(QCoreApplication.translate("Form_addFile", u"\u8ba1\u7b97\u4e2d", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("Form_addFile", u"\u786e\u8ba4\u6dfb\u52a0", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Form_addFile", u"\u53d6\u6d88\u6dfb\u52a0", None))
    # retranslateUi

