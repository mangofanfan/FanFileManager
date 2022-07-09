# 窗口控制

from PySide2.QtWidgets import QWidget, QAbstractItemView
from Form_addFile import Ui_Form_addFile
from Form_Homepage import Ui_Form_Homepage


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


class Form_addFile(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_addFile()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
