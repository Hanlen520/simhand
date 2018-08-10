""" global config """
import os
from simhand.logger import logger


# 项目根目录
ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# simhand项目目录
PROJECT_PATH = os.path.join(ROOT_PATH, 'simhand')
TORNADO_SETTING = {
    'debug': True,
    'static_path': os.path.join(PROJECT_PATH, "static"),
    'template_path': os.path.join(PROJECT_PATH, "template"),
}
TORNADO_PORT = 9507

logger.info('ROOT PATH', root_path=ROOT_PATH)
logger.info('PROJECT PATH', project_path=PROJECT_PATH)
logger.info('PORT', port=TORNADO_PORT)
