def insertions():
    from server.database.connection import transaction
    from .models import Bill, Company, Detail, Customer, Office, Product

    with transaction() as session:
        pass
