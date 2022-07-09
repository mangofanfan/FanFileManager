# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_Homepage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Homepage(object):
    def setupUi(self, Form_Homepage):
        if not Form_Homepage.objectName():
            Form_Homepage.setObjectName(u"Form_Homepage")
        Form_Homepage.setEnabled(True)
        Form_Homepage.resize(1184, 677)
        self.verticalLayoutWidget = QWidget(Form_Homepage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 80, 261, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_addFile = QPushButton(self.verticalLayoutWidget)
        self.pushButton_addFile.setObjectName(u"pushButton_addFile")
        font = QFont()
        font.setPointSize(10)
        self.pushButton_addFile.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_addFile)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.pushButton_addFiles = QPushButton(self.verticalLayoutWidget)
        self.pushButton_addFiles.setObjectName(u"pushButton_addFiles")
        self.pushButton_addFiles.setEnabled(True)
        self.pushButton_addFiles.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_addFiles)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.pushButton_addAllInDire = QPushButton(self.verticalLayoutWidget)
        self.pushButton_addAllInDire.setObjectName(u"pushButton_addAllInDire")

        self.verticalLayout.addWidget(self.pushButton_addAllInDire)

        self.label = QLabel(Form_Homepage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 421, 41))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.tableWidget = QTableWidget(Form_Homepage)
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
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(280, 80, 721, 591))
        self.lineEdit = QLineEdit(Form_Homepage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(470, 30, 411, 31))
        self.pushButton_search = QPushButton(Form_Homepage)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(890, 30, 111, 31))
        self.gridLayoutWidget = QWidget(Form_Homepage)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(4, 609, 271, 65))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_about = QPushButton(self.gridLayoutWidget)
        self.pushButton_about.setObjectName(u"pushButton_about")

        self.gridLayout.addWidget(self.pushButton_about, 2, 0, 1, 1)

        self.pushButton_wiki = QPushButton(self.gridLayoutWidget)
        self.pushButton_wiki.setObjectName(u"pushButton_wiki")

        self.gridLayout.addWidget(self.pushButton_wiki, 2, 1, 1, 1)

        self.pushButton_setting = QPushButton(self.gridLayoutWidget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")

        self.gridLayout.addWidget(self.pushButton_setting, 1, 0, 1, 2)

        self.pushButton_Update = QPushButton(Form_Homepage)
        self.pushButton_Update.setObjectName(u"pushButton_Update")
        self.pushButton_Update.setGeometry(QRect(1010, 30, 171, 31))
        self.tableWidget_index = QTableWidget(Form_Homepage)
        if (self.tableWidget_index.columnCount() < 2):
            self.tableWidget_index.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_index.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_index.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget_index.setObjectName(u"tableWidget_index")
        self.tableWidget_index.setGeometry(QRect(10, 270, 261, 331))
        self.pushButton = QPushButton(Form_Homepage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1010, 80, 171, 41))
        font2 = QFont()
        font2.setPointSize(9)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(Form_Homepage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1010, 140, 171, 41))
        self.pushButton_2.setFont(font2)
        self.groupBox = QGroupBox(Form_Homepage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(1010, 190, 171, 481))
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 70, 171, 41))
        self.pushButton_3.setFont(font2)
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 120, 171, 41))
        self.pushButton_4.setFont(font2)
        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(0, 170, 171, 41))
        self.pushButton_5.setFont(font2)
        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 220, 171, 41))
        self.pushButton_6.setFont(font2)
        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(0, 20, 171, 41))
        self.pushButton_7.setFont(font2)
        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 270, 171, 211))
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.pushButton_addFile)
        self.label_3.setBuddy(self.pushButton_addFiles)
        self.label_4.setBuddy(self.pushButton_addAllInDire)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form_Homepage)

        QMetaObject.connectSlotsByName(Form_Homepage)
    # setupUi

    def retranslateUi(self, Form_Homepage):
        Form_Homepage.setWindowTitle(QCoreApplication.translate("Form_Homepage", u"\u5e06\u5f0f\u6587\u4ef6\u7ba1\u7406\u5668", None))
        self.label_2.setText(QCoreApplication.translate("Form_Homepage", u"\u9009\u4e2d\u4e00\u4e2a\u6587\u4ef6\u5e76\u6dfb\u52a0", None))
        self.pushButton_addFile.setText(QCoreApplication.translate("Form_Homepage", u"\u6dfb\u52a0\u5355\u4e2a\u9879\u76ee", None))
        self.label_3.setText(QCoreApplication.translate("Form_Homepage", u"\u9009\u4e2d\u591a\u4e2a\u6587\u4ef6\u6279\u6b21\u6dfb\u52a0", None))
        self.pushButton_addFiles.setText(QCoreApplication.translate("Form_Homepage", u"\u6dfb\u52a0\u591a\u4e2a\u9879\u76ee", None))
        self.label_4.setText(QCoreApplication.translate("Form_Homepage", u"\u9009\u4e2d\u6587\u4ef6\u5939\u5185\u7684\u6240\u6709\u6587\u4ef6\u6dfb\u52a0", None))
        self.pushButton_addAllInDire.setText(QCoreApplication.translate("Form_Homepage", u"\u6dfb\u52a0\u6587\u4ef6\u5939\u5185\u7684\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Form_Homepage", u"\u5e06\u5f0f\u6587\u4ef6\u7ba1\u7406\u5668 | Fan File Manager", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form_Homepage", u"\u9879\u76ee\u6587\u4ef6", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form_Homepage", u"\u9879\u76ee\u6807\u7b7e", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form_Homepage", u"\u6dfb\u52a0\u65f6\u95f4", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form_Homepage", u"\u54c8\u5e0c\uff08sha1\uff09", None));
        self.pushButton_search.setText(QCoreApplication.translate("Form_Homepage", u"\u9879\u76ee\u67e5\u627e", None))
        self.pushButton_about.setText(QCoreApplication.translate("Form_Homepage", u"\u5173\u4e8e\u672c\u7a0b\u5e8f", None))
        self.pushButton_wiki.setText(QCoreApplication.translate("Form_Homepage", u"\u7a0b\u5e8f wiki", None))
        self.pushButton_setting.setText(QCoreApplication.translate("Form_Homepage", u"\u504f\u597d\u8bbe\u7f6e", None))
        self.pushButton_Update.setText(QCoreApplication.translate("Form_Homepage", u"\u5237\u65b0\u9879\u76ee\u5e93", None))
        ___qtablewidgetitem4 = self.tableWidget_index.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form_Homepage", u"\u6807\u7b7e\u96c6", None));
        ___qtablewidgetitem5 = self.tableWidget_index.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form_Homepage", u"\u683c\u5f0f\u96c6", None));
        self.pushButton.setText(QCoreApplication.translate("Form_Homepage", u"\u7f16\u8f91", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form_Homepage", u"\u5220\u9664", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form_Homepage", u"\u6587\u4ef6\u64cd\u4f5c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form_Homepage", u"\u590d\u5236\u5230...", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form_Homepage", u"\u79fb\u52a8\u5230...", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form_Homepage", u"\u538b\u7f29\u4e3a...", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form_Homepage", u"\u91cd\u547d\u540d...", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form_Homepage", u"\u5217\u5165\u9009\u62e9\u6846", None))
    # retranslateUi

