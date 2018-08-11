""" router """
from simhand.handler import *


TORNADO_ROUTER = [
    (r"/", IndexHandler),

    # 交互 暂且提供截图与ui控制作为例子
    (r"/api/screenshot", ScreenShotHandler),
    (r"/api/ui_auto", UIAutoHandler),
    (r"/api/aqube", AQubeHandler),
]
