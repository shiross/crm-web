import socket
from threading import Thread
import time
import sys
import os

from configparser import ConfigParser
from tornado.web import Application
from tornado.ioloop import IOLoop
import schedule

from .common.controllers import Error404Handler
from server.routes import get_handlers
from .database import connection


def get_settings(config):
    return {
        "static_path": os.path.join(os.getcwd(), 'server', 'common', 'resources'),
        "static_url_prefix": "/resources/",
        "template_path": os.path.join(os.getcwd(), 'server'),
        "cookie_secret": config["Server"]["cookie_secret"],
        "login_url": "/login",
        "debug": True
    }


def main():
    # Thread(target=stop_tornado).start()
    Thread(target=launch_schedule).start()
    create_app()


# def stop_tornado():
#     while not 'q' == input('Enter q to quit: \n'):
#         pass
#     IOLoop.instance().stop()


def create_app():
    config = ConfigParser()
    config.read('settings.ini')
    connection.db_url = config['Database']['url']
    settings = get_settings(config)
    app = Application(get_handlers(), **settings, default_handler_class=Error404Handler)

    # app.listen(int(config['Server']['port']), config['Server']['address'])
    # print('running server on  http://'+config['Server']['address']+':'+config['Server']['port'])
    # print(socket.gethostbyname_ex(socket.gethostname()))
    # print(socket.gethostbyname_ex(socket.gethos))
    app.listen(int(config['Server']['port']), socket.gethostbyname(socket.gethostname()))
    # app.listen(int(config['Server']['port']), "192.168.1.45")
    print('running server on  http://' + socket.gethostbyname(socket.gethostname()) + ':' + config['Server']['port'])
    IOLoop.instance().start()


def launch_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
