from os import makedirs
from pathlib import Path
from hashlib import sha1


def if_file_or_dir_exists(file_path: str, is_file: bool = True):
    """
    此函数用于确认指定的文件或目录是否存在。

    :param file_path: 路径。

    :param is_file: 是否是文件，默认为 True 即为是，如果为 False 即为目录。

    :return: 如果存在则返回 True，否则返回 False。
    """
    path = Path(file_path)
    if is_file:
        if path.is_file():
            return True
        else:
            return False

    else:
        if path.is_dir():
            return True
        else:
            return False


def make_dirs_exist(dirs_path):
    """
    此函数可以按路径创建完整的目录，如果目录已经存在则不创建。

    :param dirs_path: 需要创建的目录路径。是目录！目录！！目录！！！不是文件！！！！

    :return: 这是一个方法，要什么返回值，返回什么东西根本不重要。
    """
    if if_file_or_dir_exists(dirs_path, False):
        return None

    makedirs(name=dirs_path)
    return None


def get_sha1(name: str):
    """
    获取指定目标的 sha1 值。

    :param name: 目标文件路径。

    :return: 返回字符串，即 sha1 的字符串；如果文件不存在，返回 None。
    """
    if not if_file_or_dir_exists(name):
        return None
    temp_file = open(file=name, mode="rb")
    sha1_ = sha1(temp_file.read())
    temp_file.close()
    return sha1_.hexdigest()
