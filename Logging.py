# 日志配置文件

import logging
from TempConfing import data_log_path

logger = logging.getLogger("Main")

handler1 = logging.StreamHandler()
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
