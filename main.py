"""
本软件的开发目标是，让使用者能够通过此软件，方便快捷地管理自己的本地[素材]文件。
无论是图片、视频、音频、文档等资源，都能够做到准确识别、自动分类，并允许用户手动添加标签。
其实主要是开发给自己用的，但是如果效果可以的话，也会开源发布~
本项目的开发将在一定程度上为 帆式启动器 Fan Craft Launcher 的开发提供指导（我抄我自己 bushi
作者：芒果帆帆w（MangoFanFan）
"""
from dataManager import DataManager
from localFileFunc import get_sha1
from windowLib import Form_Homepage, Form_addFile, Form_addFiles
from PySide2.QtWidgets import QFileDialog, QMainWindow, QApplication, QTableWidgetItem
from sys import argv, exit
from os.path import split
from Logging import logger

logger.info("各模块导入正常。")


def main():
    """
    主函数
    """
    global temp
    global window
    logger.debug("全局变量 temp window 声明完毕。")

    manager = DataManager()  # 实例化项目管理器
    manager.load()  # 加载本地存储项目
    app = QApplication(argv)  # 启动窗口
    window = Form_Homepage()

    def ChooseFile():  # 窗口绑定的函数无法传入值
        """
        打开文件选择框，选择指定的单个文件作为项目添加。

        :return: 不返回值。
        """

        def add():
            """
            将选中的文件添加到项目库中。

            :return: 不返回值啦。
            """
            manager.add_project(file_name, temp.ui.lineEdit_tags.text().split(","))
            temp.close()
            return None

        file_name = QFileDialog.getOpenFileName(QMainWindow(), "选择需要添加索引的项目...")[0]
        if not file_name:
            return None  # 如果用户没有选择文件就直接关闭，直接退出此方法
        temp = Form_addFile()
        temp.ui.lineEdit_name.setText(file_name)
        temp.ui.label_fileName.setText(split(file_name)[1])
        temp.ui.label_time.setText("以确认时的系统时间为准...")
        temp.ui.label_sha1.setText(get_sha1(file_name))
        temp.ui.pushButton_confirm.clicked.connect(add)  # 确认按钮绑定添加到项目库函数
        temp.ui.pushButton_cancel.clicked.connect(temp.close)
        temp.show()
        return None  # 窗口绑定的函数无法返回值

    def ChooseFiles():  # 窗口绑定的函数无法传入值
        """
        打开文件选择框，选择多个指定的文件作为项目添加。

        :return: 不返回值。
        """

        def add():
            """
            将选中的文件添加到项目库中。

            :return: 不返回值啦。
            """
            for i in range(num):
                manager.add_project(temp.ui.tableWidget.item(i, 3).text(), temp.ui.tableWidget.item(i, 1).text().split(","))
            temp.close()
            return None

        file_names = QFileDialog.getOpenFileNames(QMainWindow(), "选择需要添加索引的项目...")[0]
        if not file_names:
            return None  # 如果用户没有选择文件就直接关闭，直接退出此方法
        temp = Form_addFiles()
        temp.ui.pushButton_confirm.clicked.connect(add)  # 确认按钮绑定添加到项目库函数
        temp.ui.pushButton_cancel.clicked.connect(temp.close)

        # 循环所有选择的项目，将基本信息打印到表格内
        num = 0
        count = len(file_names)
        temp.ui.tableWidget.setRowCount(count)  # 设置表格行数
        for data in file_names:
            name = split(data)[1]
            temp.ui.tableWidget.setItem(num, 0, QTableWidgetItem(name))
            temp.ui.tableWidget.setItem(num, 3, QTableWidgetItem(data))
            sha1 = get_sha1(data)
            temp.ui.tableWidget.setItem(num, 2, QTableWidgetItem(sha1))
            num = num + 1
        temp.show()
        return None  # 窗口绑定的函数无法返回值

    def UpdateTable():
        """
        刷新列表（其实是表格）中的信息，每次更改变动项目库中的内容时都需要刷新。

        :return: 不返回值呐！
        """
        logger.debug("方法：刷新 GUI 显示的项目库。")
        global window
        logger.debug("全局变量 window 声明完毕。")
        row = len(manager.get_success_list())
        window.ui.tableWidget.setRowCount(row)
        num = 0
        for data in manager.success_data_list:  # 循环，把项目库中所有信息打印进表格
            window.ui.tableWidget.setItem(num, 0, QTableWidgetItem(split(data["name"])[1]))  # 表格第一列显示项目名
            window.ui.tableWidget.setItem(num, 1, QTableWidgetItem(",".join(data["tags"])))  # 第二列显示标签
            window.ui.tableWidget.setItem(num, 2, QTableWidgetItem(data["time"]))  # 第三列显示时间
            window.ui.tableWidget.setItem(num, 3, QTableWidgetItem(data["sha1"]))  # 第四列显示 sha1
            num = num + 1
        tag_index, type_index = manager.get_index()
        count = max(len(tag_index), len(type_index))
        window.ui.tableWidget_index.setRowCount(count)
        num = 0
        for tag in tag_index.keys():
            window.ui.tableWidget_index.setItem(num, 0, QTableWidgetItem(tag))
            num = num + 1
        num = 0
        for type_ in type_index.keys():
            window.ui.tableWidget_index.setItem(num, 1, QTableWidgetItem(type_))
            num = num + 1

        logger.info("GUI 显示的项目库刷新完毕。")
        return None

    UpdateTable()  # 更新一次表格信息
    window.ui.pushButton_addFile.clicked.connect(ChooseFile)  # 绑定添加单个项目函数
    window.ui.pushButton_addFiles.clicked.connect(ChooseFiles)  # 绑定添加多个项目函数
    window.ui.pushButton_Update.clicked.connect(UpdateTable)
    window.show()
    logger.info("FFM 进入逻辑循环，现在是您的主场。")
    exit_code = app.exec_()  # 关闭窗口
    logger.info("逻辑循环已经退出，正在保存项目库至文件。")
    manager.save()
    logger.info("进程结束，感谢使用。")
    logger.info("——帆式文件管理器 | Fan File Manager")
    logger.info("——作者/Made by 芒果帆帆/MangoFanFan")
    return exit_code


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
