"""
对外界指令响应
- 转发到指定模块处理
- 将处理结果返回到外界

现有功能
- 操作截图
- 操作UI自动化框架
"""
from simhand.config import logger
from simhand.u2_wrapper import U2Wrapper
import subprocess


def screen_shot(device_id, pic_name):
    """
    操作截图

    :param device_id: 设备ID，与adb devices得到的ID一致
    :param pic_name: 截图保存的真实路径及文件名（保存在手机中）
    :return:
    """
    shot_cmd_list = ['adb', '-s', device_id, 'shell', 'screencap', '-p', pic_name]
    logger.info('SCREEN SHOT CMD', cmd=' '.join(shot_cmd_list))
    screen_shot_completed_process = subprocess.run(shot_cmd_list, stdout=subprocess.PIPE)
    screen_shot_result = screen_shot_completed_process.stdout.decode()
    logger.info('SCREEN SHOT RESULT', result=screen_shot_result or 'None')
    return screen_shot_result or 'None'


def ui(device_id, action_name, action_args):
    """
    ui操作，通过uiautomator2，详见u2_wrapper.py

    :param device_id:
    :param action_name:
    :param action_args:
    :return:
    """
    u2_object = U2Wrapper(device_id)
    if not hasattr(u2_object, action_name):
        return 'no action called {}'.format(action_name)
    return getattr(u2_object, action_name)(action_args)
