import traceback
import json

from tornado.web import RequestHandler, HTTPError
from tornado.web import authenticated
from tornado.gen import coroutine

from server.common.managers import Error
from server.database.connection import transaction, get_session
from ..common.utils import decorators
from server.user.login.managers import LoginManager
from server.user.managers import UserManager


class SuperController(RequestHandler):
    """Utilice esta clase para factorizar metodos comunes de entre los controladores."""

    def get_user_id(self):
        return int(self.get_current_user())

    def get_user(self):
        return LoginManager().get(self.get_user_id())

    def set_user_id(self, user_id):
        self.set_secure_cookie('user', str(user_id))

    def get_current_user(self):
        """Sobrecarga del metodo `get_current_user()`"""
        return self.get_secure_cookie("user")

    def respond(self, response=None, success=True, message=""):
        """Retorna al cliente invocador un respuesta estándar serializada con json."""
        # if not response and not success:
        #     response = traceback.format_exc()
        self.write(json.dumps({"response": response, 'success': success, 'message': message}))

    def respond_api(self, response=None, success=True):
        """Retorna al cliente invocador un respuesta estándar serializada con json para la aplicacion c#."""
        if not response and not success:
            response = 0
            print(response)
        self.write(json.dumps(response))

    def get(self):
        """Prueba del json, solo para api controllers.

        Quitar este método en producción.
        """
        self.post()

    def write_error(self, status_code, **kwargs):
        self.render("common/views/error.html",
                    error_code=status_code,
                    message=kwargs.get('message', 'Internal Server Error'),
                    url_redirect='/')

    def set_session(self):
        if not hasattr(self, 'db'):
            self.db = get_session()


class MethodDispatcher(SuperController):
    routes = {}

    def no_method(self):
        raise HTTPError(401)

    def get(self):
        getattr(self, self.routes[self.request.uri].get('GET', 'no_method'))()

    def post(self):
        getattr(self, self.routes[self.request.uri].get('POST', 'no_method'))()


class ApiController(MethodDispatcher):
    def no_method(self):
        """lanza un error cuando no encuentra el metodo"""
        raise HTTPError(401)

    @coroutine
    def get(self):
        getattr(self, self.routes[self.request.uri].get('GET', 'no_method'))()

    @coroutine
    def post(self):
        getattr(self, self.routes[self.request.uri].get('POST', 'no_method'))()


class CrudController(MethodDispatcher):
    @decorators(authenticated, coroutine)
    def get(self):
        super().get()

    @decorators(authenticated, coroutine)
    def post(self):
        super().post()

    def index(self):
        self.set_session()
        self.verif_privileges()
        result = self.manager(self.db).get_page(1, 10, None, None, True)
        result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        result.update(self.get_extra_data())
        self.render(self.main_html, **result)
        self.db.close()

    def table(self):
        self.set_session()
        self.verif_privileges()
        data = json.loads(self.get_argument("data"))
        result = self.manager(self.db).get_page(**data)
        result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        self.render(self.table_html, **result)
        self.db.close()

    def insert(self):
        self.set_session()
        self.verif_privileges()
        ins_manager = self.manager(self.db)
        dictionary = json.loads(self.get_argument("object"))
        object = ins_manager.entity(**dictionary)
        indicted_object = ins_manager.insert(object)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Insertado correctamente!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al insertar')
        self.db.close()

    def update(self):
        self.set_session()
        self.verif_privileges()
        ins_manager = self.manager(self.db)
        dictionary = json.loads(self.get_argument("object"))
        object = ins_manager.entity(**dictionary)
        indicted_object = ins_manager.update(object)
        if len(ins_manager.errors) == 0:
            self.respond(indicted_object.get_dict(), message='Actualizado correctamente!')
        else:
            self.respond([item.__dict__ for item in ins_manager.errors], False, 'Ocurrió un error al actualizar')
        self.db.close()

    def change_state(self):
        self.set_session()
        self.verif_privileges()
        id = json.loads(self.get_argument("id"))
        state = json.loads(self.get_argument("enabled"))
        updated_object = self.manager(self.db).change_state(id, state)
        if state:
            message = "Dado de Alta!"
        else:
            message = "Dado de Baja!"
        self.respond(updated_object.get_dict(), message=message)
        self.db.close()

    def verif_privileges(self):
        if not UserManager(self.db). \
                has_access(self.get_user_id(),
                           self.request.uri):
            raise HTTPError(401)

    def set_session(self):
        if not hasattr(self, 'db'):
            self.db = get_session()

    def get_extra_data(self):
        return {}


class Error404Handler(RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render("common/views/error.html",
                    error_code='404',
                    message="This page doesn't exist",
                    url_redirect='/')
