from tornado.web import authenticated
from tornado.gen import coroutine

from server.common.utils import decorators
from ..common.controllers import SuperController


class Index(SuperController):
    @decorators(authenticated, coroutine)
    def get(self):
        usuario = self.get_user()
        if usuario:
            self.render("main/view.html", user=usuario)
        else:
            self.redirect('/logout')


class IndexPortal(SuperController):
    def get(self):
        if self.get_current_user() is None:
            self.redirect('/nota')