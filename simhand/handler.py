""" handler for router """
from tornado.web import RequestHandler
from simhand.logger import logger
from simhand import forward
import json

# STATUS
RESULT_OK = 1000
RESULT_ERROR = 1001


class BaseHandler(RequestHandler):
    def set_default_headers(self):
        """ 主要为与vue应用通信 """
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    def end_with_json(self, code, data=None, message=None):
        """ 规范服务器返回 """
        request_url = self.request.uri
        result_dict = {
            'code': code,
            'data': data or {},
            'message': message or {},
        }
        logger.info('REQUEST END', code=code, data=data, message=message, request_url=request_url)
        self.finish(result_dict)


class IndexHandler(BaseHandler):
    """ default """
    def get(self):
        self.end_with_json(RESULT_OK, message='SIMHAND ALIVE :)')

    def post(self):
        self.end_with_json(RESULT_OK, message='SIMHAND ALIVE :)')


class ScreenShotHandler(BaseHandler):
    def get(self):
        # 得到 设备ID 与 截图保存名称
        arg_dict = self.request.arguments
        logger.info('GET SCREENSHOT', args=arg_dict)
        pic_name = arg_dict['name'][0].decode()
        device_id = arg_dict['deviceId'][0].decode()
        # 正式截图
        shot_result = forward.screen_shot(device_id, pic_name)
        # 返回截图结果
        self.end_with_json(RESULT_OK, message=shot_result)

    def post(self):
        self.end_with_json(RESULT_ERROR, message='Not Implemented Yet')


class UIAutoHandler(BaseHandler):
    def get(self):
        # 获取动作名称 动作参数 设备编号
        arg_dict = self.request.arguments
        logger.info('GET UIAUTOACTION', args=arg_dict)
        action_name = arg_dict['actionName'][0].decode()
        action_args = json.loads(arg_dict['actionArgs'][0].decode())
        device_id = arg_dict['deviceId'][0].decode()
        # ui操作
        ui_result = forward.ui(device_id, action_name, action_args)
        self.end_with_json(RESULT_OK, message=ui_result)

    def post(self):
        self.end_with_json(RESULT_ERROR, message='Not Implemented Yet')


class AQubeHandler(BaseHandler):
    def get(self):
        arg_dict = self.request.arguments
        logger.info('GET AQUBE', args=arg_dict)
        action_name = arg_dict['actionName'][0].decode()
        action_args = json.loads(arg_dict['actionArgs'][0].decode())
        aqube_result = forward.aqube(action_name, action_args)
        self.end_with_json(RESULT_OK, message=aqube_result)

    def post(self):
        self.end_with_json(RESULT_ERROR, message='Not Implemented Yet')
