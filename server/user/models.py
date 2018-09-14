from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship

from ..database.models import Base
from ..database.serializable import Serializable


class User(Serializable, Base):
    way = {'role': {'modules': {}, 'company': {}},
           }

    __tablename__ = 'usr_user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    # last_name = Column(String(50), nullable=False)
    # mail = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    role_id = Column(Integer, ForeignKey('usr_role.id'), nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)
    fk_company = Column(Integer, ForeignKey('company.id'), nullable=False)
    # customer_id = Column(Integer, ForeignKey('cns_cli.id'), nullable=False)

    company = relationship('Company', cascade="save-update")
    role = relationship('Role')

    # customer = relationship('Customer')

    def get_dict(self, way=None):
        dictionary = super().get_dict(way)
        return dictionary

    def get_dict_api(self, w={'company': {}}):
        dictionary = super().get_dict(w)
        empleado_persona = {
            "id": dictionary["id"],
            "username": dictionary["username"],
            "password": dictionary["password"],
            "name": dictionary["name"],
            "fkCompany": dictionary["company"]["id"]}
        return empleado_persona

    def get_bd_api(self, w={'company': {}}):
        dictionary = super().get_dict(w)
        object = {
            "company": dictionary["company"]["name"],
            "office": "",
            "customerList": "",
            "productList": "",
        }
        return object


Access = Table('usr_access', Base.metadata,
               Column('role_id', Integer, ForeignKey('usr_role.id')),
               Column('module_id', Integer, ForeignKey('usr_module.id')))


class Role(Serializable, Base):
    way = {'users': {}, 'modules': {}}

    __tablename__ = 'usr_role'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(200), nullable=False)

    users = relationship('User')
    modules = relationship('Module', secondary=Access)


class Module(Serializable, Base):
    way = {'roles': {}}

    __tablename__ = 'usr_module'

    id = Column(Integer, primary_key=True)
    route = Column(String(100))
    title = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False, unique=True)
    icon = Column(String(50), nullable=False, default='home')
    menu = Column(Boolean, nullable=False, default=True)
    parent_id = Column(Integer, ForeignKey('usr_module.id'))

    roles = relationship('Role', secondary=Access)
    children = relationship('Module')
