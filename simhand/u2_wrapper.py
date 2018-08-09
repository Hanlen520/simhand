"""
server与uiautomator2的连接层
将server的指令转换成实际的动作 操作设备
"""
import uiautomator2 as u2
import subprocess
import time
from requests.exceptions import ConnectionError
from urllib3.exceptions import ProtocolError
from simhand.config import logger


class U2Wrapper(object):
    def __init__(self, device_id):
        # TODO 实际上每次都init太慢 但是不init会有断开的风险 正式环境需要在uiautomator2中增加一个restart方法
        try:
            self.device = u2.connect(device_id)
            self.device.current_app()
        except (ConnectionError, ConnectionResetError, ProtocolError):
            _cmd_list = ['python', '-m', 'uiautomator2', 'init', device_id]
            logger.info('U2 is down, RESTART', cmd=_cmd_list)
            subprocess.run(_cmd_list, shell=True)
            time.sleep(2)
            self.device = u2.connect(device_id)

    def click_widget_by_text(self, action_args):
        if 'widgetText' not in action_args:
            return 'no widgetText'
        widget_text = action_args['widgetText']
        try:
            self.device(text=widget_text).click(timeout=1)
            feedback = 'clicked'
        except u2.UiObjectNotFoundError:
            feedback = 'not found'
        return feedback

    def click_widget_by_id(self, action_args):
        if 'widgetId' not in action_args:
            return 'no widgetId'
        widget_id = action_args['widgetId']
        try:
            self.device(id=widget_id).click(timeout=1)
            feedback = 'clicked'
        except u2.UiObjectNotFoundError:
            feedback = 'not found'
        return feedback
