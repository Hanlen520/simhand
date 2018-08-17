import importlib
import pysubmodule
from simhand.config import PYSUBMODULE_JSON
from simhand.logger import logger


pysubmodule.sync(PYSUBMODULE_JSON)


def load_aqube():
    return importlib.import_module('AQube_Core.AQube_Core')


class AQubeWrapper(object):
    aqube_module = load_aqube().CmdHandler()

    @classmethod
    def __getattr__(cls, item):
        if hasattr(cls.aqube_module, item):
            return getattr(cls.aqube_module, item)
        logger.info('METHOD NOT FOUND', method=item)
        return None
