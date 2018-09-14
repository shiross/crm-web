from datetime import datetime
import json
import os
import uuid
import os.path
from .managers import ProductManager, CompanyManager, OfficeManager, CustomerManager
from ..common.controllers import *
from ..user.managers import UserManager


class InventarioController(CrudController):
    routes = {
        '/importar_empresa': {'GET': 'index', 'POST': 'table'},
        '/importar_sucursales': {'GET': 'index2', 'POST': 'table'},
        '/importar_clientes': {'GET': 'index3', 'POST': 'table'},
        '/importar_productos': {'GET': 'index4', 'POST': 'table'},
        '/importar_promotores': {'GET': 'index5', 'POST': 'table'},
        '/importar_emp': {'POST': 'importar'},
        '/importar_suc': {'POST': 'importar2'},
        '/importar_cli': {'POST': 'importar3'},
        '/importar_prd': {'POST': 'importar4'},
        '/importar_prm': {'POST': 'importar5'},
    }

    def initialize(self):
        self.main_html = "inventario/views/index.html"
        self.main2_html = "inventario/views/index2.html"
        self.main3_html = "inventario/views/index3.html"
        self.main4_html = "inventario/views/index4.html"
        self.main5_html = "inventario/views/index5.html"
        # self.table_html = "pendientes/views/table.html"
        self.manager = CompanyManager
        self.manager2 = OfficeManager
        self.manager3 = CustomerManager
        self.manager4 = ProductManager
        self.manager5 = UserManager

    def index(self, **extra_data):
        self.set_session()
        # self.verif_privileges()
        result = self.manager(self.db).get_page(1, 10, None, None, True)
        # result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        # result.update(self.get_extra_data())
        self.render(self.main_html, **result)
        self.db.close()

    def index2(self, **extra_data):
        self.set_session()
        # self.verif_privileges()
        result = self.manager(self.db).get_page(1, 10, None, None, True)
        # result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        # result.update(self.get_extra_data())
        self.render(self.main2_html, **result)
        self.db.close()

    def index3(self, **extra_data):
        self.set_session()
        # self.verif_privileges()
        result = self.manager(self.db).get_page(1, 10, None, None, True)
        # result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        # result.update(self.get_extra_data())
        self.render(self.main3_html, **result)
        self.db.close()

    def index4(self, **extra_data):
        self.set_session()
        # self.verif_privileges()
        result = self.manager(self.db).get_page(1, 10, None, None, True)
        # result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        # result.update(self.get_extra_data())
        self.render(self.main4_html, **result)
        self.db.close()

    def index5(self, **extra_data):
        self.set_session()
        # self.verif_privileges()
        result = self.manager(self.db).get_page(1, 10, None, None, True)
        # result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        # result.update(self.get_extra_data())
        self.render(self.main5_html, **result)
        self.db.close()

    def table(self):
        self.set_session()
        # self.verif_privileges()
        data = json.loads(self.get_argument("data"))
        result = self.manager(self.db).get_page(**data)
        # result['privileges'] = UserManager(self.db).get_privileges(self.get_user_id(), self.request.uri)
        self.render(self.table_html, **result)
        self.db.close()

    def importar(self):
        """
        metodo que hace la importacion de txt o excel.
        """
        self.set_session()
        fileinfo = self.request.files['archivo'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open("server/common/resources/uploads/" + cname, 'wb')
        fh.write(fileinfo['body'])
        fh.close()
        if extn == '.xlsx':
            mee = self.manager(self.db).import_excel(cname)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
            self.db.close()

    def importar2(self):
        """
        metodo que hace la importacion de txt o excel.
        """
        self.set_session()
        fileinfo = self.request.files['archivo'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open("server/common/resources/uploads/" + cname, 'wb')
        fh.write(fileinfo['body'])
        fh.close()
        if extn == '.xlsx':
            mee = self.manager2(self.db).import_excel(cname)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
            self.db.close()

    def importar3(self):
        """
        metodo que hace la importacion de txt o excel.
        """
        self.set_session()
        fileinfo = self.request.files['archivo'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        print("flacoooo")
        print(str(datetime.now()))
        fh = open("server/common/resources/uploads/" + cname, 'wb')
        fh.write(fileinfo['body'])
        fh.close()
        print("end flacooo")
        print(str(datetime.now()))
        if extn == '.xlsx':
            mee = self.manager3(self.db).import_excel(cname)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
            self.db.close()

    def importar4(self):
        """
        metodo que hace la importacion de txt o excel.
        """
        self.set_session()
        fileinfo = self.request.files['archivo'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open("server/common/resources/uploads/" + cname, 'wb')
        fh.write(fileinfo['body'])
        fh.close()
        if extn == '.xlsx':
            mee = self.manager4(self.db).import_excel(cname)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
            self.db.close()

    def importar5(self):
        """
        metodo que hace la importacion de txt o excel.
        """
        self.set_session()
        fileinfo = self.request.files['archivo'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open("server/common/resources/uploads/" + cname, 'wb')
        fh.write(fileinfo['body'])
        fh.close()
        if extn == '.xlsx':
            mee = self.manager5(self.db).import_excel(cname)
            self.respond(message=mee['message'], success=mee['success'])
        else:
            self.respond(message='Formato de Archivo no aceptado¡¡', success=False)
            self.db.close()