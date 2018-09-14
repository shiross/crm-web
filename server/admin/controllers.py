import json

from .managers import NotaManager
from ..common.controllers import ApiController


class NotaController(ApiController):

    routes = {
        '/excel': {'GET': 'index', 'POST': 'table'},
        '/import_excel':{'POST':'excel_import'},
        '/export_excel':{'POST':'excel_export'}
    }

    def initialize(self):
        self.main_html = "admin/views/index.html"
        self.table_html = "admin/views/table.html"
        self.manager = NotaManager

    def index(self, **extra_data):
        self.set_session()
        #self.verif_privileges()
        result = self.manager(self.db).get_page(1, 10, None, None, True)
        #result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        #result.update(self.get_extra_data())
        self.render(self.main_html, **result)
        self.db.close()

    def table(self):
        self.set_session()
        #self.verif_privileges()
        data = json.loads(self.get_argument("data"))
        result = self.manager(self.db).get_page(**data)
        #result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        self.render(self.table_html, **result)
        self.db.close()