import os
from configparser import ConfigParser
from urllib.parse import urlencode
from tornado.testing import gen_test, AsyncHTTPTestCase
from tornado.web import Application

from server.routes import get_handlers
from server.database import connection


def create_app():
    config = ConfigParser()
    config.read('settings.ini')
    connection.db_url = config['Database']['url']
    settings = {
        "static_path": os.path.join(os.getcwd(), 'server', 'common', 'resources'),
        "static_url_prefix": "/resources/",
        "template_path": os.path.join(os.getcwd(), 'server'),
        "cookie_secret": config["Server"]["cookie_secret"],
        "login_url": "/login",
    }
    app = Application(get_handlers(), **settings)
    app.listen(int(config['Server']['port']), config['Server']['address'])
    return app


class LoginTest(AsyncHTTPTestCase):
    def get_app(self):
        return create_app()

    def test_loggin_success(self):
        body = urlencode({'username': 'admin', 'password': 'admin'})
        response = self.fetch('/login', method='POST', body=body, follow_redirects=False)
        assert 'Set-Cookie' in response.headers, 'usuario invalido'
        response = self.fetch('/', method='GET', headers={'Cookie': response.headers['Set-Cookie']})
        assert '/login' not in response.effective_url, 'no renderiza el index, aún logeado correctamente'

    def test_loggin_fail(self):
        body = urlencode({'username': 'admin', 'password': 'adminxx'})
        response = self.fetch('/login', method='POST', body=body, follow_redirects=False)
        assert 'Set-Cookie' not in response.headers, 'usuario no debe entrar'
