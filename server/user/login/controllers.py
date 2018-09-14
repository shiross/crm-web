from tornado.gen import coroutine

from ...common.controllers import SuperController
from .managers import LoginManager


class Login(SuperController):
    @coroutine
    def get(self):
        """Renderiza el login"""
        self.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.set_header('Pragma', 'no-cache')
        self.set_header('Expires', '0')
        usuario = self.get_secure_cookie("user")
        if usuario:
            self.redirect("/")
        else:
            self.clear_cookie("user")
            self.render("user/login/view.html")

    @coroutine
    def post(self):
        """Inicia sesión en la aplicación.

        Si se inicia sesión con éxito enctonces se guarda el
        usuario en la cookie caso contrario se vuelve al login.
        """
        self.set_session()
        username = self.get_argument('username', default=None)
        password = self.get_argument('password', default=None)
        user = LoginManager().login(username, password)
        if user:
            self.set_user_id(user.id)
        self.redirect("/")


class Logout(SuperController):
    @coroutine
    def get(self):
        self.clear_cookie('user')
        self.redirect(self.get_argument("next", "/"))


class ApiLogin(SuperController):
    @coroutine
    def post(self):
        """Devuelve el usuario que coincida con el username y password dados.

        Si ocurre algún error se retornará None en la respuesta json al
        cliente invocador.
        """
        try:
            username = self.get_argument('username')
            password = self.get_argument('password')
            usuario = LoginManager().login(username, password)
            self.respond(usuario.getDict())
        except:
            self.respond(success=False)
