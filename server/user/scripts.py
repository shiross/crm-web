# from server.pendientes.models import Customer
from server.inventario.models import Company


def insertions():
    import hashlib
    from server.database.connection import transaction
    from .models import User, Role, Module

    with transaction() as session:
        user_m = Module(title='G. Usuarios', name='user_module', icon='person')
        usuarios_m = Module(title='Usuarios', route='/user', name='users', icon='bubble_chart')
        roles_m = Module(title='Roles', route='/role', name='roles', icon='bubble_chart')
        user_m.children.append(usuarios_m)
        user_m.children.append(roles_m)
        query_usuario = Module(title='Consultar', route='', name='user_query', menu=False)
        insert_usuario = Module(title='Adicionar', route='/user_insert', name='user_insert', menu=False)
        update_usuario = Module(title='Actualizar', route='/user_update', name='user_update', menu=False)
        delete_usuario = Module(title='Dar de Baja', route='/user_delete', name='user_delete', menu=False)

        query_role = Module(title='Consultar', route='', name='role_query', menu=False)
        insert_role = Module(title='Adicionar', route='/role_insert', name='role_insert', menu=False)
        update_role = Module(title='Actualizar', route='/role_update', name='role_update', menu=False)

        admin_m = Module(title='Importar Excel', route='', name='excel', icon='bubble_chart')
        import_company = Module(title='Importar Empresa', route='/importar_empresa', name='company_module', icon='bubble_chart')
        import_sucursal = Module(title='Importar Sucursal', route='/importar_sucursales', name='office_module',
                                icon='bubble_chart')
        import_product = Module(title='Importar Productos', route='/importar_productos', name='product_module',
                                icon='bubble_chart')
        import_customer = Module(title='Importar Clientes', route='/importar_clientes', name='customer_module',
                                icon='bubble_chart')
        import_promoter = Module(title='Importar Promotores', route='/importar_promotores', name='promoter_module',
                                icon='bubble_chart')

        # inventary_excel = Module(title='Importar Inventario', route='/importar_inventario', name='inventary_module',
        #                        icon='bubble_chart')
        # consultas_m = Module(title='Consultas', route='', name='query', icon='search')
        # query = Module(title='Busqueda ;)', route='/query', name='query_module', icon='bubble_chart')

        usuarios_m.children.append(query_usuario)
        usuarios_m.children.append(insert_usuario)
        usuarios_m.children.append(update_usuario)
        usuarios_m.children.append(delete_usuario)
        roles_m.children.append(query_role)
        roles_m.children.append(insert_role)
        roles_m.children.append(update_role)
        admin_m.children.append(import_company)
        admin_m.children.append(import_sucursal)
        admin_m.children.append(import_product)
        admin_m.children.append(import_customer)
        admin_m.children.append(import_promoter)
        # admin_m.children.append(inventary_excel)

        # consultas_m.children.append(query)
        company = Company(name='admin',nit='123',activity='admin',payment='tc',text='admin',coin=19)
        admin_role = Role(name='Administrador', description='Todos los Permisos.')
        # admin_customer = Customer(name='Herracruz')
        user_role = Role(name='Usuario', description='Cliente')
        customer_role = Role(name='Cliente', description='Cliente app movil')
        admin_role.modules.append(user_m)
        admin_role.modules.append(usuarios_m)
        admin_role.modules.append(roles_m)
        # admin_role.modules.append(consultas_m)
        admin_role.modules.append(query_usuario)
        admin_role.modules.append(insert_usuario)
        admin_role.modules.append(update_usuario)
        admin_role.modules.append(delete_usuario)
        admin_role.modules.append(query_role)
        admin_role.modules.append(insert_role)
        admin_role.modules.append(update_role)
        admin_role.modules.append(admin_m)
        admin_role.modules.append(import_company)
        admin_role.modules.append(import_sucursal)
        admin_role.modules.append(import_customer)
        admin_role.modules.append(import_product)
        admin_role.modules.append(import_promoter)
        # admin_role.modules.append(inventary_excel)
        # admin_role.modules.append(query)

        # customer_role.modules.append(consultas_m)
        # customer_role.modules.append(query)
        # admin_role.modules.append(import_company)


        hex_dig = hashlib.sha512(b'admin').hexdigest()
        # name = 'admin', last_name = 'admin', mail = 'admin@host.com',
        super_user = User(name='admin',username='admin', password=hex_dig)
        super_user.role = admin_role
        super_user.company=company
        # super_user.customer = admin_customer

        # session.add(admin_customer)
        session.add(super_user)
        session.add(user_role)
        session.add(customer_role)

        # hex_dig = hashlib.sha512(b'12345').hexdigest()
        # for i in range(1, 100):
        #     session.add(User(name='nombre',
        #                      last_name='apellido',
        #                      mail='mail@' + str(i) + '.com',
        #                      username='username' + str(i),
        #                      password=hex_dig,
        #                      role_id=2))
        session.commit()
