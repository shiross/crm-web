import hashlib

from server.common.managers import SuperManager, Error
from .models import User, Role, Module, Access
from sqlalchemy.exc import IntegrityError


class UserManager(SuperManager):
    def __init__(self, db):
        super().__init__(User, db)

    def insert(self, user):
        if user.role_id > 1:
            user.password = hashlib.sha512(user.password.encode()).hexdigest()
            return super().insert(user)
        return Error('unknown')

    def get_user(self, username, password):
        password = hashlib.sha512(password.encode()).hexdigest()
        return self.db.query(User).filter(User.username == username, User.password == password).first()

    def get_userByname(self, username):
        # password = hashlib.sha512(password.encode()).hexdigest()
        return self.db.query(User).filter(User.username == username).first()

    def get_userById(self, id):
        return self.db.query(User).filter(User.id == id).first()

    def update(self, user):
        if user.role_id > 1:
            if not user.password or user.password == '':
                user.password = (self.db.query(User.password)
                                 .filter(User.id == user.id).first())[0]
            else:
                user.password = hashlib.sha512(user.password.encode()).hexdigest()
            return super().update(user)

    def change_password(self, object, fk_user):
        # object.password = hashlib.sha512(password.encode()).hexdigest()
        object['fk_user'] = fk_user
        object = User(**object)
        self.db.merge(object)
        self.db.commit()
        return object

    def import_excel(self, cname):
        try:
            wb = load_workbook(filename="server/common/resources/uploads/" + cname)
            sheet = wb.get_sheet_by_name(name='Hoja1')  # parametrizable......
            colnames = ['idEmpresa', 'idPromotor', 'NomPromotor', 'UsrPromotor',
                        'PasPromotor']
            min_row = 1
            indices = {cell[0].value: n - min_row for n, cell in
                       enumerate(sheet.iter_cols(min_row=min_row, max_row=min_row), start=min_row) if
                       cell[0].value in colnames}
            for row in sheet.iter_rows(min_row=min_row + 1):
                if row[indices['idEmpresa']].value is not None and \
                                row[indices['idPromotor']].value is not None and \
                                row[indices['NomPromotor']].value is not None and \
                                row[indices['UsrPromotor']].value is not None and \
                                row[indices['PasPromotor']].value is not None:



                    hex_dig = hashlib.sha512(row[indices['PasPromotor']].value.encode()).hexdigest()
                    # hex_dig = hashlib.sha512(b"row[indices['PasPromotor']].value").hexdigest()
                    if UserManager(self.db).get_userById(row[indices['idPromotor']].value) is None:
                        usuario = User(
                            id=row[indices['idPromotor']].value,
                            name=row[indices['NomPromotor']].value,
                            username=row[indices['UsrPromotor']].value,
                            password=hex_dig,
                            role_id=3,
                            enabled=True,
                            fk_company=10
                        )
                        self.db.add(usuario)
                        self.db.flush()
            self.db.commit()
            return {'message': 'Importado Todos Correctamente.', 'success': True}
        except IntegrityError as e:
            self.db.rollback()
            if 'UNIQUE constraint failed: rrhh_persona.dni' in str(e):
                return {'message': 'CI duplicado', 'success': False}
            if 'UNIQUE constraint failed: rrhh_empleado.codigo' in str(e):
                return {'message': 'codigo de empleado duplicado', 'success': False}
            return {'message': str(e), 'success': False}

    def get_privileges(self, id, route):
        parent_module = self.db.query(Module). \
            join(Role.modules).join(User). \
            filter(Module.route == route). \
            filter(User.id == id). \
            filter(User.enabled). \
            first()
        if not parent_module:
            return dict()
        modules = self.db.query(Module). \
            join(Role.modules).join(User). \
            filter(Module.parent_id == parent_module.id). \
            filter(User.id == id). \
            filter(User.enabled)
        privileges = {parent_module.name: parent_module}
        for module in modules:
            privileges[module.name] = module
        return privileges

    def has_access(self, id, route):
        aux = self.db.query(User). \
            join(Role).join(Access).join(Module). \
            filter(User.id == id). \
            filter(Module.route == route). \
            filter(User.enabled). \
            all()
        return len(aux) != 0

    def get_page(self, page_nr=1, max_entries=10, like_search=None, order_by=None, ascendant=True, query=None):
        query = self.db.query(User).join(Role).filter(Role.id > 1)
        return super().get_page(page_nr, max_entries, like_search, order_by, ascendant, query)


class RoleManager(SuperManager):
    def __init__(self, db):
        super().__init__(Role, db)

    def get_page(self, page_nr=1, max_entries=10, like_search=None, order_by=None, ascendant=True, query=None):
        query = self.db.query(self.entity).filter(Role.id > 1)
        return super().get_page(page_nr, max_entries, like_search, order_by, ascendant, query)

    def update(self, role):
        if role.id > 1:
            return super().update(role)

    def list_all(self):
        return self.db.query(Role).filter(Role.id > 1)


class ModuleManager:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Module).filter(Module.parent_id == None)
