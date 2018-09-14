
import json

from server.database.connection import transaction
from .managers import UserManager, RoleManager, ModuleManager
from ..common.controllers import CrudController, SuperController


class UserController(CrudController,SuperController):

    routes = {
        '/user': {'GET': 'index', 'POST': 'table'},
        '/user_insert': {'POST': 'insert'},
        '/user_update': {'POST': 'update'},
        '/user_delete': {'POST': 'change_state'}
    }

    def initialize(self):
        self.main_html = "user/views/user.html"
        self.table_html = "user/views/user_table.html"
        self.manager = UserManager

    def index(self, **extra_data):
        self.set_session()
        self.verif_privileges()
        manager = UserManager(self.db)
        result = manager.get_page()
        result['privileges'] = manager.get_privileges(self.get_user_id(), self.request.uri)
        result['roles'] = RoleManager(self.db).list_all()
        self.render(self.main_html, **result)
        self.db.close()

    def table(self):
        self.set_session()
        self.verif_privileges()
        manager = UserManager(self.db)
        data = json.loads(self.get_argument("data"))
        result = manager.get_page(**data)
        result['privileges'] = manager.get_privileges(self.get_user_id(), self.request.uri)
        self.render(self.table_html, **result)
        self.db.close()


class RoleController(CrudController, SuperController):
    routes = {
        '/role': {'GET': 'index', 'POST': 'table'},
        '/role_insert': {'POST': 'insert'},
        '/role_update': {'POST': 'update'},
    }

    def initialize(self):
        self.main_html = "user/views/role.html"
        self.table_html = "user/views/role_table.html"
        self.manager = RoleManager

    def get_extra_data(self):
        return {'modules': ModuleManager(self.db).list_all()}
