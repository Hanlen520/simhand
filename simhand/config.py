""" global config """
import os
from structlog import get_logger


logger = get_logger()

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
TORNADO_SETTING = {
    'debug': True,
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'template_path': os.path.join(os.path.dirname(__file__), "template"),
}
TORNADO_PORT = 9507
