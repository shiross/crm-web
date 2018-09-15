def insertions():
    from server.database.connection import transaction
    from .models import Customer,Zone

    with transaction() as session:
        pass
