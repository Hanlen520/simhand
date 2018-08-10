""" global config """
import os
from simhand.logger import logger


# 项目根目录
ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# SIMHAND 项目目录
PROJECT_PATH = os.path.join(ROOT_PATH, 'simhand')
# AQUBE_CORE 项目目录
AQUBE_PATH = os.path.join(ROOT_PATH, 'AQube_Core')
# AQUBE_CORE 入口文件
AQUBE_RUN = os.path.join(AQUBE_PATH, 'run.py')
# AQUBE_CORE URL
AQUBE_URL = 'https://github.com/williamfzc/AQube_Core.git'


# TORNADO 配置
TORNADO_SETTING = {
    'debug': True,
    'static_path': os.path.join(PROJECT_PATH, "static"),
    'template_path': os.path.join(PROJECT_PATH, "template"),
}
TORNADO_PORT = 9507

logger.info('ROOT PATH', root_path=ROOT_PATH)
logger.info('PROJECT PATH', project_path=PROJECT_PATH)
logger.info('PORT', port=TORNADO_PORT)
logger.info('AQUBE PATH', aqube_core=AQUBE_PATH)
