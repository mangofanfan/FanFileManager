# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_addFiles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_addFiles(object):
    def setupUi(self, Form_addFiles):
        if not Form_addFiles.objectName():
            Form_addFiles.setObjectName(u"Form_addFiles")
        Form_addFiles.resize(568, 459)
        self.tableWidget = QTableWidget(Form_addFiles)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 50, 551, 341))
        self.label = QLabel(Form_addFiles)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 511, 21))
        self.label_2 = QLabel(Form_addFiles)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 420, 91, 16))
        self.label_count = QLabel(Form_addFiles)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setGeometry(QRect(120, 420, 91, 16))
        self.pushButton_cancel = QPushButton(Form_addFiles)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(410, 410, 151, 41))
        self.pushButton_confirm = QPushButton(Form_addFiles)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setGeometry(QRect(240, 410, 151, 41))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.tableWidget)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form_addFiles)

        QMetaObject.connectSlotsByName(Form_addFiles)
    # setupUi

    def retranslateUi(self, Form_addFiles):
        Form_addFiles.setWindowTitle(QCoreApplication.translate("Form_addFiles", u"\u6dfb\u52a0\u591a\u4e2a\u9879\u76ee | \u5e06\u5f0f\u6587\u4ef6\u7ba1\u7406\u5668", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_addFiles", u"\u9879\u76ee\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_addFiles", u"\u6807\u7b7e\uff08\u9700\u8981\u7f16\u8f91", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_addFiles", u"\u54c8\u5e0c\uff08sha1\uff09", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_addFiles", u"\u9879\u76ee\u8def\u5f84", None));
        self.label.setText(QCoreApplication.translate("Form_addFiles", u"\u5728\u4e0b\u65b9\u8868\u683c\u4e2d\u7f16\u8f91\u6bcf\u4e00\u4e2a\u9879\u76ee\u7684\u6807\u7b7e\uff0c\u7136\u540e\u9009\u62e9 \u786e\u8ba4\u6dfb\u52a0 \u4ee5\u8fdb\u884c\u64cd\u4f5c\u3002", None))
        self.label_2.setText(QCoreApplication.translate("Form_addFiles", u"\u9009\u4e2d\u9879\u76ee\u6570 |", None))
        self.label_count.setText(QCoreApplication.translate("Form_addFiles", u"\u672a\u6307\u5b9a", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Form_addFiles", u"\u53d6\u6d88\u6dfb\u52a0", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("Form_addFiles", u"\u786e\u8ba4\u6dfb\u52a0", None))
    # retranslateUi

