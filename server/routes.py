

from server.services.controllers import ApiServiceController
from .user.controllers import UserController, RoleController
from .user.login.controllers import Login, Logout
from .main.controllers import Index, IndexPortal
from .inventario.controllers import  InventarioController


def get_handlers():
    """Retorna una lista con las rutas, sus manejadores y datos extras."""
    handlers = list()

    #login
    handlers.append((r'/login', Login))
    handlers.append((r'/logout', Logout))

    # main
    handlers.append((r'/', Index))


    #user
    handlers.extend(get_routes(UserController))

    #role
    handlers.extend(get_routes(RoleController))


    handlers.extend(get_routes(ApiServiceController))

    handlers.extend(get_routes(InventarioController))

    return handlers


def get_routes(handler):
    routes = list()
    for route in handler.routes:
        routes.append((route, handler))
    return routes

