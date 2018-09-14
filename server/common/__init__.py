import traceback
import pickle
import json

from tornado.web import RequestHandler
from tornado.web import authenticated
from tornado.gen import coroutine
import sys


class SuperController(RequestHandler):
    """Utilice esta clase para factorizar metodos comunes de entre los controladores."""

    def get_user(self):
        """Retorna el usuario actual como objeto.

        Returns
        -------
        User
        """
        return pickle.loads(self.current_user)

    def set_user(self, user):
        """Guarda el usuario actual en la cookie.

        Parameters
        ----------
        user : User
        """
        self.set_secure_cookie("user", pickle.dumps(user))

    def get_current_user(self):
        """Sobrecarga del metodo `get_current_user()`"""
        return self.get_secure_cookie("user")

    def respond(self, response=None, success=True, message=""):
        """Retorna al cliente invocador un respuesta estándar serializada con json."""
        if not response and not success:
            response = traceback.format_exc()
            print(response)
        self.write(json.dumps({"response": response, 'success': success, 'message': message}))

    def get(self):
        """Prueba del json, solo para api controllers.

        Quitar este método en producción.
        """
        self.post()

    def handle_error(self):
        """Maneja cualquier tipo de error de forma general.

        Retorna el error al cliente invocador.
        Quitar o mejorar este método en producción.
        Usar loggs en producción.
        """
        error = traceback.format_exc()
        # error = sys.exc_info() #more details
        print(error)
        self.write("<pre>" + error + "</pre>")

    def handle_api_error(self):
        """Maneja cualquier tipo de error de forma general de las clases api.

        Retorna el error al cliente invocador en una respuesta estándar json.
        Quitar o mejorar este método en producción.
        Usar loggs en producción.
        """
        error = traceback.format_exc()
        print(error)
        self.respond(error, False)

    # ------------------ factorized metods ----------------------------------------------------------
    def initialize(self, manager=None, html_prefix=None):
        """Para asignar el manejador al controlador en las clases hijas."""
        self.manager = manager
        self.html_prefix = html_prefix