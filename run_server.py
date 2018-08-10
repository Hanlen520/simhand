""" server entry """
from tornado.web import Application
from tornado.ioloop import IOLoop
import requests
import time
import threading

from simhand import config as cf
from simhand.logger import logger
from simhand.router import TORNADO_ROUTER


def ping(delay):
    time.sleep(delay)
    response = requests.get(
        url='http://localhost:{}'.format(cf.TORNADO_PORT),
    )
    if 'ALIVE' in response.text:
        logger.info('SIMHAND UP :)')
        return
    logger.error('SIMHAND ERROR :(')
    raise RuntimeError('simhand start failed')


if __name__ == "__main__":
    # stable check
    logger.info('STARTING ...')
    threading.Thread(target=ping, args=(2,)).start()

    application = Application(TORNADO_ROUTER, **cf.TORNADO_SETTING)
    application.listen(cf.TORNADO_PORT)
    IOLoop.instance().start()
