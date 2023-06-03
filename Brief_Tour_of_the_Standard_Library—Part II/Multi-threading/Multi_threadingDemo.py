import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

import AsyncZip
from Config.Config import path


def Demo():
    background = AsyncZip.AsyncZip(
        path + "Brief_Tour_of_the_Standard_Library—Part II\Multi-threading\Photo.txt",
        path + "Brief_Tour_of_the_Standard_Library—Part II\Multi-threading\Photo.rar",
    )
    background.start()
    print("Vẫn tiếp tục chép ảnh dưới nền")
    background.join()
    print("Hoàn thành chép ảnh")
