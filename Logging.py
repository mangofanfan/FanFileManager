# 日志配置文件

import logging
from os.path import split
from TempConfing import data_log_path
from localFileFunc import if_file_or_dir_exists, make_dirs_exist

logger = logging.getLogger("Main")

handler1 = logging.StreamHandler()
if not if_file_or_dir_exists(split(data_log_path)[0], False):
    make_dirs_exist(split(data_log_path)[0])
handler2 = logging.FileHandler(filename=data_log_path, encoding="utf-8", mode="w")

logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.DEBUG)
handler2.setLevel(logging.NOTSET)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] : %(message)s",
                              datefmt="%H:%M:%S")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)
