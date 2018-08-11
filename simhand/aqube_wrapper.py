import importlib
import subprocess
import os
from simhand.config import AQUBE_PATH, AQUBE_URL
from simhand.logger import logger


def get_aqube():
    if os.path.exists(AQUBE_PATH):
        old_cwd = os.getcwd()
        os.chdir(AQUBE_PATH)
        subprocess.run(['git', 'pull', '--rebase'])
        os.chdir(old_cwd)
    else:
        subprocess.run(['git', 'clone', AQUBE_URL])


def load_aqube():
    return importlib.import_module('AQube_Core.AQube_Core')


get_aqube()


class AQubeWrapper(object):
    aqube_module = load_aqube().CmdHandler()

    @classmethod
    def __getattr__(cls, item):
        if hasattr(cls.aqube_module, item):
            return getattr(cls.aqube_module, item)
        logger.info('METHOD NOT FOUND', method=item)
        return None
