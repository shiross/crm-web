from sqlalchemy import Column, Integer, String, Float, Date, Text, DateTime, Time
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from ..database.models import Base
from ..database.serializable import Serializable


class Company(Serializable, Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    nit = Column(String(14), nullable=False)
    activity = Column(String(50), nullable=False)
    payment = Column(String(40), nullable=False)
    text = Column(String(255), nullable=False)
    coin = Column(Float, nullable=False)

    def get_dict_api(self, way=None):
        dictionary = super().get_dict(way)
        empresa = {"id": dictionary["id"],
                   "name": dictionary["name"],
                   "nit": dictionary["nit"],
                   "activity": dictionary["activity"],
                   "payment": dictionary["payment"],
                   "text": dictionary["text"],
                   "coin": dictionary["coin"]
                   }
        return empresa


class Office(Serializable, Base):
    way = {'company': {}, 'promoter': {}}
    __tablename__ = "office"
    id = Column(Integer, primary_key=True)
    fk_company = Column(Integer, ForeignKey('company.id'), nullable=False)
    fk_promoter = Column(Integer, ForeignKey('usr_user.id'), nullable=False)
    name = Column(String(45), nullable=False)
    address = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    department = Column(String(45), nullable=False)
    key = Column(String(30), nullable=False)
    auth = Column(String(30), nullable=False)
    dsfini = Column(Integer, nullable=False)
    dsffin = Column(Integer, nullable=False)
    limdate = Column(Date, nullable=False)

    company = relationship('Company', cascade="save-update")
    promoter = relationship('User', cascade="save-update")

    def get_dict_api(self, way={'company': {}, 'promoter': {}}):
        dictionary = super().get_dict(way)
        sucursal = {"id": dictionary["id"],
                    "name": dictionary["name"],
                    "address": dictionary["address"],
                    "phone": dictionary["phone"],
                    "department": dictionary["department"],
                    "key": dictionary["key"],
                    "auth": dictionary["auth"],
                    "dsfini": dictionary["dsfini"],
                    "dsffin": dictionary["dsffin"],
                    "limdate": dictionary["limdate"],
                    "fkCompany": dictionary["company"]["id"],
                    "fkPromoter": dictionary["promoter"]["id"]
                    }
        return sucursal


        # def get_dict_api(self, way={'family': {}, 'group': {}}):
        #     dictionary = super().get_dict(way)
        #     grupo = {
        #         "id_grupo": dictionary["group"]["id_group"],
        #         "linea": dictionary["group"]["line"],
        #         "nombre": dictionary["group"]["name"],
        #         "familia": dictionary["family"]["name"]
        #     }
        #     return grupo


class Product(Serializable, Base):
    way = {'company': {}}
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    fk_company = Column(Integer, ForeignKey('company.id'), nullable=False)
    name = Column(String(50), nullable=False)
    unit = Column(String(10), nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    stock = Column(Float, nullable=False)

    company = relationship('Company', cascade="save-update")

    # family = relationship('Family', cascade="save-update")

    def get_dict_api(self, way={'company': {}}):
        dictionary = super().get_dict(way)
        grupo = {"id": dictionary["id"],
                 "name": dictionary["name"],
                 "unit": dictionary["unit"],
                 "price": dictionary["price"],
                 "discount": dictionary["discount"],
                 "stock": dictionary["stock"],
                 "fkCompany": dictionary["company"]["id"],
                 }
        return grupo


class Customer(Serializable, Base):
    way = {'company': {}}
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    fk_company = Column(Integer, ForeignKey('company.id'), nullable=False)
    name = Column(String(100), nullable=False)
    nit = Column(String(18), nullable=False)

    company = relationship('Company', cascade="save-update")

    def get_dict_api(self, way={'company': {}}):
        dictionary = super().get_dict(way)
        cliente = {
            "id": dictionary["id"],
            "name": dictionary["name"],
            "nit": dictionary["nit"],
            "fkCompany": dictionary["company"]["id"]
        }
        return cliente


class Bill(Serializable, Base):
    way = {'company': {}, 'customer': {}}
    __tablename__ = "bill"

    id = Column(Integer, primary_key=True)
    id_bill = Column(Integer, nullable=False)
    fk_company = Column(Integer, ForeignKey('company.id'), nullable=False)
    fk_customer = Column(Integer, ForeignKey('customer.id'), nullable=False)
    fk_promoter = Column(Integer, ForeignKey('usr_user.id'), nullable=False)
    date = Column(Date, nullable=False)
    hour = Column(Time, nullable=False)
    nit = Column(String(18), nullable=False)
    name = Column(String(45), nullable=False)
    ctrlcode = Column(String(20), nullable=False)

    company = relationship('Company', cascade="save-update")
    customer = relationship('Customer', cascade="save-update")
    promoter = relationship('User', cascade="save-update")

    details = relationship('Detail', cascade="save-update")


class Detail(Serializable, Base):
    way = {'bill': {}, 'product': {}}
    __tablename__ = "detail"

    id = Column(Integer, primary_key=True)
    fk_bill = Column(Integer, ForeignKey('bill.id'), nullable=False)
    fk_product = Column(Integer, ForeignKey('product.id'), nullable=False)

    quantity = Column(Float, nullable=False)
    oriprize = Column(Float, nullable=False)
    finprize = Column(Float, nullable=False)
    total = Column(Float, nullable=False)

    # group = relationship('Group', cascade="save-update")
    bill = relationship('Bill', cascade="save-update")
    product = relationship('Product', cascade="save-update")


    # def get_dict_api(self, way={'subgroup': {
    #
    # }}):
    #     dictionary = super().get_dict(way)
    #     producto = {"codigo": dictionary["code"],
    #                 "codigo_origen": dictionary["code_origin"],
    #                 "nombre": dictionary["name"],
    #                 "stock": dictionary["stock"],
    #                 "subgrupo": dictionary["subgroup"]["name"],
    #                 "sublinea": "",
    #                 "grupo": "",
    #                 "linea": "",
    #                 "familia": "",
    #                 }
    #     return producto
