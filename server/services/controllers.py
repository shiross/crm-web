import json
import os
import uuid
import os.path

from server.user.login.managers import ApiLoginManager
from ..inventario.managers import *
from ..common.controllers import *
from ..user.managers import UserManager


class ApiServiceController(ApiController):
    routes = {
        '/api/promotor/login': {'POST': 'login'},
        '/api/promotor/password': {'POST': 'change_password'},
        '/api/empresa/listar': {'POST': 'get_companies'},
        '/api/sucursal/listar': {'POST': 'get_offices'},
        '/api/cliente/listar': {'POST': 'get_customers'},
        '/api/producto/listar': {'POST': 'get_products'},
        '/api/facturas/recibir': {'POST': 'bills'},
        '/api/promotor/base': {'POST': 'database'}
    }

    def login(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            username = data['username']
            password = data['password']
            usuario = ApiLoginManager(self.db).apiLogin(username, password)
            self.respond_api(usuario.get_dict_api())
        except:
            self.respond(success=False)

    def change_password(self):
        try:
            self.set_session()
            dictionary = json.loads(self.request.body.decode('utf-8'))
            user = UserManager(self.db).get_userById(dictionary['id'])
            user.password = dictionary['password']
            updated_object = UserManager(self.db).update(user)
            self.respond_api(updated_object.get_dict_api())
        except:
            self.respond(success=False)
        self.db.close()

    def get_companies(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            promoter = UserManager(self.db).get_userById(data['id'])
            fk_company = promoter.fk_company
            company = CompanyManager(self.db).getCompanyByID(fk_company)
            # list = []
            # for company in companies:
            #     list.append(company.get_dict())
            self.respond(response=1, message=company.get_dict(), success=True)
        except:
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

    def get_offices(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            promoter = UserManager(self.db).get_userById(data['id'])
            # usuario = ApiLoginManager(self.db).apiLogin(username, password)
            fk_promoter = promoter.id
            office = OfficeManager(self.db).getOfficeByPromoter(fk_promoter)
            # list = []
            # for office in offices:
            #     list.append(office.get_dict_api())
            self.respond(response=1, message=office.get_dict_api(), success=True)
        except:
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

    def get_customers(self):
        try:
            self.set_session()
            customers = CustomerManager(self.db).list_all()
            list = []
            for customer in customers:
                list.append(customer.get_dict_api())
            self.respond(response=len(list), message=list, success=True)
        except:
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

    def get_products(self):
        try:
            self.set_session()
            products = ProductManager(self.db).list_all()
            list = []
            for product in products:
                list.append(product.get_dict_api())
            self.respond(response=len(list), message=list, success=True)
        except:
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

    def bills(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            xs = BillManager(self.db).insertBills(data)
            self.respond(response=1, success=xs, message="Recibidos todos")
        except:
            self.respond(response=0, success=False, message="Not Found")
        self.db.close()

    def database(self):
        try:
            self.set_session()
            data = json.loads(self.request.body.decode('utf-8'))
            promoter = UserManager(self.db).get_userById(data['id'])
            office = OfficeManager(self.db).getOfficeByPromoter(promoter.id)
            company = CompanyManager(self.db).getCompanyByID(promoter.fk_company)
            customers = CustomerManager(self.db).list_all()
            customer_list = []
            for customer in customers:
                customer_list.append(customer.get_dict_api())
            products = ProductManager(self.db).list_all()
            product_list = []
            for product in products:
                product_list.append(product.get_dict_api())
            result = promoter.get_bd_api()
            result['office'] = office.get_dict_api()
            result['company'] = company.get_dict()
            result['customerList'] = customer_list
            result['productList'] = product_list

            self.respond(response=1, success=True, message=result)
        except:
            self.respond(response=0, success=False, message="Nelly")
        self.db.close()
