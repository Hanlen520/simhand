"""
python example
"""
import requests
import json


PC_IP = 'http://172.17.152.193:9507'
SCREEN_SHOT_API = '/api/screenshot'
UI_AUTO_API = '/api/ui_auto'


def get_screen_shot(pic_name, device_id):
    requests.get(
        url=PC_IP + SCREEN_SHOT_API,
        params={
            'name': pic_name,
            'deviceId': device_id,
        },
    )


def ui_action(action_name, action_args, device_id):
    requests.get(
        url=PC_IP + UI_AUTO_API,
        params={
            'actionName': action_name,
            'actionArgs': action_args,
            'deviceId': device_id,
        },
    )


if __name__ == '__main__':
    ui_action(
        action_name='click_widget_by_text',
        action_args=json.dumps({
            'widgetText': '微信',
        }),
        device_id='9c12aa96',
    )
