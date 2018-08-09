""" server entry """
from tornado.web import Application
from tornado.ioloop import IOLoop

from simhand import config as cf
from simhand.router import TORNADO_ROUTER

if __name__ == "__main__":
    print('SIMHAND UP :)')
    application = Application(TORNADO_ROUTER, **cf.TORNADO_SETTING)
    application.listen(cf.TORNADO_PORT)
    IOLoop.instance().start()
