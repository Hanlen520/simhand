"""
python example
"""
import requests
import json


PC_IP = 'http://localhost:9507'
SCREEN_SHOT_API = '/api/screenshot'
UI_AUTO_API = '/api/ui_auto'
AQUBE_API = '/api/aqube'


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


def apply_aqube_action(action_name, action_args):
    requests.get(
        url=PC_IP + AQUBE_API,
        params={
            'actionName': action_name,
            'actionArgs': action_args,
        }
    )


if __name__ == '__main__':
    # ui_action(
    #     action_name='click_widget_by_text',
    #     action_args=json.dumps({
    #         'widgetText': '微信',
    #     }),
    #     device_id='9c12aa96',
    # )

    apply_aqube_action(
        action_name='setting',
        action_args=json.dumps({
            'device': '9c12aa96',
            'action': 'airplane_on',
        }),
    )
