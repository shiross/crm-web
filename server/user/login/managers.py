import hashlib

from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import make_transient

from server.common.managers import SuperManager
from ...database.connection import transaction
from ..models import User, Role, Module


class ApiLoginManager(SuperManager):
    def __init__(self, db):
        super().__init__(User, db)

    def apiLogin(self, username, password):
        # descomentar....
        password = hashlib.sha512(password.encode()).hexdigest()
        return self.db.query(User).filter(User.username == username). \
            filter(User.password == password). \
            first()


class LoginManager():
    def login(self, username, password):
        """Retorna un usuario que coincida con el username y password dados.

        parameters
        ----------
        username : str
        password : str
            El password deberá estar sin encriptar.

        returns
        -------
        User
        None
            Retornará None si no encuentra nada.
        """
        password = hashlib.sha512(password.encode()).hexdigest()
        with transaction() as session:
            usuario = session.query(User). \
                options(joinedload('role').
                        joinedload('modules').
                        joinedload('children')). \
                filter(User.username == username). \
                filter(User.password == password). \
                filter(User.enabled). \
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.role.modules = self.order_modules(usuario.role.modules)
        return usuario

    def get(self, key):
        with transaction() as session:
            usuario = session.query(User). \
                options(joinedload('role').
                        joinedload('modules').
                        joinedload('children')). \
                filter(User.id == key). \
                filter(User.enabled). \
                first()
            if not usuario:
                return None
            session.expunge(usuario)
            make_transient(usuario)
        usuario.role.modules = self.order_modules(usuario.role.modules)
        return usuario

    def order_modules(self, modules):
        modules.sort(key=lambda x: x.id)
        mods_parents = []
        mods = {}
        while len(modules) > 0:
            module = modules.pop(0)
            module.children = []
            mods[module.id] = module
            parent_module = mods.get(module.parent_id, None)
            if parent_module:
                parent_module.children.append(module)
            else:
                mods_parents.append(module)
        return mods_parents
