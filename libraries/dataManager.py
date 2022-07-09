# 此模块被设计以用于读取、保存数据到本地，数据以标准 JSON 格式存储。

from json import loads, dumps
from os import path
from datetime import datetime
from localFileFunc import if_file_or_dir_exists, get_sha1
from TempConfing import data_files_json
from Logging import logger


class DataManager:
    """
    这是一个管理数据的类，不太会写，所以基本是乱写的（
    """

    def __init__(self):
        """
        实例化
        """
        self.data = None
        self.normal_data = {"name": "path", "tags": ["tag1", "tag2", "tag3"], "time": "xxxx-xx-xx xx:xx:xx",
                            "sha1": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx忘记总共多少位了 就这样吧 bushi"}
        self.description = None
        self.error_data_list = []
        self.success_data_list = []
        self.tag_index = {}
        self.type_index = {}

        # 如果配置文件不存在则创建空文件
        if not if_file_or_dir_exists(data_files_json):
            temp = open(file=data_files_json, mode="w", encoding="utf-8")
            temp.close()

        # 读取配置文件内容
        with open(file=data_files_json, mode="r", encoding="utf-8") as temp_file:
            self.json_read: dict[str or list[dict[str or list]]] = loads(temp_file.read())

        logger.debug("项目管理器实例化成功。")

    def load(self):
        """
        加载读取到的数据文件，加载完毕后即可进行查询或读取。

        如果是一个空配置文件，或格式有残缺，则会同时写入基础格式信息。

        :return: 此函数返回 self。
        """
        if "description" not in self.json_read:
            self.json_read["description"] = "FanFilesManager"
        self.description: str = self.json_read["description"]

        if "data" not in self.json_read:
            self.json_read[
                "data"] = '[{"name": "path","tags": ["tag1", "tag2", "tag3"],"time": "xxxx-xx-xx xx:xx:xx","sha1": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx（不知道有多少个 忘记了 反正好多好多 bushi"}]'
        self.data: list[dict[str or list]] = self.json_read["data"]

        # 排查格式有误的项目，并对格式正确的项目编制索引
        for data in self.json_read["data"]:
            if "name" not in data or "tags" not in data or "time" not in data or "sha1" not in data:
                self.error_data_list.append(data)
            else:
                self.success_data_list.append(data)

        logger.debug("项目管理器：成功加载本地存储的项目数据。")

        self.make_index()
        self.save()  # 保存到文件
        return self

    def add_project(self, name: str, tags: list[str]):
        """
        向缓存中添加新的项目，需要项目的基本信息和标签。

        :param name: 项目路径。

        :param tags: 项目添加的标签。

        :return: 根据成功与否，此函数返回布尔值。
        """
        # 判断输入的文件路径是否存在
        if not if_file_or_dir_exists(name):
            return False  # 文件不存在，添加失败
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取事件
        sha1_ = get_sha1(name)  # 获取哈希值
        data = {"name": name, "tags": tags, "time": time, "sha1": sha1_}  # 生成字典
        self.success_data_list.append(data)  # 添加进列表
        logger.debug(f"项目管理器：新项目已添加至项目库：{name} 。")
        self.make_index()  # 重新编制索引
        self.save()  # 保存到文件
        return True

    def delete(self, name: str):
        """
        从缓存中删除指定路径的项目。

        :param name: 项目路径。

        :return: 此函数返回 self。
        """
        # 查找指定路径的项目
        delete_data = None
        for data in self.success_data_list:
            if data["name"] == name:
                delete_data = data
                break

        # 如果 delete_data 仍然是 None，说明没有找到
        if not delete_data:
            logger.debug(f"项目管理器：指定项目 {name} 在项目库中不存在。")
        else:
            self.success_data_list.remove(delete_data)
            logger.debug(f"项目管理器：指定项目 {name} 已从项目库删除。")
            self.make_index()
            self.save()
        return self

    def make_index(self):
        """
        为读取到的正确存储数据编制索引。在 self.load() 和 self.add_project() 中已经自动调用此函数。

        索引将缓存在内存中，关闭程序时不会保存，每次启动程序都需要重新编制。索引有利于加快查询速度，但会需要经常更新即重新编制。

        执行此函数后，请读取 self.tag_index 和 self.type_index 两个字典来获取索引；或者通过 self.get_index() 方法获得无首项的两个字典。

        :return: 此函数返回 self。
        """
        # # 按照标签索引
        # 遍历每一个正确的项目
        self.tag_index["无标签"] = []
        for data in self.success_data_list:
            data: dict[str or list]

            # 如果项目没有添加标签则添加到“无标签”中
            if not data["tags"]:
                self.tag_index["无标签"].append(data)
                continue

            # 如果项目添加了标签则遍历项目标签
            for tag in data["tags"]:
                tag: str
                try:  # 尝试对已有的索引添加，索引的本质即一个字典
                    self.tag_index[tag].append(data)
                except Exception:
                    self.tag_index[tag] = [data]

        # # 按照文件格式（后缀）索引
        self.type_index["文件（无后缀）"] = []
        for data in self.success_data_list:
            data: dict[str or list]

            # 分离文件名与后缀，suf 的值就是文件后缀名
            suf = path.splitext(path.split(data["name"])[1])[1]

            # 如果莫有后缀就是无后缀（？听君一席话，……
            if suf == "":
                self.type_index["文件（无后缀）"].append(data)

            # 下面是对各个不同后缀的划分
            elif suf in [".jpg", ".png", ".jpeg", ".gif"]:  # 图片
                try:
                    self.type_index["图片图像"].append(data)
                except Exception:
                    self.type_index["图片图像"] = [data]
            elif suf in [".mp3", ".flac", ".wav"]:  # 音频
                try:
                    self.type_index["音乐音效"].append(data)
                except Exception:
                    self.type_index["音乐音效"] = [data]
            elif suf in [".mp4", ".mov", ".flv"]:  # 视频
                try:
                    self.type_index["视频影片"].append(data)
                except Exception:
                    self.type_index["视频影片"] = [data]
            elif suf in [".txt", ".word", ".rtf"]:  # 文档
                try:
                    self.type_index["文本文档"].append(data)
                except Exception:
                    self.type_index["文本文档"] = [data]
            else:  # 其他后缀
                try:
                    self.type_index["其他格式"].append(data)
                except Exception:
                    self.type_index["其他格式"] = [data]
        logger.debug("项目管理器：索引编制完毕。")
        return self

    def get_index(self):
        """
        获取两个索引字典，但是没有首项（名称为‘path’的删不掉的那个文件）。

        :return: 返回两个索引字典。
        """
        temp_list = []
        tag_index = self.tag_index
        try:
            tag_index["tag1"].remove(self.normal_data)
        except:
            pass
        try:
            tag_index["tag2"].remove(self.normal_data)
        except:
            pass
        try:
            tag_index["tag3"].remove(self.normal_data)
        except:
            pass
        for datas in tag_index.keys():  # 循环查找无意义的空列表
            if not tag_index[datas]:
                temp_list.append(datas)
        for datas in temp_list:  # 清除
            tag_index.pop(datas)
        temp_list.clear()
        type_index = self.type_index
        try:
            type_index["文件（无后缀）"].remove(self.normal_data)
        except:
            pass
        for datas in type_index.keys():
            if not type_index[datas]:
                temp_list.append(datas)
        for datas in temp_list:
            type_index.pop(datas)
        return tag_index, type_index

    def get_success_list(self):
        """
        获取正确的项目列表，不包括删不掉的那个（

        :return: 返回一个列表。
        """
        temp_list = self.success_data_list
        if self.normal_data in temp_list:
            temp_list.remove(self.normal_data)
        return temp_list

    def save(self):
        """
        将现在缓存中的数据信息存储入文件。在 self.load() 和 self.add_project() 中已经自动调用此函数。

        在对缓存进行变动操作时经常调用此方法可以缓解因程序崩溃、出现异常等事故时的数据损坏程度。

        :return: 此函数返回 self。
        """
        # # 将所有 self.success_data_list 中的 data 全部写入文件
        # 首先读取一遍
        with open(file=data_files_json, mode="r", encoding="utf-8") as temp_file:
            self.json_read = loads(temp_file.read())
            # 循环确认文件中的所有数据都是正确的
            for data in self.json_read["data"]:
                if not if_file_or_dir_exists(data["name"]):
                    self.json_read["data"].remove(data)
            # 循环确认所有缓存中正确的数据都已被写入
            for data in self.success_data_list:
                if data not in self.json_read["data"]:
                    self.json_read["data"].append(data)

        # 然后再写入
        with open(file=data_files_json, mode="w", encoding="utf-8") as temp_file:
            temp_file.write(dumps(self.json_read))

        logger.debug("项目管理器：项目库已存储至文件。")
        return self
