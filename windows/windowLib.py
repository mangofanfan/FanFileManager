# 窗口控制

from PySide2.QtWidgets import QWidget, QAbstractItemView
from PySide2.QtGui import QIcon
from Form_addFile import Ui_Form_addFile
from Form_addFiles import Ui_Form_addFiles
from Form_Homepage import Ui_Form_Homepage
from TempConfing import data_window_icon


class Form_Homepage(QWidget):
    """
    继承 UI
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_Homepage()
        self.ui.setupUi(self)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止用户从 GUI 编辑表格
        self.ui.tableWidget.verticalHeader().setHidden(True)  # 隐藏表格前的序号
        self.ui.tableWidget_index.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_index.verticalHeader().setHidden(True)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon(data_window_icon))  # 设置窗口 logo


class Form_addFile(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_addFile()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon(data_window_icon))


class Form_addFiles(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_addFiles()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.tableWidget.verticalHeader().setHidden(True)
        self.setWindowIcon(QIcon(data_window_icon))
